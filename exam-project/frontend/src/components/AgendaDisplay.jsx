// src/components/AgendaDisplay.jsx
import React, { useEffect, useState } from 'react';

const AgendaDisplay = () => {
  const [events, setEvents] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchCalendar = async () => {
      try {
        const response = await fetch('http://192.168.0.37:3000/api/calendar');
        if (!response.ok) {
          throw new Error('Något gick fel vid hämtning av kalender.');
        }
        const data = await response.json();
        setEvents(data);
      } catch (error) {
        console.error('Fel vid hämtning av kalender:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchCalendar();
  }, []);

  if (loading) {
    return (
      <div className="text-center mt-5">
        <div className="spinner-border text-primary" role="status">
          <span className="sr-only">Laddar...</span>
        </div>
        <p>Laddar dagens agenda...</p>
      </div>
    );
  }

  return (
    <div className="mt-5">
      <h3 className="text-center mb-4">Dagens Agenda</h3>
      {events.length > 0 ? (
        <ul className="list-group">
          {events.map((event, index) => (
            <li key={index} className="list-group-item">
              <div className="d-flex justify-content-between align-items-center">
                <strong>{event.summary || "Namnlöst event"}</strong>
                <span>
                  {event.start?.dateTime
                    ? new Date(event.start.dateTime).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
                    : 'Heldag'}
                </span>
              </div>
            </li>
          ))}
        </ul>
      ) : (
        <p className="text-center text-muted">Inget schemalagt för idag eller imorgon.</p>
      )}
    </div>
  );
};

export default AgendaDisplay;