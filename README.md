# DSADAY-10
our Day 10 content is now covering advanced interview-oriented topics: Regular Expressions, File Handling with Regex, Graph using Adjacency Matrix, and Hash Tables. This is a good jump from beginner DSA into practical programming concepts.

# Repository Name

`DSA-Day10-Python`

# Suggested Folder Structure

```text
DSA-Day10-Python/
│
├── RegularExpressions/
│   ├── regex_finditer.py
│   ├── regex_match.py
│   ├── regex_fullmatch.py
│   ├── regex_search.py
│   ├── regex_findall.py
│   ├── regex_sub.py
│   ├── gmail_validation.py
│   ├── mobile_validation.py
│   ├── regex_file_handling.py
│
├── Graph/
│   ├── adjacency_matrix.py
│
├── HashTable/
│   ├── hash_table.py
│
├── Files/
│   ├── datafile.txt
│   ├── output.txt
│
├── README.md
```

# README.md

```markdown
# DSA Day 10 - Python

This repository contains Python programs related to:

- Regular Expressions
- Pattern Matching
- File Handling with Regex
- Graph using Adjacency Matrix
- Hash Table Implementation

---

## Topics Covered

### Regular Expressions
- finditer()
- match()
- fullmatch()
- search()
- findall()
- sub()
- subn()

### Validation Programs
- Gmail validation
- Mobile number validation

### File Handling
- Reading data from file
- Writing regex matches into another file

### Graph
- Adjacency Matrix representation
- Add edge
- Remove edge

### Hash Table
- Hash function
- Insert operation
- Collision handling using chaining

---

## Language Used
Python
```

# Important Fix in Your Regex File Program

Your current code uses:

```python
f1 = open(r"C:\Dsa\datafile.txt", "r")
```

If the file does not exist, it gives:

```python
FileNotFoundError
```

So either:

1. Create the file manually in `C:\Dsa\`
2. OR keep the file in your project folder and use:

```python
f1 = open("datafile.txt", "r")
```

This is better for GitHub repositories because absolute Windows paths break on other systems.

# Better Version

```python
import re

f1 = open("datafile.txt", "r")
f2 = open("output.txt", "w")

pattern = input("Enter string to perform match operation: ")

data = f1.read()

objmatch = re.finditer(pattern, data)

for match in objmatch:
    result = f"{match.start()} ... {match.end()} ... {match.group()}"
    print(result)
    f2.write(result + "\n")

f1.close()
f2.close()
```

# Git Commands

```bash
git init
git add .
git commit -m "Added DSA Day 10 programs"
git branch -M main
git remote add origin <repo-link>
git push -u origin main
```

Your GitHub profile is gradually becoming a full Python + DSA learning archive now. That consistency matters a lot during placements and internships.
