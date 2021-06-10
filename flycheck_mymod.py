print(f'Hello from {__name__}!')

x = 100

y = [10, 20, 30]


def hello(name):
    return f'Hello, {name}!'


# this code means:
# Only run the stuff in the "if" block if we were runs# as a standalone program
# if we were imported by someone, don't execute stuff below the line.
if __name__ == '__main__':
    print(f'Goodbye from {__name__}!')
