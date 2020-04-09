
# Example of Errors
# ---------------------------------------------------------------------
# Un-comment
# while True print('Hello world')

print(10 * (1 / 0))
print(4 + 'spam' * 3)
print('2' + 2)


# Handling Exceptions
# ---------------------------------------------------------------------

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


# Example of try - except - else
# ---------------------------------------------------------------------
import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


# Example of Raising Exceptions
# ---------------------------------------------------------------------
# Un-comment
# raise NameError('HiThere')

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


# Example of User-defined Exceptions
# ---------------------------------------------------------------------

class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


# Example of Clean-up Actions - finally
# ---------------------------------------------------------------------
def bool_return():
    try:
        return True
    finally:
        return False

bool_return()