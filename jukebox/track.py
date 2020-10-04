class Track:

    def __init__(self, title, duration, record):
        self._title = title
        self._record = record
        self._duration = duration

    @property
    def track_title(self):
        return self._title

    @property
    def duration(self):
        return self._duration

    def record_title(self):
        return self._record.title