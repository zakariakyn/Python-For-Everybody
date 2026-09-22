# Python File Handling - PY4E Exercise 7.1

Comprehensive guide, source code, test data, and conceptual breakdown for reading and manipulating text files in Python.

---

## 1. Problem Statement

Write a program that:
1. Prompts the user for a file name.
2. Safely opens the file (handling invalid inputs or missing files gracefully).
3. Reads through the file line by line.
4. Strips redundant whitespace and trailing newlines.
5. Converts all textual characters to uppercase.
6. Prints each processed line to standard output.

---

## 2. Source Code (`solution.py`)

```python
# Prompt user for the filename
fname = input("Enter file name: ")

# Safely attempt to open the file
try:
    fh = open(fname, "r")
except FileNotFoundError:
    print(f"Error: File '{fname}' cannot be opened.")
    quit()

# Process each line sequentially
for line in fh:
    # rstrip() removes the trailing '\n' to prevent double spacing
    cleaned_line = line.rstrip().upper()
    print(cleaned_line)

# Release system resources
fh.close()
```

---

## 3. Input Data (`words.txt`)

```text
Writing programs or programming is a very creative
and rewarding activity  You can write programs for
many reasons ranging from making your living to solving
a difficult data analysis problem to having fun to helping
someone else solve a problem  This book assumes that
{\em everyone} needs to know how to program and that once
you know how to program, you will figure out what you want
to do with your newfound skills

We are surrounded in our daily lives with computers ranging
from laptops to cell phones  We can think of these computers
as our personal assistants who can take care of many things
on our behalf  The hardware in our current-day computers
is essentially built to continuously ask us the question
What would you like me to do next

Our computers are fast and have vasts amounts of memory and 
could be very helpful to us if we only knew the language to 
speak to explain to the computer what we would like it to 
do next If we knew this language we could tell the 
computer to do tasks on our behalf that were reptitive  
Interestingly, the kinds of things computers can do best
are often the kinds of things that we humans find boring
and mind-numbing and result
```

---

## 4. Execution Output

### Console Input
```text
Enter file name: words.txt
```

### Console Output
```text
WRITING PROGRAMS OR PROGRAMMING IS A VERY CREATIVE
AND REWARDING ACTIVITY  YOU CAN WRITE PROGRAMS FOR
MANY REASONS RANGING FROM MAKING YOUR LIVING TO SOLVING
A DIFFICULT DATA ANALYSIS PROBLEM TO HAVING FUN TO HELPING
SOMEONE ELSE SOLVE A PROBLEM  THIS BOOK ASSUMES THAT
{\EM EVERYONE} NEEDS TO KNOW HOW TO PROGRAM AND THAT ONCE
YOU KNOW HOW TO PROGRAM, YOU WILL FIGURE OUT WHAT YOU WANT
TO DO WITH YOUR NEWFOUND SKILLS

WE ARE SURROUNDED IN OUR DAILY LIVES WITH COMPUTERS RANGING
FROM LAPTOPS TO CELL PHONES  WE CAN THINK OF THESE COMPUTERS
AS OUR PERSONAL ASSISTANTS WHO CAN TAKE CARE OF MANY THINGS
ON OUR BEHALF  THE HARDWARE IN OUR CURRENT-DAY COMPUTERS
IS ESSENTIALLY BUILT TO CONTINUOUSLY ASK US THE QUESTION
WHAT WOULD YOU LIKE ME TO DO NEXT

OUR COMPUTERS ARE FAST AND HAVE VASTS AMOUNTS OF MEMORY AND
COULD BE VERY HELPFUL TO US IF WE ONLY KNEW THE LANGUAGE TO
SPEAK TO EXPLAIN TO THE COMPUTER WHAT WE WOULD LIKE IT TO
DO NEXT IF WE KNEW THIS LANGUAGE WE COULD TELL THE
COMPUTER TO DO TASKS ON OUR BEHALF THAT WERE REPTITIVE
INTERESTINGLY, THE KINDS OF THINGS COMPUTERS CAN DO BEST
ARE OFTEN THE KINDS OF THINGS THAT WE HUMANS FIND BORING
AND MIND-NUMBING AND RESULT
```

---

## 5. File Concepts & Mechanics

### What is a File?
A file is a sequence of bytes stored permanently on non-volatile secondary storage (SSD, HDD). Unlike variables stored in primary memory (RAM), files remain intact when program execution finishes or power is lost.

### The File Handle (`open()`)
```python
fh = open(fname, "r")
```
* `open()` does **not** load the file's entire content into memory immediately.
* It returns a **file handle** (a stream cursor/pointer) provided by the operating system.
* The `"r"` parameter sets the access mode to read-only.

### Line-by-Line Iteration
```python
for line in fh:
```
* Python iterates through the file handle lazily as a generator.
* It reads exactly one line at a time from storage into RAM, keeping memory usage constant ($O(1)$) regardless of whether the file size is 10 KB or 10 GB.

### Newline Characters and `rstrip()`
* In text files, line breaks are represented by the invisible control character `\n` (ASCII 10).
* When reading lines, `line` ends with `\n`.
* Because `print()` appends its own newline by default, calling `print(line)` outputs an unwanted empty line between each line.
* Calling `rstrip()` strips this invisible `\n` (and any trailing spaces) from the right-hand edge before printing.

### Error Handling (`try ... except`)
* File access operations depend on external operating system states.
* If a specified filename does not exist, Python raises `FileNotFoundError`.
* Wrapping `open()` in a `try ... except` block prevents traceback crashes and provides a clean exit via `quit()`.