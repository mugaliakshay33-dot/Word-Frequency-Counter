# Word Frequency Counter Using Python

## Project Description

The **Word Frequency Counter** is a simple Python application that analyzes text files and calculates how frequently each word appears.

The program reads a text file, counts the total number of words, identifies unique words, and displays the **10 most frequently used words**.

This project demonstrates fundamental Python concepts such as file handling, regular expressions, collections, and text processing.

## Features

* Reads and analyzes text files
* Counts total words
* Identifies unique words
* Displays the top 10 most frequent words
* Performs case-insensitive word counting
* Handles file errors
* Simple command-line interface
* No external libraries required

## Technologies Used

* **Programming Language:** Python 3
* **Libraries:**

  * `collections.Counter` – Counts word occurrences.
  * `pathlib` – Handles file paths.
  * `re` – Extracts words using regular expressions.

## Project Structure

```text
Word-Frequency-Counter/
│
├── word_frequency.py
├── sample.txt
└── README.md
```

## How to Run

**Step 1:** Install Python 3.

**Step 2:** Clone the GitHub repository.

```bash
git clone https://github.com/YOUR_USERNAME/Word-Frequency-Counter.git
```

**Step 3:** Navigate to the project directory.

```bash
cd Word-Frequency-Counter
```

**Step 4:** Run the Python program.

```bash
python word_frequency.py
```

**Step 5:** Enter the path of the text file you want to analyze.

```text
Enter Text File Path: sample.txt
```

## Sample Input

**File: sample.txt**

```text
Python is easy.
Python is powerful.
Python is popular.
```

## Sample Output

```text
===== WORD FREQUENCY COUNTER =====

Enter Text File Path: sample.txt

===== WORD FREQUENCY ANALYSIS =====

Total Words: 9
Unique Words: 5

Top 10 Most Frequent Words:

python: 3
is: 3
easy: 1
powerful: 1
popular: 1
```

## How It Works

1. The user enters the path of a text file.
2. The program checks whether the file exists.
3. The file content is read using UTF-8 encoding.
4. Regular expressions extract English words from the text.
5. All words are converted to lowercase for case-insensitive analysis.
6. The `Counter` class calculates word frequencies.
7. The program displays the total number of words and unique words.
8. The 10 most frequently occurring words are displayed.

## Python Concepts Used

* File Handling
* Functions
* Regular Expressions
* Python Collections
* Counter Class
* Lists
* Conditional Statements
* Exception Handling
* String Manipulation

## Future Enhancements

* Support multiple text files.
* Export word frequencies to CSV.
* Generate word frequency charts.
* Remove common stop words.
* Add support for multiple languages.
* Create a graphical interface using Tkinter.
* Generate word clouds.
* Analyze larger text datasets.

## Project Objective

The objective of this project is to develop a Python-based text analysis application that identifies word frequencies in text files while demonstrating fundamental programming and data-processing concepts.
