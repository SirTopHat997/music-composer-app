import React from 'react';

const TrackControls = ({ onSkip, onLike }) => {
  return (
    <div>
      <button onClick={onSkip}>Skip</button>
      <button onClick={onLike}>Like</button>
    </div>
  );
};

export default TrackControls;
