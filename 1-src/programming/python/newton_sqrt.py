# This .py file shows the evolution of function my_sqrt() using Newton's method,
# which references [Introduction to Software Testing](https://www.fuzzingbook.org/html/Intro_Testing.html).

def my_sqrt(x):
    approx = None
    guess = x / 2
    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2
    return approx

print(my_sqrt(4))
print(my_sqrt(2))
print(my_sqrt(16))

####################

def my_sqrt_with_log(x):
    approx = None
    guess = x / 2
    while approx != guess:
        print("approx =", approx) # Debugging
        approx = guess
        guess = (approx + x / approx) / 2
    return approx

my_sqrt_with_log(9)

#####################

# Test

## v1: manual
t1 = my_sqrt(2) * my_sqrt(2)
print(t1)

## v2: automatic
result = my_sqrt(4)
expected_result = 2.0

if result == expected_result:
    print("Test passed.")
else:
    print("Test failed.")

## v3: compact `assert()` 
assert my_sqrt(4) == 2

## v4: reasonable threshold for float
EPSILON = 1e-8

assert abs(my_sqrt(4) - 2) < EPSILON

## v5: function form
def assertEquals(x, y, epsilon=1e-8):
    assert abs(x - y) < epsilon

assertEquals(my_sqrt(4), 2)
assertEquals(my_sqrt(9), 3)
assertEquals(my_sqrt(100), 10)

## v6: thousands of test cases
for n in range(1, 1000):
    assertEquals(my_sqrt(n) * my_sqrt(n), n)

## v7: timeout
import time

start = time.time()
for n in range(1, 1000):
    assertEquals(my_sqrt(n) * my_sqrt(n), n)
end = time.time()
print(f'The elapsed time is {end - start}s.')

## v8: at random
import random
import time

start = time.time()
for i in range(1, 10000):
    x = 1 + random.random() * 1000000
    assertEquals(my_sqrt(x) * my_sqrt(x), x)
end = time.time()
print(f'The elapsed time is {end - start}s.')

## v9: run-time check
def my_sqrt_checked(x):
    root = my_sqrt(x)
    assertEquals(root * root, x)
    return root

t = my_sqrt_checked(2.0)
print(t)

########

# System Input

## v1

def sqrt_program(arg: str) -> None:
    x = int(arg)
    print(f'The root of {x} is {my_sqrt(x)}.')

sqrt_program("4")
sqrt_program("-1")

## v2: fixed negative

def sqrt_program(arg: str) -> None:
    x = int(arg)
    if x < 0:
        print("Illegal Input")
    else:
        print(f'The root of {x} is {my_sqrt(x)}.')

### `pip install fuzzingbook` needed
from fuzzingbook.ExpectError import ExpectTimeout

with ExpectTimeout(1):
    sqrt_program("-1")

from fuzzingbook.ExpectError import ExpectError

with ExpectError():
    sqrt_program("xyzzy")

## v3: fixed non-float

def sqrt_program(arg: str) -> None:
    try:
        x = float(arg)
    except ValueError:
        print("Illegal Input.")
    else:
        if x < 0:
            print("Illegal Number.")
        else:
            print(f'The root of {x} is {my_sqrt(x)}.')

sqrt_program("4")
sqrt_program("-1")
sqrt_program("xyzzy")

from fuzzingbook.ExpectError import ExpectError

with ExpectError():
    root = my_sqrt(0)

## v4: fixed zero

def my_sqrt_fixed(x):
    assert 0 <= x
    if x == 0:
        return 0
    return my_sqrt(x)
