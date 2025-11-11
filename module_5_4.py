
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact is not found"
        except IndexError:
            return "Give me phone please."    

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_phone(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "change phone."

    
@input_error
def phone_print(args, contacts):
    name = args[0]
    return contacts[name]

@input_error
def all_print(contacts):
    string_value = ""
    for key, value in contacts.items():
        string_value += f"{key} {value}\n"    
    return string_value.strip() 


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "phone":
            print(phone_print(args, contacts))
        elif command == "all":
            print(all_print(contacts))  
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()