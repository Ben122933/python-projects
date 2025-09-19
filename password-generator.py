import secrets
import string


class Password:
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        #Get characters from a string module
        self.base_characters: str = string.ascii_lowercase + string.digits

        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation

    def generate(self) -> str:
        password: list[str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))

        return ''.join(password)

    def check_strength(self) -> None:
        password_strength: list = ['strong', 'not strong enough', 'weak', 'very weak']
        uppercase_used: bool = self.use_uppercase
        symbols_used: bool = self.use_symbols
        length_of_character: int = self.length

        if uppercase_used == True and symbols_used == True and length_of_character >= 16:
            strength: str = password_strength[0]
            print(f'Your password is {strength}')

        elif uppercase_used == False and symbols_used == True and length_of_character >= 16:
            strength: str = password_strength[1]
            print(f'Your password is {strength}, Uppercase character is not used')

        elif uppercase_used == True and symbols_used == False and length_of_character >= 16:
            strength: str = password_strength[1]
            print(f'Your password is {strength}, symbols are not used')

        elif uppercase_used == True and symbols_used == True and length_of_character < 16:
            strength: str = password_strength[1]
            print(f'Your password is {strength}, length of password is less than 16')

        elif uppercase_used == False and symbols_used == True and length_of_character < 16:
            strength: str = password_strength[2]
            print(f'Your password is {strength}, uppercase characters are not used and the length of password is less '
                  f'than 16')

        elif uppercase_used == True and symbols_used == False and length_of_character < 16:
            strength: str = password_strength[2]
            print(f'Your password is {strength}, symbols are not used and the length of password is less than 16')

        elif uppercase_used == False and symbols_used == False and length_of_character >= 16:
            strength: str = password_strength[2]
            print(f'Your password is {strength}, uppercase characters and symbols are not used')

        else:
            strength: str = password_strength[3]
            print(f'Your password is {strength}, symbols and uppercase characters are not used and the length of the '
                  f'password is less than 16')


def main():
    length: int = int(input('How long do you want your password?'))

    uppercase = input('Do you want uppercase characters? (Yes or No)')

    if uppercase.lower() == 'yes':
       uppercase = True
    elif uppercase.lower() == 'no':
        uppercase = False

    else:
        raise ValueError

    symbols = input('Do you want symbols?')
    if symbols.lower() == 'yes':
        symbols = True
    elif symbols.lower() == 'no':
        symbols = False
    else:
        raise ValueError

    password: Password = Password(length=length, uppercase=uppercase, symbols=symbols)
    generated: str = password.generate()
    print(generated)
    print(password.check_strength())

if __name__ == '__main__':
    main()
