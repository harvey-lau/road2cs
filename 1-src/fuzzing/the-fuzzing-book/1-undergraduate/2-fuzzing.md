# The Notes of [Fuzzing: Breaking Things with Random Inputs](https://www.fuzzingbook.org/html/Fuzzer.html)

## 0x01 The Intro of Python Classes

- Fuzzer as a base class for fuzzers;
- Runner as a base class for programs under test.

```Python
from fuzzingbook.Fuzzer import Runner
from fuzzingbook.Fuzzer import RandomFuzzer
from fuzzingbook.Fuzzer import PrintRunner
from fuzzingbook.Fuzzer import ProgramRunner

random_fuzzer = RandomFuzzer()
s = random_fuzzer.fuzz()
print(s)

print_runner = PrintRunner()
t = random_fuzzer.run(print_runner)
print(t)

cat = ProgramRunner('cat')
r = random_fuzzer.run(cat)
print(r)
```

## 0x02 A Simple Fuzzer

```Python
import random

def fuzzer(max_length: int = 100, char_start: int = 32, char_range: int = 32) -> str:
    """A string up to 'max_length' characters
       in the range ['char_start', 'char_start' + 'char_range')"""
    string_length = random.randrange(0, max_length + 1)
    out = ""
    for i in range(0, string_length):
        out += chr(random.randrange(char_start, char_start + char_range))
    return out

print(fuzzer())
print(fuzzer(1000, ord('a'), 26))
```

## 0x03 Fuzzing External Programs

```Python
import os
import tempfile

basename = "input.txt"
tempdir = tempfile.mkdtemp()
FILE = os.path.join(tempdir, basename)
print(FILE)

data = fuzzer()
with open(FILE, "w") as f:
    f.write(data)
contents = open(FILE).read()
print(contents)
assert(contents == data)
```

```Python
import subprocess

# v1: 1 input
program = "bc"
with open(FILE, "w") as f:
    f.write("2 + 2\n")
result = subprocess.run([program, FILE],
                        stdin=subprocess.DEVNULL,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True)

print(result.stdout)
print(result.returncode)
print(result.stderr)

####################

# v2: 100 inputs
trials = 100
program = "bc"

runs = []

for i in range(trials):
    data = fuzzer()
    with open(FILE, "w") as f:
        f.write(data)
    result = subprocess.run([program, FILE],
                            stdin=subprocess.DEVNULL,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            universal_newlines=True)
    runs.append((data, result))

s = sum(1 for (data, result) in runs if result.stderr == "")
print(s)

errors = [(data, result) for (data, result) in runs if result.stderr != ""]
(first_data, first_result) = errors[0]

print(repr(first_data))
print(first_result.stderr)

[result.stderr for (data, result) in runs if
 result.stderr != ""
 and "illegal character" not in result.stderr
 and "parse error" not in result.stderr
 and "syntax error" not in result.stderr]

print(result.stderr)

print(runs)
s = sum(1 for (data, result) in runs if result.returncode != 0)
print(s)
```

## 0x04 Different Bugs

```Python
from fuzzingbook.ExpectError import ExpectError

def crash_if_too_long(s):
    buffer = "Thursday"
    if len(s) > len(buffer):
        raise ValueError

trails = 100
with ExpectError():
    for i in range(trails):
        s = fuzzer()
        print(s)
        crash_if_too_long(s)

############################

def hang_if_no_space(s):
    i = 0
    while True:
        if i < len(s):
            if s[i] == '':
                break
        i += 1

from fuzzingbook.ExpectError import ExpectTimeout

trials = 100
with ExpectTimeout(2):
    for i in range(trials):
        s = fuzzer()
        hang_if_no_space(s)

###########################

def collapse_if_too_large(s):
    if int(s) > 1000:
        raise ValueError

long_number = fuzzer(100, ord('0'), 10)
print(long_number)

with ExpectError():
    collapse_if_too_large(long_number)
```

```C
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv) {
    /* Create an array with 100 bytes, initialized with 42 */
    char *buf = malloc(100);
    memset(buf, 42, 100);

    /* Read the N-th element, with N being the first command-line argument */
    int index = atoi(argv[1]);
    char val = buf[index];

    /* Clean up memory so we don't leak */
    free(buf);
    return val;
}

// clang -fsanitize=address -g -o program program.c

// ./program 99; echo $?
// ./program 110
```

```Python
######################################

secrets = ("<space for reply>" + fuzzer(100) +
           "<secret-certificate>" + fuzzer(100) +
           "secret-key" + fuzzer(100) + "<other-secrets>")

uninitialized_memory_marker = "deadbeef"
while len(secrets) < 2048:
    secrets += uninitialized_memory_marker
print(secrets)

def heartbeat(reply: str, length: int, memory: str) -> str:
    # Store reply in memory
    memory = reply + memory[len(reply):]

    # Send back heartbeat
    s = ""
    for i in range(length):
        s += memory[i]
    return s

cc = heartbeat("potato", 6, memory=secrets)
print(cc)
cc = heartbeat("bird", 4, memory=secrets)
print(cc)
cc = heartbeat("hat", 500, memory=secrets)
print(cc)

#########

from fuzzingbook.ExpectError import ExpectError

with ExpectError():
    for i in range(10):
        s = heartbeat(fuzzer(), random.randint(1, 500), memory=secrets)
        assert not s.find(uninitialized_memory_marker)
        assert not s.find("secret")
```

## 0x05 Program-Specific Checkers

```Python
airport_codes: Dict[str, str] = {
    "YVR": "Vancouver",
    "JFK": "New York-JFK",
    "CDG": "Paris-Charles de Gaulle",
    "CAI": "Cairo",
    "LED": "St. Petersburg",
    "PEK": "Beijing",
    "HND": "Tokyo-Haneda",
    "AKL": "Auckland"
}

print(airport_codes["YVR"])
print("AKL" in airport_codes)

# v1: 1 test case
def code_repOK(code: str) -> bool:
    assert len(code) == 3, "Airport code must have 3 characters: " + repr(code)
    for c in code:
        assert c.isalpha(), "Non-letter in airport code: " + repr(code)
        assert c.isupper(), "Lowercase letter in airport code: " + repr(code)
    return True

assert code_repOK("SEA")

# v2: test all elements in Dict[]
def airport_codes_repOK():
    for code in airport_codes:
        assert code_repOK(code)
    return True

with ExpectError():
    assert airport_codes_repOK()

# v3: add an invalid element
airport_codes["YMML"] = "Melbourne"

with ExpectError():
    assert airport_codes_repOK()

# v4: check before adding
def add_new_airport(code: str, city: str) -> None:
    assert code_repOK(code)
    airport_codes[code] = city

with ExpectError():
    assert airport_codes_repOK()
    add_new_airport("BER", "Berlin")
    add_new_airport("London-Heathrow", "LHR")

typed_airport_codes: Dict[str, str] = {
    "YVR": "Vancouver"
}
typed_airport_codes[1] = "First"
```

## 0x06 One More Example

```Python
cat = ProgramRunner(program="cat")
rr = cat.run("hello")
print(rr)

random_fuzzer = RandomFuzzer(min_length=20, max_length=20)
for i in range(10):
    print(random_fuzzer.fuzz())

for i in range(10):
    inp = random_fuzzer.fuzz()
    result, outcome = cat.run(inp)
    assert result.stdout == inp
    assert outcome == Runner.PASS

print(random_fuzzer.run(cat))
print(random_fuzzer.runs(cat, 10))
```
