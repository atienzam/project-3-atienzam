class LibraryItem:
    def __init__(self, id_code, title, location, checked_out_by, requested_by):
        self._id_code = id_code
        self._title = title
        self._location = location
        self._checked_out_by = checked_out_by
        self._requested_by = requested_by

    def get_check_out(self):
        return


class Patron:
    def __init__(self, idNum, name):
        self._idNum = idNum
        self._name = name

    def get_check_out(self):
        return


class Library:
    def __init__(self, current_date):
        self._current_date = current_date

    def get_check_out(self):
        return