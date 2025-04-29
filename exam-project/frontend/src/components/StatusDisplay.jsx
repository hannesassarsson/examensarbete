import React from "react";

const StatusDisplay = ({ status }) => {
  return (
    <div className="card text-center mt-4">
      <div
        className={`card-header ${
          status.checkedIn ? "bg-success" : "bg-danger"
        } text-white`}
      >
        {status.checkedIn ? "Incheckad" : "Utcheckad"}
      </div>
      <div className="card-body">
        <h5 className="card-title">
          {status.checkedIn
            ? "Du är just nu incheckad."
            : "Du är just nu utcheckad."}
        </h5>
        {status.time && (
          <p className="card-text">
            Senaste aktivitet: <strong>{status.time}</strong>
          </p>
        )}
      </div>
    </div>
  );
};

export default StatusDisplay;