# project-3

You will be writing a Library simulator involving multiple classes.  You will write the LibraryItem, Patron and Library classes, and the three classes that inherit from LibraryItem (Book, Album and Movie).  All data members of each class should be marked as private (a leading underscore in the name).  Since they're private, if you need to access them from outside the class, you should do so via get or set methods.  Any get or set methods should be named per the usual convention ("get_" or "set_" followed by the name of the data member).

Here are descriptions of the three classes:

**LibraryItem:**
* id_code - a unique identifier for a LibraryItem - you can assume uniqueness, you don't have to enforce it
* title - cannot be assumed to be unique
* location - a LibraryItem can be "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT"
* checked_out_by - refers to the Patron who has it checked out (if any)
* requested_by - refers to the Patron who has requested it (if any); a LibraryItem can only be requested by one Patron at a time
* date_checked_out - when a LibraryItem is checked out, this will be set to the current_date of the Library
* init method - takes an id_code, and title; checked_out_by and requested_by should be initialized to None; a new LibraryItem's location should be on the shelf
* get and set methods as needed
 
**Book/Album/Movie:**
* These three classes all inherit from LibraryItem.
* All three will need a method called get_check_out_length that returns the number of days that type of library item may be checked out for.  For a Book it's 21 days, for an Album it's 14 days, and for a Movie it's 7 days.
* All three will have an additional field.  For Book, it's a string field called author.  For Album, it's a string field called artist.  For Movie, it's a string field called director.  There will also need to be get methods to return the values of these fields.
 
**Patron:**
* id_num - a unique identifier for a Patron - you can assume uniqueness, you don't have to enforce it
* name - cannot be assumed to be unique
* checked_out_items - a collection of LibraryItems that a Patron currently has checked out
* fine_amount - how much the Patron owes the Library in late fines (measured in dollars); this is allowed to go negative
* init method - takes an idNum and name
* get and set methods as needed
* add_library_item - adds the specified LibraryItem to checked_out_items
* remove_library_item - removes the specified LibraryItem from checked_out_items
* amend_fine - a positive argument increases the fine_amount, a negative one decreases it; this is allowed to go negative
 
**Library:**
* holdings - a collection of the LibraryItems in the Library
* members - a collection of the Patrons in the Library
* current_date - stores the current date represented as an integer number of "days" since the Library object was created
* an init method that initializes the current_date to zero
* add_library_item - adds the parameter to holdings
* add_patron - adds the parameter to members
* get_library_item - returns the LibraryItem corresponding to the ID parameter, or None if no such LibraryItem is in the holdings
* get_patron - returns the Patron corresponding to the ID parameter, or None if no such Patron is a member
* check_out_library_item
  * takes as parameters a patron ID and an item ID, in that order
  * if the specified Patron is not in the Library's members, return "patron not found"
  * if the specified LibraryItem is not in the Library's holdings, return "item not found"
  * if the specified LibraryItem is already checked out, return "item already checked out"
  * if the specified LibraryItem is on hold by another Patron, return "item on hold by other patron"
  * otherwise update the LibraryItem's checkedOutBy, dateCheckedOut and Location
  * if the LibraryItem was on hold for this Patron, update requestedBy
  * update the Patron's checkedOutItems
  * return "check out successful"
* return_library_item
  * takes as its parameter an item ID
  * if the specified LibraryItem is not in the Library's holdings, return "item not found"
  * if the LibraryItem is not checked out, return "item already in library"
  * update the Patron's checkedOutItems
  * update the LibraryItem's location depending on whether another Patron has requested it (if so, it should go on the hold shelf)
  * update the LibraryItem's checkedOutBy
  * return "return successful"
* request_library_item
  * takes as parameters a patron ID and an item ID, in that order
  * if the specified Patron is not in the Library's members, return "patron not found"
  * if the specified LibraryItem is not in the Library's holdings, return "item not found"
  * if the specified LibraryItem is already requested, return "item already on hold"
  * update the LibraryItem's requestedBy
  * if the LibraryItem is on the shelf, update its location to on hold
  * return "request successful" 
* pay_fine
  * takes as a parameter the amount that is being paid (not the negative of that amount) 
  * if the specified Patron is not in the Library's members, return "patron not found"
  * use amendFine to update the Patron's fine; return "payment successful"
* increment_current_date
  * takes no parameters
  * increment current date
  * increase each Patron's fines by 10 cents for each overdue LibraryItem they have checked out (using amendFine)
 
 
Note - a LibraryItem can be on request without its location being the hold shelf (if another Patron has it checked out);


One limited example of how your classes might be used is:
```
      b1 = Book("345", "Phantom Tollbooth", "Juster")
      a1 = Album("456", "...And His Orchestra", "The Fastbacks")
      m1 = Movie("567", "Laputa", "Miyazaki")
      print(b1.get_author())
      print(a1.get_artist())
      print(m1.get_director())
      
      p1 = Patron("abc", "Felicity")
      p2 = Patron("bcd", "Waldo")
      
      lib = Library()
      lib.add_library_item(b1)
      lib.add_library_item(a1)
      lib.add_patron(p1)
      lib.add_patron(p2)
      
      lib.check_out_library_item("bcd", "456")
      loc = a1.get_location()
      lib.request_library_item("abc", "456")
      for i in range(57):
         lib.increment_current_date()   # 57 days pass
      p2_fine = p2.get_fine_amount()
      lib.pay_fine("bcd", p2_fine)
      lib.return_library_item("456")
```
You are responsible for testing all of the required functions to make sure they operate as specified.

 

Your file must be named: **Library.py**

Just to think about: Since there are three possible locations for a LibraryItem, there are six hypothetical changes in location.  Are all six possible according to these specifications?

 
