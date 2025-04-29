import React, { useState, useRef, useEffect } from "react";
import Swal from "sweetalert2";

const LoginScreen = ({ onLogin }) => {
  const [pin, setPin] = useState("");
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current?.focus();

    const enterFullScreen = async () => {
      if (document.documentElement.requestFullscreen) {
        await document.documentElement.requestFullscreen();
      }
    };
    enterFullScreen();
  }, []);

  useEffect(() => {
    if (pin.length === 4) {
      handlePinSubmit();
    }
  }, [pin]);

  const handlePinSubmit = async () => {
    try {
      const response = await fetch("http://192.168.0.37:3000/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pin }),
      });

      if (response.ok) {
        const data = await response.json();

        // Visa en kort lyckad animation
        Swal.fire({
          position: "center",
          icon: "success",
          title: "Tagg scannad!",
          showConfirmButton: false,
          timer: 800,
          timerProgressBar: true,
        });

        localStorage.setItem("token", data.token);
        localStorage.setItem("user", JSON.stringify(data.user));
        setTimeout(() => {
          onLogin(data.token, data.user);
        }, 800); // Vänta lite så användaren ser animationen
      } else {
        Swal.fire({
          icon: "error",
          title: "Fel",
          text: "Felaktig PIN-kod",
        });
        setPin("");
      }
    } catch (err) {
      Swal.fire({
        icon: "error",
        title: "Något gick fel",
        text: "Kunde inte verifiera lösenord",
      });
      setPin("");
    }
  };

  return (
    <div className="d-flex justify-content-center align-items-center min-vh-100 bg-light px-4">
      <div className="bg-white rounded shadow p-5 w-100 w-md-50">
        <h2 className="text-center mb-4">Scanna din tagg</h2>
        <input
          ref={inputRef}
          type="password"
          className="form-control form-control-lg mb-4 text-center"
          placeholder="Scanna NFC eller skriv PIN"
          value={pin}
          onChange={(e) => setPin(e.target.value)}
          maxLength={4}
          inputMode="numeric"
          autoFocus
        />
      </div>
    </div>
  );
};

export default LoginScreen;