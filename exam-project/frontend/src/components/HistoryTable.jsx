import React, { useEffect, useState } from "react";

const HistoryTable = ({ refreshTrigger }) => {
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const response = await fetch("http://192.168.0.37:3000/api/history", {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        });

        if (response.ok) {
          const data = await response.json();
          setHistory(data);
        } else {
          console.error("Fel vid hämtning av historik");
        }
      } catch (error) {
        console.error("Kunde inte hämta historik:", error);
      }
    };

    fetchHistory();
  }, [refreshTrigger]);

  const formatAction = (action) => {
    return action === "check-in" ? "Incheckning" : "Utcheckning";
  };

  return (
    <div className="mt-4 px-4">
      <h3 className="text-center mb-4">Historik</h3>
      <div className="table-responsive">
        <table className="table table-striped table-bordered">
          <thead className="table-light">
            <tr>
              <th>Användare</th>
              <th>Åtgärd</th>
              <th>Tidpunkt</th>
            </tr>
          </thead>
          <tbody>
            {history.length > 0 ? (
              history.map((entry) => (
                <tr key={entry.id}>
                  <td>{entry.user_name}</td>
                  <td>{formatAction(entry.action)}</td>
                  <td>{entry.timestamp}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="3" className="text-center">
                  Laddar historik...
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default HistoryTable;