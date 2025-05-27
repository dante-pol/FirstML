import time


def main():

    for i in range(0, 101, 1):
        print(f'\r{i}%..', end="")
        time.sleep(0.25)

def sum(a, b):
    return a + b

main()