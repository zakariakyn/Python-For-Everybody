# Exercise 5.2 — Largest and Smallest Numbers

**Course:** Python for Everybody — Course 1 (Getting Started with Python), Week 5

## Problem

Write a program that repeatedly prompts a user for integer numbers until the user enters `done`. Once `done` is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number, catch it with a `try/except`, print an appropriate message, and ignore the number.

Enter `7`, `2`, `bob`, `10`, and `4` and match the output below.

## Expected Output

```
Invalid input
Maximum is 10
Minimum is 2
```

## Solution

```python

tab = []
cond = False

largest = None
smallest = None

while True :

    x = input("Enter a number (or 'done'): ")

    if x == 'done':
        break
    else :
        try :
            num = int(x)
            tab.append(num)
        except :
            print("Invalid input.")

largest = max(tab)
smallset = min(tab)

print("Maximum is", largest)
print("Minimum is", smallset)

```

## Sample Run

```
Enter a number: 7
Enter a number: 2
Enter a number: bob
Invalid input
Enter a number: 10
Enter a number: 4
Enter a number: done
Maximum is 10
Minimum is 2
```

## What I Learned

- Using a `while True` loop with `break` to stop on a sentinel value (`done`)
- Handling bad input with `try/except ValueError`
- Storing values in a list and using `max()` and `min()`
- Guarding against an empty list before calling `max()` / `min()`
