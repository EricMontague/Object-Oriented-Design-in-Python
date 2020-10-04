from collections import deque


class JukeBox:

    def __init__(self, cost_per_song):
        self._records = {}
        self._song_queue = deque()
        self._cost_per_song = cost_per_song
        self._currently_playing = None
        self._volume = 0
        self._money_needed_to_play_song = cost_per_song

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new_volume):
        self._volume = new_volume

    def insert_record(self, record):
        self._records[record.title] = record

    def remove_record(self, title):
        record = self._records.get(title)
        return record

    def cost_per_song(self):
        return self._cost_per_song

    def currently_playing(self):
        return self._currently_playing

    def next_song(self):
        if self._song_queue:
            return self._song_queue[0]
        return None
    
    def get_records(self):
        return self._records[:]

    def take_money(self, money):
        self._money_needed_to_play_song += money

    def play(self, record_title, track_number):
        if self.can_play_song() > 0:
            raise ValueError(
            f"You need to insert {self._money_needed_to_play_song} more cents in order to play a song"
        )
        record = self._records.get(record_title)
        if not record:
            raise ValueError(f"There is no record titled: {record_title}")
        track = record.get_track(track_number)
        if not track:
            raise ValueError(f"This record doesn't have a track number {track_number}")
        if self._currently_playing is None:
            self._currently_playing = record
        else:
            self._song_queue.append(track)
        self._money_needed_to_play_song -= self._cost_per_song
    
    def can_play_song(self):
        return self._money_needed_to_play_song > 0

    def pause(self):
        if self._currently_playing:
            title = self._currently_playing.record_title()
            self._records[title].pause()

    def end_song(self):
        if self._currently_playing:
            title = self._currently_playing.record_title()
            self._records[title].end()
            self._currently_playing = None
