class Track:

    def __init__(self, title, duration):
        self._title = title
        self._duration = duration

    @property
    def title(self):
        return self._title

    @property
    def duration(self):
        return self._duration