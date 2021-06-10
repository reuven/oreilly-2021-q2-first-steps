def menu(*args):
    while True:
        choice = input(f'Enter choice {args}: ').strip()

        if choice in args:
            return choice

        print(f'Illegal choice; try again')
