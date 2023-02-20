from collections import UserDict


class AdressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record

 
class Record:
    
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, phones):
        for phone in phones:
            self.add_phone(phone)

    def del_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)



class Field:
    
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass

