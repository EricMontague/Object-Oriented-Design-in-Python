class RecordState:
    
    NOT_YET_PLAYED = 0
    PLAYING = 1
    PAUSED = 2
    ENDED = 3


class Record:

    def __init__(self, title, artist, tracks):
        self._title = title
        self._artist = artist
        self._tracks = tracks
        self._state = RecordState.NOT_YET_PLAYED
    
    @property
    def title(self):
        return self._title

    @property
    def artist(self):
        return self._artist

    @property
    def tracks(self):
        return self._tracks[:]
    
    @property
    def num_tracks(self):
        return len(self._tracks)

    @property
    def state(self):
        return self._state
    
    def pause(self):
        self._state = RecordState.PAUSED

    def end(self):
        self._state = RecordState.ENDED

    def duration(self):
        total = 0
        for track in self._tracks:
            total += track.duration
        return total

    def get_track(self, track):
        return self._tracks.get(track)
