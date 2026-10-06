<img width="259" height="101" alt="image" src="https://github.com/user-attachments/assets/85f47684-bad1-42eb-b478-a9edecb2067e" />


> **Project of the Master in AI Development — Module “Python Programming”**  
> Student: Michele Assirelli


# Search Engine Query Correction Algorithm
A Python-based search query correction algorithm using Levenshtein distance to identify and correct typing errors in user queries.

# Search Engine Query Correction Algorithm

## Description

This project implements a simple **query correction algorithm** based on the **Levenshtein distance**.

The goal is to identify possible typing errors in user search queries and, when possible, replace incorrect words with the most similar words contained in a predefined dictionary.

## How It Works

The project mainly consists of two functions:

- `Levenshtein_distance(str_1, str_2)`: calculates the Levenshtein distance between two strings, considering insertions, deletions, and substitutions.
- `suggest_correction(query, dictionary)`: analyzes each word in the query, calculates its distance from the words in the dictionary, and suggests a corrected query when a sufficiently close match is found.

### Correction Rules

The algorithm handles three different cases:

1. **Correct query**  
   If all words have a Levenshtein distance of 0, the query is considered correct.

2. **Word too distant**  
   If at least one word has a distance greater than 2, the query cannot be automatically corrected.

3. **Query correction**  
   If the incorrect words have a distance between 1 and 2, they are replaced with the closest words found in the dictionary.

## Dictionary

The dictionary contains words related to the context of a **company search engine**, together with commonly used:

- conjunctions
- articles
- prepositions

Examples of included terms are `ricerca`, `motore`, `documenti`, `repository`, `database`, `software`, `azienda`, and `produttività`.

## Examples

The project includes several test queries containing typing errors, such as:

```text
motor ricerca aziendale
motoree ricerca aziendale
motore ricerac aziendale
motore ricerca azlendale
ricerca documeti aziendale
```

The algorithm compares each word with the dictionary and, when possible, suggests a corrected version of the query.

## Requirements

- Python 3.x
- No external libraries required

## Usage

Run the Python script:

```bash
python "Un algoritmo di correzione per un motore di ricerca (1).py"
```

The queries defined in `query_list` are automatically processed and the results are printed to the terminal.

## Project Structure

```text
.
├── Un algoritmo di correzione per un motore di ricerca (1).py
└── README.md
```

## Technologies

- Python
- Levenshtein Distance
- String Matching
- Text Query Processing
