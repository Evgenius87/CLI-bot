def input_error(func):
    def inner(*args):
        
        try:
            result  = func(*args)
            return result
        except ValueError:
            print('Enter user name')
        except KeyError:
            print('Unknwn comand! Please try again')
        except IndexError:
            print('Give me name and phone please')   
           
    return inner


@input_error
def hallo(args):
    hi = "How can I help you?"
    return hi

@input_error
def add(args):
    if args[1].isdigit():
        contacts[args[0]] = args[1]
    else:
        raise IndexError

@input_error
def change(args):
    if args[1].isdigit():
        contacts[args[0]] = args[1]
    else:
        raise IndexError

@input_error
def phone(name):
    return contacts[name[0]]

@input_error
def show_all(args):
    return contacts

@input_error
def good_bye(args):
    return "Good bye!"
    

contacts = {}

COMANDS = {
    'hallo': hallo,
    'add': add,
    'change': change,
    'phone' : phone,
    'show all': show_all,
    'good bye': good_bye,
    "close": good_bye, 
    "exit": good_bye
}


def parser_comand(in_put):
    comands = in_put.lower()
    comands  = comands.split(' ')
    if comands[0] == 'good':
        comand = f'{comands[0]} {comands[1]}'
        args = ''
        return comand, args
    elif comands[0] == 'show':
        comand = f'{comands[0]} {comands[1]}'
        args = ''
        return comand, args
    else:
        comand = comands[0]
        args = comands[1:]
        return comand, args


@input_error
def main(*args):
    
    while True:
        comand, args = parser_comand(input('>>>'))
        
        if args:
            handler = (COMANDS[comand])
            if handler(args) != None:
                print(handler(args))                    
        else:
            handler = (COMANDS[comand])
            print(handler(args))        
            if handler(args) == 'Good bye!':
                break


if __name__ == '__main__':
    main()