# 📊 Data Analyzer and Transformer Program

## 📌 Project Overview

The **Data Analyzer and Transformer Program** is a menu-driven Python program designed to perform different operations on a dataset entered by the user.

This project is created for **learning and practical purposes**. It demonstrates important Python concepts such as:

* Lists
* `if-elif-else`
* `while` loop
* Built-in functions
* Recursion
* Lambda functions
* `filter()`
* `sorted()`
* User-defined functions
* Returning multiple values
* Multiple assignment
* User input and type conversion

---

## 🎯 Objectives

The main objectives of this project are:

1. To accept numerical data from the user.
2. To store the data in a Python list.
3. To display basic information about the dataset.
4. To calculate the factorial of a number using recursion.
5. To filter data using a lambda function.
6. To sort data in ascending or descending order.
7. To calculate basic statistical values.
8. To understand menu-driven programming in Python.

---

## 🛠️ Technologies Used

| Technology         | Purpose                 |
| ------------------ | ----------------------- |
| Python             | Programming Language    |
| List               | Store dataset           |
| `while` Loop       | Display menu repeatedly |
| `if-elif-else`     | Handle menu choices     |
| Built-in Functions | Data analysis           |
| Recursion          | Factorial calculation   |
| Lambda             | Data filtering          |
| `filter()`         | Filter dataset          |
| `sorted()`         | Sort dataset            |
| Functions          | Perform calculations    |

---

# 📋 Main Menu

When the program starts, the following menu is displayed:

```text
Welcome to the Data Analyzer and Transformer Program

Main Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data
5. Sort Data
6. Display Statistics
7. Exit Program
```

---

# 🔹 Features

## 1️⃣ Input Data

The user can enter multiple numbers separated by spaces.

### Example:

```text
Enter data separated by spaces: 10 20 30 40 50
```

The input is converted into integers and stored inside a list.

### Code:

```python
values = input("Enter data separated by spaces: ")
data = list(map(int, values.split()))
```

### Concepts Used:

* `input()`
* `split()`
* `map()`
* `int()`
* `list()`

---

## 2️⃣ Display Data Summary

This option displays basic information about the entered dataset.

It shows:

* Total number of elements
* Minimum value
* Maximum value
* Sum
* Average

### Example:

```text
Data Summary:
Total elements: 5
Minimum value: 10
Maximum value: 50
Sum: 150
Average: 30.0
```

### Built-in Functions Used:

```python
len(data)
min(data)
max(data)
sum(data)
```

Average is calculated using:

```python
sum(data) / len(data)
```

---

## 3️⃣ Calculate Factorial

This option calculates the factorial of a number using **recursion**.

### Example:

```text
Enter a number: 5
Factorial: 120
```

### Factorial Logic:

```text
5! = 5 × 4 × 3 × 2 × 1
   = 120
```

### Function:

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

### Concept Used:

**Recursion** means a function calls itself.

---

## 4️⃣ Filter Data

This option filters the dataset according to a threshold value.

Only values **greater than or equal to** the threshold are displayed.

### Example:

```text
Data:
10 20 30 40 50

Enter threshold: 30

Filtered Data: [30, 40, 50]
```

### Code:

```python
result = list(filter(lambda x: x >= number, data))
```

### Concepts Used:

* Lambda function
* `filter()`
* List
* Comparison operator

---

## 5️⃣ Sort Data

This option sorts the dataset in two ways:

```text
1. Ascending
2. Descending
```

### Ascending Example:

```text
Original Data: 50 20 40 10 30

Sorted Data: [10, 20, 30, 40, 50]
```

### Descending Example:

```text
Sorted Data: [50, 40, 30, 20, 10]
```

### Code:

Ascending:

```python
sorted(data)
```

Descending:

```python
sorted(data, reverse=True)
```

---

## 6️⃣ Display Statistics

This option calculates and displays:

* Minimum
* Maximum
* Sum
* Average

A user-defined function is used to calculate and return multiple values.

### Function:

```python
def statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return minimum, maximum, total, average
```

The returned values are stored using multiple assignment:

```python
a, b, c, d = statistics(data)
```

### Example:

```text
Dataset Statistics:
Minimum: 10
Maximum: 50
Sum: 150
Average: 30.0
```

---

# 🔄 Program Flow

```text
Start
  ↓
Display Main Menu
  ↓
Enter Choice
  ↓
 ┌─────────────────────────────┐
 │ 1. Input Data               │
 │ 2. Display Data Summary     │
 │ 3. Calculate Factorial      │
 │ 4. Filter Data              │
 │ 5. Sort Data                │
 │ 6. Display Statistics       │
 │ 7. Exit                     │
 └─────────────────────────────┘
  ↓
Perform Selected Operation
  ↓
Return to Main Menu
  ↓
Choice 7?
  ↓
Yes → Exit Program
```

