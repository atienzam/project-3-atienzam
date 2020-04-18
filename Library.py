# Author: Marc Atienza
# Date: 4/17/2020
# Description: This program is supposed to represent a Library simulator. Unfortunately I ran out of time and could not
#   finish the project in time.

class LibraryItem:
   def __init__(self, library_item_id, title):
       self._library_item_id = library_item_id
       self._title = title
       self._location = "ON_SHELF"
       self._checked_out_by = None
       self._requested_by = None
       self._date_checked_out = 0

   def get_library_item_id(self):
       return self._library_item_id

   def get_title(self):
       return self._title

   def get_location(self):
       return self._location

   def set_checked_out_by(self, checked_out_patron):
       self._checked_out_by = checked_out_patron

   def get_checked_out_by(self):
       return self._checked_out_by

   def set_requested_by(self, who_requested):
       self._requested_by = who_requested

   def get_requested_by(self):
       return self._requested_by

   def set_date_checked_out(self, date):
       self._date_checked_out = date

   def get_date_checked_out(self):
       return self._date_checked_out


class Book(LibraryItem):
   def __init__(self, library_item_id, title, author):
       super().__init__(library_item_id, title)
       self._check_out_length = 21
       self._author = author

   def get_check_out_length(self):
       return self._check_out_length

   def get_author(self):
       return self._author


class Album(LibraryItem):
   def __init__(self, library_item_id, title, artist):
       super().__init__(library_item_id, title)
       self._check_out_length = 14
       self._artist = artist

   def get_check_out_length(self):
       return self._check_out_length

   def get_artist(self):
       return self._artist


class Movie(LibraryItem):
   def __init__(self, library_item_id, title, director):
       super().__init__(library_item_id, title)
       self._check_out_length = 7
       self._director = director

   def get_check_out_length(self):
       return self._check_out_length

   def get_author(self):
       return self._director


class Patron:
   def __init__(self, patron_id, name):
       self._patron_id = patron_id
       self._name = name
       self._checked_out_items = []
       self._fine_amount = 0

   def get_patron_id(self):
       return self._patron_id

   def get_name(self):
       return self._name

   def get_checked_out_items(self):
       return self._checked_out_items

   def get_fine_amount(self):
       return self._fine_amount

   def add_library_item(self, library_item):
       self._checked_out_items.append(library_item)

   def remove_library_item(self, library_item):
       self._checked_out_items.remove(library_item)

   def amend_fine(self, fine):
       self._fine_amount += fine


class Library:
   def __init__(self):
       self._holdings = []
       self._members = []
       self._current_date = 0

   def add_library_item(self, library_item_obj):
       """takes library item object and adds it to catalog(holdings)"""
       self._holdings.append(library_item_obj)

   def add_patron(self, patron_obj):
       """takes a patron object and adds them to member list"""
       self._members.append(patron_obj)

   def get_library_item_from_id(self, library_item_id):
       if library_item_id in self._holdings:
           return library_item_id
       else:
           return None

   def get_patron_from_id(self, patron_id):
       if patron_id in self._members:
           return patron_id
       else:
           return None

   def check_out_library_item(self, patron_id, library_item_id):
       if patron_id not in self._members:
           return "patron not found"
       if library_item_id not in self._holdings:
           return "item not found"

       location = library_item_id.get_location()
       if location == "CHECKED_OUT":
           return "item already checked out"
       if location == "ON_HOLD_SHELF":
           return "item on hold by other patron"
       else:
           patron_id.


   def return_library_item(self, library_item_id):
       if library_item_id not in self._holdings:
           return "item not found"

       location = library_item_id.get_location()
       if location != "CHECKED_OUT":
           return "item already in library"


   def request_library_item(self, patron_id, library_item_id):
       if patron_id not in self._members:
           return "patron not found"
       if library_item_id not in self._holdings:
           return "item not found"
       if library_item_id.get_requested_by() is not None:
           return "item already on hold"

   def pay_fine(self, patron_id, amount):
       if patron_id not in self._members:
           return "patron not found"
       else:
           patron_id.amend_fine(amount)
           return "payment successful"

   def increment_current_date(self):
       self._current_date += 1
       if self._current_date >
