Day 2 – Python String Basics (Notes)
🔹 1. What is a String?

A string in Python is a sequence of characters enclosed within quotes.

name = "Siva"
language = 'Python'

✔ Key points:

Strings are immutable

Strings support indexing, slicing, and multiple built-in methods

🔹 2. String Indexing

Example:

s = "Python"


Indexes:

 P   y   t   h   o   n
 0   1   2   3   4   5


Negative Indexing:

 P    y    t    h    o    n
-6   -5   -4   -3   -2   -1


Examples:

s[0]   # P
s[-1]  # n

🔹 3. String Slicing

Syntax:

string[start : end : step]


Examples:

s = "DataScience"

s[0:4]     # Data
s[2:8]     # taScie
s[2:8:2]   # tSc


✔ End index is not included.

🔹 4. Useful String Methods
Case Methods
text.upper()      # HELLO
text.lower()      # hello
text.title()      # Hello World

Strip Spaces
text.strip()

Replace Text
text.replace("old", "new")

Find Substring
text.find("th")   # returns position or -1

Split String
"Data Science".split()
# ['Data', 'Science']

Join Strings
"-".join(["Data", "Science"])
# Data-Science

🔹 5. Concatenation & Repetition
Concatenation:
"Data" + "Science"   # DataScience

Repetition:
"AI" * 3    # AIAIAI

🔹 6. Membership Operator

Check if substring exists:

"a" in "Data"        # True
"Sci" in "Science"   # True
