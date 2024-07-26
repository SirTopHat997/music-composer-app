import React, { useEffect, useState } from 'react';
import { Howl } from 'howler';

const MusicPlayer = ({ trackUrl }) => {
  const [playing, setPlaying] = useState(false);
  let sound;

  useEffect(() => {
    if (trackUrl) {
      sound = new Howl({ src: [trackUrl] });
    }
  }, [trackUrl]);

  const togglePlay = () => {
    if (playing) {
      sound.pause();
    } else {
      sound.play();
    }
    setPlaying(!playing);
  };

  return (
    <div>
      <button onClick={togglePlay}>{playing ? 'Pause' : 'Play'}</button>
    </div>
  );
};

export default MusicPlayer;
