
def main():
    print_square(3)


def print_square(size):
    # Print a square of size x size
    for i in range(size):
        # Print a row of size #
        for j in range(size):
            # Print a #
            print("#", end='')
            # Print a space
        print()
    