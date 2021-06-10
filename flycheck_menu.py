def menu(*args):
    while True:
        choice = input('Enter choice {args}: ').strip()

        if choice in args:
            return choice

        print(f'Illegal choice; try again')