---

# 🧠 Python Concepts Demonstrated

## 1. List

A list is used to store multiple values.

```python
data = []
```

Example:

```python
data = [10, 20, 30, 40, 50]
```

---

## 2. While Loop

The `while True` loop keeps the menu running until the user chooses Exit.

```python
while True:
    # menu
```

The program stops using:

```python
break
```

---

## 3. Conditional Statements

The program uses `if`, `elif`, and `else` to process different choices.

```python
if choice == "1":
    ...
elif choice == "2":
    ...
else:
    ...
```

---

## 4. Built-in Functions

The program uses several Python built-in functions:

```text
len()   → Number of elements
min()   → Minimum value
max()   → Maximum value
sum()   → Total of values
sorted() → Sort values
```

---

## 5. Recursion

The factorial function calls itself.

```python
return n * factorial(n - 1)
```

This is an example of **recursive programming**.

---

## 6. Lambda Function

A lambda function is a small anonymous function.

```python
lambda x: x >= number
```

It is used with `filter()` to filter the dataset.

---

## 7. User-Defined Function

The program creates its own functions.

Example:

```python
def factorial(n):
```

and:

```python
def statistics(numbers):
```

---

## 8. Return Multiple Values

The `statistics()` function returns four values:

```python
return minimum, maximum, total, average
```

These values are received using:

```python
a, b, c, d = statistics(data)
```

---

# ▶️ How to Run the Program

### Step 1: Install Python

Make sure Python is installed on your computer.

Check Python version:

```bash
python --version
```

---

### Step 2: Create Python File

Create a file named:

```text
data_analyzer.py
```

---

### Step 3: Add the Code

Copy the complete Python program into the file.

---

### Step 4: Run the Program

Open Terminal / Command Prompt in the project folder and type:

```bash
python data_analyzer.py
```

---

# 💻 Sample Output

```text
Welcome to the Data Analyzer and Transformer Program

Main Menu:
1. Input Data
2. Display Data Summary
3. Calculate Factorial
4. Filter Data
5. Sort Data
6. Display Statistics
7. Exit Program

Please enter your choice: 1

Enter data separated by spaces: 10 20 30 40 50

Data has been stored successfully!
```

### Data Summary:

```text
Please enter your choice: 2

Data Summary:
Total elements: 5
Minimum value: 10
Maximum value: 50
Sum: 150
Average: 30.0
```

### Factorial:

```text
Please enter your choice: 3

Enter a number: 5
Factorial: 120
```

### Filter:

```text
Please enter your choice: 4

Enter threshold: 30
Filtered Data: [30, 40, 50]
```

### Sorting:

```text
Please enter your choice: 5

1. Ascending
2. Descending

Enter choice: 1
Sorted Data: [10, 20, 30, 40, 50]
```

### Statistics:

```text
Please enter your choice: 6

Dataset Statistics:
Minimum: 10
Maximum: 50
Sum: 150
Average: 30.0
```

### Exit:

```text
Please enter your choice: 7

Thank you! Goodbye!
```

---

# 📚 Learning Outcomes

After completing this project, the learner can understand:

* How to create a menu-driven Python program.
* How to work with lists.
* How to take multiple values from the user.
* How to use Python built-in functions.
* How recursion works.
* How lambda functions work.
* How `filter()` works.
* How to sort data.
* How to create user-defined functions.
* How to return multiple values from a function.
* How to use loops and conditional statements.

---

# ⚠️ Important Notes

* The program expects **integer values** when entering dataset values.
* Data should be entered using spaces.

Correct:

```text
10 20 30 40 50
```

Incorrect:

```text
10,20,30,40,50
```

* Data must be entered before using options **2, 4, 5, and 6**.
* Factorial is intended for non-negative integers.

---

# 📁 Project Structure

```text
Data-Analyzer-and-Transformer/
│
├── data_analyzer.py
│
└── README.md
```

---

# 👩‍💻 Author

**Sneha Padsala**

### Purpose

This project is created for **Python learning, practice, and academic purposes**.

---

# ⭐ Conclusion

The **Data Analyzer and Transformer Program** is a beginner-friendly Python project that combines multiple programming concepts into one practical application.

It provides a simple way to practice **data handling, functions, recursion, lambda functions, filtering, sorting, loops, and conditional statements** in Python.
