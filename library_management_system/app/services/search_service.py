from app.enums.search_criteria import SearchCriteria


class _SearchService:
    def __init__(self):
        self._books_by_id = {}

    def add_book(self, book):
        pass

    def update_book(self, book_id, payload):
        pass

    def remove_book(self, book_id):
        pass

    def search(self, criteria, query):
        if criteria == SearchCriteria.AUTHOR:
            return self._search_by_author(query)
        elif criteria == SearchCriteria.PUBLICATION_DATE:
            return self._search_by_publication_date(query)
        elif criteria == SearchCriteria.SUBJECT:
            return self._search_by_subject(query)
        elif criteria == SearchCriteria.TITLE:
            return self._search_by_title(query)

    def search_by_author(self, author_name):
        pass

    def search_by_title(self, book_title):
        pass

    def search_by_subject(self, subject):
        pass

    def _search_by_publication_date(self, pub_date):
        pass


search_service = _SearchService()
