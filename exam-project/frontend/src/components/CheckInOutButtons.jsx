import React from "react";
import Swal from "sweetalert2";

const CheckInOutButtons = ({ setStatus, onActionComplete, status }) => {
  const handleAction = async (action) => {
    const now = new Date().toLocaleString();

    if (action === "check-in" && status.checkedIn) {
      Swal.fire("Redan incheckad", "Du är redan incheckad!", "info");
      return;
    }
    if (action === "check-out" && !status.checkedIn) {
      Swal.fire("Redan utcheckad", "Du är redan utcheckad!", "info");
      return;
    }

    setStatus({ checkedIn: action === "check-in", time: now });

    try {
      const response = await fetch("http://192.168.0.37:3000/api/history", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
        body: JSON.stringify({ action }),
      });

      if (!response.ok) throw new Error("Kunde inte logga åtgärd.");

      Swal.fire({
        icon: "success",
        title: action === "check-in" ? "Incheckad!" : "Utcheckad!",
        timer: 1500,
        showConfirmButton: false,
      });

      onActionComplete();
    } catch (err) {
      Swal.fire("Fel", err.message, "error");
    }
  };

  const handleChangePin = async () => {
    const { value: newPin } = await Swal.fire({
      title: "Ändra PIN",
      input: "password",
      inputLabel: "Ny PIN-kod (4 siffror)",
      inputAttributes: {
        maxlength: 4,
        pattern: "\\d{4}",
        autocapitalize: "off",
        autocorrect: "off",
      },
      showCancelButton: true,
      inputValidator: (value) => {
        if (!value || value.length !== 4) {
          return "PIN måste vara exakt 4 siffror";
        }
      },
    });

    if (newPin) {
      try {
        const response = await fetch("http://192.168.0.37:3000/api/change_pin", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
          body: JSON.stringify({ new_pin: newPin }),
        });

        if (!response.ok) throw new Error("PIN-ändring misslyckades");

        Swal.fire("Klart!", "PIN uppdaterad.", "success");
      } catch (err) {
        Swal.fire("Fel", err.message, "error");
      }
    }
  };

  return (
    <div className="d-flex flex-column gap-3 mt-4">
      <button
        className="btn btn-success btn-lg"
        onClick={() => handleAction("check-in")}
      >
        Incheckning
      </button>
      <button
        className="btn btn-danger btn-lg"
        onClick={() => handleAction("check-out")}
      >
        Utcheckning
      </button>
      <button
        className="btn btn-warning btn-lg"
        onClick={handleChangePin}
      >
        Ändra PIN
      </button>
    </div>
  );
};

export default CheckInOutButtons;