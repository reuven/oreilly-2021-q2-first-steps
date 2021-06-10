def menu(*args):
    while True:
        choice = input(f'Enter choice {args}: ').strip()

        if choice in args:
            return choice

        print(f'Illegal choice; try again')


# when I say "import menu" from another file, the __name__ for this module is 'menu'.
# When it is run from the command line, the __name__ for this module is '__main__'.

As a resultt, 