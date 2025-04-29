import React, { useState, useEffect } from "react";  // Lägg till denna rad
import LoginScreen from "./components/LoginScreen";
import CheckInOutButtons from "./components/CheckInOutButtons";
import StatusDisplay from "./components/StatusDisplay";
import HistoryTable from "./components/HistoryTable";
import AgendaDisplay from "./components/AgendaDisplay";
import Swal from "sweetalert2";

function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [user, setUser] = useState(
    JSON.parse(localStorage.getItem("user")) || null
  );
  const [status, setStatus] = useState({ checkedIn: false, time: null });
  const [refreshHistory, setRefreshHistory] = useState(false);

  useEffect(() => {
    const fetchStatus = async () => {
      if (!token) return;
      try {
        const response = await fetch("http://192.168.0.37:3000/api/status", {
          headers: { Authorization: `Bearer ${token}` },
        });
        const data = await response.json();

        if (response.ok) {
          setStatus({
            checkedIn: data.status === "check-in",
            time: new Date().toLocaleString(),
          });
        } else {
          console.error("Fel vid hämtning av status", data);
        }
      } catch (error) {
        console.error("Kunde inte hämta status:", error);
      }
    };

    fetchStatus();
  }, [token, refreshHistory]);

  const handleLogin = (receivedToken, receivedUser) => {
    setToken(receivedToken);
    setUser(receivedUser);
    localStorage.setItem("token", receivedToken);
    localStorage.setItem("user", JSON.stringify(receivedUser));
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    setToken(null);
    setUser(null);
    setStatus({ checkedIn: false, time: null });
  };

  return (
    <div className="min-vh-100 bg-light px-4 py-6">
      <h1 className="text-center mb-6 text-primary font-weight-bold">
        NFC In/Utcheckning
      </h1>

      {!token ? (
        <LoginScreen onLogin={handleLogin} />
      ) : (
        <div className="max-w-xl mx-auto">
          <h2 className="text-center text-dark font-weight-semibold mb-4">
            Välkommen {user.name}!
          </h2>
          <AgendaDisplay />
          <CheckInOutButtons
            setStatus={setStatus}
            status={status}
            user={user}
            onActionComplete={() => setRefreshHistory(!refreshHistory)}
          />

          <StatusDisplay status={status} />

          <button
            className="mt-4 btn btn-dark w-100 py-3 font-weight-bold"
            onClick={handleLogout}
          >
            Logga ut
          </button>

          <div className="mt-5">
            <HistoryTable refreshTrigger={refreshHistory} />
          </div>
          
        </div>
      )}
    </div>
  );
}

export default App;