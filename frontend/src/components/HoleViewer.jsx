import React, { useEffect, useState } from 'react';
import axios from 'axios';

const HoleViewer = ({ holeId }) => {
  const [hole, setHole] = useState(null);
  const [distance, setDistance] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchHoleData = async () => {
      try {
        const res = await axios.get(`/api/hole/${holeId}`);
        setHole(res.data);
      } catch (err) {
        console.error('Error fetching hole info:', err);
      }
    };

    const fetchDistance = async () => {
      try {
        const locationRes = await axios.get('/api/location');
        const playerLoc = locationRes.data;

        const distanceRes = await axios.post(`/api/hole/${holeId}/distance`, {
          lat: playerLoc.lat,
          lon: playerLoc.lon,
        });

        setDistance(distanceRes.data.distance_to_green_yards);
      } catch (err) {
        console.error('Error calculating distance:', err);
      }
    };

    const loadAll = async () => {
      await fetchHoleData();
      await fetchDistance();
      setLoading(false);
    };

    loadAll();
  }, [holeId]);

  if (loading || !hole) return <p>Loading hole data...</p>;

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: 'auto' }}>
      <h2>Hole {hole.number}</h2>
      <img
        src={hole.image_url}
        alt={`Hole ${hole.number}`}
        style={{ width: '100%', borderRadius: '12px', marginBottom: '15px' }}
      />
      <p><strong>Par:</strong> {hole.par}</p>
      <p><strong>Yardage:</strong> {hole.yardage} yds</p>
      <p><strong>Handicap:</strong> {hole.handicap}</p>
      <p><strong>Type:</strong> {hole.type}</p>
      <p><strong>Notes:</strong> {hole.notes}</p>
      <hr />
      <h3>📍 Distance to Green: {distance ? `${distance} yards` : 'N/A'}</h3>
    </div>
  );
};

export default HoleViewer;
