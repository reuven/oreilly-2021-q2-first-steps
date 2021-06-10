def menu(*args):
    while True:
        choice = input(f'Enter choice {args}: ').strip()

        if choice in args:
            return choice

        print(f'Illegal choice; try again')


# when I say "import menu" from another file, the __name__ for this module is 'menu'.
# When it is run from the command line, the __name__ for this module is '__main__'.

# I can use that distinction to have functionality that only runs when
# the module/program is run interactively.

if __name__ == '__main__':
    print('Demo menu usage!')

    user_choice = menu('a', 'b', 'c')
    print(f'User choice was {user_choice}')
