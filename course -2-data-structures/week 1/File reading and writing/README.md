# Parsing Logic Reference & Code Explanation

This document explains the mechanical structure, data flow, and error-handling requirements of the Python delimiter parser using safe, generic tokens.

---

## 1. Complete Source Code

```python
path = "results.txt"

with open("netflix.txt", "r", encoding="utf-8", errors="ignore") as file:
    with open(path, "w", encoding="utf-8") as result:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            line = line.split("|")

            if line[0]:
                line[0] = line[0].split(":")
                
            result.write(f"email : {line[0][0]} , password : {line[0][1]} , {line[3]}\n")
    print("Done !")
```

---

## 2. Input vs. Output Example

### Input File (`netflix.txt`)
```text
alexander.k@example.com:Str0ngP@ss2024 | Plan = Premium | Price = $19.99 | Country = US 🇺🇸 | MaxStreams = 4 | Quality = UHD
sarah_m99@demo.org:MySecretKey987 | Plan = Standard | Price = €13.49 | Country = DE 🇩🇪 | MaxStreams = 2 | Quality = FHD
david.tech@sample.net:D@v1dP@ssw0rd! | Plan = Basic | Price = £8.99 | Country = UK 🇬🇧 | MaxStreams = 1 | Quality = HD
```

### Result File (`results.txt`)
```text
email : alexander.k@example.com , password : Str0ngP@ss2024  ,  Country = US 🇺🇸 
email : sarah_m99@demo.org , password : MySecretKey987  ,  Country = DE 🇩🇪 
email : david.tech@sample.net , password : D@v1dP@ssw0rd!  ,  Country = UK 🇬🇧 
```

> **Note on spacing:** Notice that fields like `Country = US 🇺🇸` preserve leading and trailing spaces from around the pipe (`|`). To remove extra spaces around values, call `.strip()` on each item (e.g., `line[3].strip()`).

---

## 3. Line-by-Line Breakdown

### Step 1: Destination Setup
```python
path = "results.txt"
```
Defines the output file path where the extracted records will be written.

### Step 2: Safe File Opening
```python
with open("netflix.txt", "r", encoding="utf-8", errors="ignore") as file:
    with open(path, "w", encoding="utf-8") as result:
```
* `open("netflix.txt", "r", encoding="utf-8", errors="ignore")`: Opens the source file in read mode. Any corrupted bytes or character encoding mismatches are discarded without crashing via `errors="ignore"`.
* `open(path, "w", encoding="utf-8")`: Opens `results.txt` in write mode (`"w"`), creating a fresh file or overwriting previous content.
* Context managers (`with`) ensure both file handles close cleanly after processing.

### Step 3: Line Iteration and Sanitization
```python
for line in file:
    line = line.strip()
    if not line:
        continue
```
* Reads the file line by line without loading the entire file into RAM.
* `line = line.strip()` trims leading/trailing spaces and newline characters (`\n`).
* `if not line: continue` checks for empty or blank lines and skips them immediately.

### Step 4: Delimiter Splitting (`|`)
```python
line = line.split("|")
```
Splits the string on every pipe character (`|`), producing an indexed list of fields:

| Index | Generic Segment | Example Representation |
| :--- | :--- | :--- |
| `line[0]` | First column | `alexander.k@example.com:Str0ngP@ss2024 ` |
| `line[1]` | Second column | ` Plan = Premium ` |
| `line[2]` | Third column | ` Price = $19.99 ` |
| `line[3]` | Fourth column | ` Country = US 🇺🇸 ` |
| `line[n]` | Successive columns | Remaining metadata attributes |

### Step 5: Sub-splitting the First Field (`:`)
```python
if line[0]:
    line[0] = line[0].split(":")
```
* Takes `line[0]` and divides it at the colon (`:`).
* Converts `line[0]` into a nested list:
  * `line[0][0]`: The identifier / email (`alexander.k@example.com`).
  * `line[0][1]`: The secret / password (`Str0ngP@ss2024 `).

### Step 6: Formatted File Write
```python
result.write(f"email : {line[0][0]} , password : {line[0][1]} , {line[3]}\n")
```
* Injects `line[0][0]`, `line[0][1]`, and `line[3]` into a single formatted string.
* Adds a newline character (`\n`) to ensure each record is written on a separate line.


