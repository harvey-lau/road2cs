# The Notes of [Introduction of Software Testing](https://www.fuzzingbook.org/html/Intro_Testing.html)

This section shows an example of function `my_sqrt()` using Newton's method, which evolves along with testing.

## 0x01 Version 1

```Python
def my_sqrt(x):
    approx = None
    guess = x / 2
    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2
    return approx

#################

print(my_sqrt(4))
print(my_sqrt(2))
print(my_sqrt(16))

```

## 0x02 Version 2: Debugging

```Python
def my_sqrt_with_log(x):
    approx = None
    guess = x / 2
    while approx != guess:
        print("approx =", approx) # Debugging
        approx = guess
        guess = (approx + x / approx) / 2
    return approx

#################

my_sqrt_with_log(9)
```

## 0x03 Version 3: Testing

```Python
def my_sqrt(x):
    approx = None
    guess = x / 2
    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2
    return approx

#################

# test 1: manual
my_sqrt(2) * my_sqrt(2)

# test 2: automatic
result = my_sqrt(4)
expected_result = 2.0

if result == expected_result:
    print("Test passed.")
else:
    print("Test failed.")

# test 3: compact `assert()`
assert my_sqrt(4) == 2

# test 4: reasonable threshold for float
EPSILON = 1e-8

assert abs(my_sqrt(4) - 2) < EPSILON

# test 5: testing with function
def assertEquals(x, y, epsilon=1e-8):
    assert abs(x - y) < epsilon

assertEquals(my_sqrt(4), 2)
assertEquals(my_sqrt(9), 3)
assertEquals(my_sqrt(100), 10)

# test 6: thousands of test cases
def assertEquals(x, y, epsilon=1e-8):
    assert abs(x - y) < epsilon

for n in range(1, 1000):
    assertEquals(my_sqrt(n) * my_sqrt(n), n)

# test 7: testing with timeout
import time

def assertEquals(x, y, epsilon=1e-8):
    assert abs(x - y) < epsilon

start = time.time()
for n in range(1, 1000):
    assertEquals(my_sqrt(n) * my_sqrt(n), n)
end = time.time()
print(f'The elapsed time is {end - start}s.')

# test 8: testing with timeout at random
import random
import time

def assertEquals(x, y, epsilon=1e-8):
    assert abs(x - y) < epsilon

start = time.time()
for i in range(1, 10000):
    x = 1 + random.random() * 1000000
    assertEquals(my_sqrt(x) * my_sqrt(x), x)
end = time.time()
print(f'The elapsed time is {end - start}s.')

# test 9: run-time check
def assertEquals(x, y, epsilon=1e-8):
    assert abs(x - y) < epsilon

def my_sqrt_checked(x):
    root = my_sqrt(x)
    assertEquals(root * root, x)
    return root
```

## 0x04 Version 4: System Input

```Python
def sqrt_program(arg: str) -> None:
    x = int(arg)
    print(f'The root of {x} is {my_sqrt(x)}.')

##############################################

sqrt_program("4")
sqrt_program("-1") # Bug
```

## 0x05 Version 5: Fixed the Negative Values

```Python
def sqrt_program(arg: str) -> None:
    x = int(arg)
    if x < 0:
        print("Illegal Input")
    else:
        print(f'The root of {x} is {my_sqrt(x)}.')

##################################################

# test 1
from fuzzingbook.ExpectError import ExpectTimeout

with ExpectTimeout(1):
    sqrt_program("-1")

# test 2
from fuzzingbook.ExpectError import ExpectError

with ExpectError():
    sqrt_program("xyzzy")
```

## 0x06 Version 6: Fixed the Non-float Values

```Python
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

######################################################

# test 1
sqrt_program("4")

# test 2
sqrt_program("-1")

# test 3
sqrt_program("xyzzy")

# test 4
from fuzzingbook.ExpectError import ExpectError

with ExpectError():
    root = my_sqrt(0)
```

## 0x07 Version 7: Final Version

```Python
def my_sqrt_fixed(x):
    assert 0 <= x
    if x == 0:
        return 0
    return my_sqrt(x)
```
