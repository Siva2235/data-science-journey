🚀 Day 2 – Python String Basics

Mastering string operations is an essential step in Data Science, NLP, and data cleaning.
Today’s tasks focused on understanding Python strings through indexing, slicing, methods, and basic transformations.

📘 Topics Covered

What is a String?

Indexing & Negative Indexing

Slicing (start, end, step)

Common String Methods

String Concatenation & Repetition

Membership Operators

Real-world text processing tasks

🔤 1. String Basics
Creating Strings
text1 = "Hello"
text2 = 'Python'

Indexing Example
s = "Python"
s[0]    # P
s[-1]   # n

Slicing Example
s = "DataScience"
s[0:4]      # Data
s[2:8:2]    # tSc

🛠️ 2. Useful String Methods
Case Conversion
text.upper()
text.lower()
text.title()

Strip Extra Spaces
text.strip()

Replace Words
text.replace("bad", "good")

Split & Join
text.split()                   # ['Data', 'Science']
"-".join(["Data", "Science"])  # Data-Science
