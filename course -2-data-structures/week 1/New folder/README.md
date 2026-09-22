# Python — Average spam confidence from a file

## Exercise 7.2

Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

```
X-DSPAM-Confidence:    0.8475
```

Count these lines and extract the floating point values from each of the lines and compute the average of those values, producing an output as shown below. Do not use the `sum()` function or a variable named `sum` in your solution.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt — when testing, enter `mbox-short.txt` as the file name.

## The code

```python
fname = input("Enter file name: ")
fh = open(fname)

count = 0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(":")
    val = float(line[pos + 1:])
    total = total + val
    count = count + 1

if count > 0:
    print("Average spam confidence:", total / count)
```

⚠️ **Typo fixed:** the last line originally had `if coun > 0:` — missing a `t`. Python would raise `NameError: name 'coun' is not defined` since `coun` was never declared. It must be `count`.

## What the code does

Reads a file line by line, finds every line starting with `X-DSPAM-Confidence:`, extracts the number after the colon, and calculates the **average** of all those numbers.

## Line-by-line explanation

| Line | Explanation |
|---|---|
| `fname = input("Enter file name: ")` | Asks the user to type a file name |
| `fh = open(fname)` | Opens the file, returns a file handle (`fh`) |
| `count = 0` | Counter for how many matching lines were found |
| `total = 0.0` | Running sum of the confidence values (float, so division gives decimals) |
| `for line in fh:` | Loops through the file, one line at a time |
| `if not line.startswith("X-DSPAM-Confidence:"): continue` | Skips any line that doesn't start with this exact text |
| `pos = line.find(":")` | Finds the position of the `:` character in the line |
| `val = float(line[pos + 1:])` | Takes everything **after** the `:`, converts it to a decimal number |
| `total = total + val` | Adds this value to the running total |
| `count = count + 1` | Increments the counter |
| `if count > 0:` | Avoids dividing by zero if no matching line was found |
| `print("Average spam confidence:", total / count)` | Prints the average |

## Example

If the file contains:
```
X-DSPAM-Confidence: 0.8475
X-DSPAM-Confidence: 0.6178
X-DSPAM-Confidence: 0.6961
```

The code:
- Finds 3 matching lines → `count = 3`
- Sums the values → `total = 0.8475 + 0.6178 + 0.6961 = 2.1614`
- Prints: `Average spam confidence: 0.7204666666666667`

## Key concepts used

| Concept | Role |
|---|---|
| `startswith()` | Checks if a string begins with a given text |
| `find()` | Returns the position (index) of a character in a string |
| String slicing `[pos+1:]` | Extracts a substring from a position to the end |
| `float()` | Converts text into a decimal number |
| `continue` | Skips the rest of the loop body and moves to the next line |
