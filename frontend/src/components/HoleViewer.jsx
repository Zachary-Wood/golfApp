import React, { useEffect, useState } from 'react';
import axios from 'axios';

const HoleViewer = () => {
  const [hole, setHole] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchHoleData = async () => {
      try {
        const res = await axios.get('/api/hole/1'); 
        console.log('✅ Hole data:', res.data);
        setHole(res.data);
      } catch (err) {
        console.error('❌ Error fetching hole info:', err.response || err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchHoleData();
  }, []);

  if (loading) return <p>Loading hole data...</p>;
  if (!hole) return <p>No hole data found.</p>;

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
    </div>
  );
};

export default HoleViewer;

