import React, { useState, useEffect } from 'react';
import MusicPlayer from './components/MusicPlayer';
import TrackControls from './components/TrackControls';

const App = () => {
  const [trackUrl, setTrackUrl] = useState('');

  useEffect(() => {
    // Fetch the initial track from backend
    fetch('/generate?user_id=1')
      .then(response => response.json())
      .then(data => setTrackUrl(data.track_url));
  }, []);

  return (
    <div className="App">
      <h1>AI Music Composer</h1>
      <MusicPlayer trackUrl={trackUrl} />
      <TrackControls onSkip={() => {/* handle skip */}} onLike={() => {/* handle like */}} />
    </div>
  );
};

export default App;
