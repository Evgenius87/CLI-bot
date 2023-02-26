from collections import UserDict
from datetime import datetime

class AdressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self, n = 3):
        self.n = n
        records_list = []
        counter = 0
        for record in self.data:
            records_list.append(record)
            counter += 1
            if counter == self.n:
                yield records_list
                records_list = []
                counter = 0
        if records_list:
            yield records_list
        
         
class Record:
    
    def __init__(self, name, phone, birthday = None) -> None:
        self.name = name
        self.phone = phone
        self.birthday = birthday.value
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, phones):
        for phone in phones:
            self.add_phone(phone)

    def del_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def days_to_birthday(self):
        self.birth = self.birthday
        today = datetime.now()
        this_day = datetime(today.year, today.month, today.day)
        birthday_next_year = datetime(today.year+1, self.birth.value.month, self.birth.value.day)
        birthday_this_year = datetime(today.year, self.birth.value.month, self.birth.value.day)
        difference = birthday_this_year - this_day
        if difference.days < 0:
            difference = birthday_next_year - this_day
        return f'{difference.days} days'

class Field:
    
    def __init__(self, value) -> None:
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Name(Field):
    pass


class Phone(Field):

    @Field.value.setter
    def value(self, value):
        if len(value) != 12:
            raise ValueError("Phone must contains 12 symbols.")
        if not value.startswith('380'):
            raise ValueError("Phone must starts from '380'.")
        if not value.isnumeric():
            raise ValueError('Wrong phones.')
        self._value = value


class BirthDay(Field):

    @Field.value.setter
    def value(self, value):
        try:
            self.birthday = datetime.strptime(value, '%d %m %Y')
        except:
            raise ValueError('format birthday: dd mm yyyy')
        self._value = self.birthday
    
        
