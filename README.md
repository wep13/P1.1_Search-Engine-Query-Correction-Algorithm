<img width="259" height="101" alt="image" src="https://github.com/user-attachments/assets/85f47684-bad1-42eb-b478-a9edecb2067e" />


> **Project of the Master in AI Development — Module “Python Programming”**  
> Student: Michele Assirelli


# Search Engine Query Correction Algorithm

A Python implementation of a query correction algorithm for a search engine.

The project uses **Levenshtein distance** to identify and correct misspelled words in user search queries by comparing them with a predefined dictionary of relevant words.

## How It Works

The algorithm works in three main steps:

1. The input query is split into individual words.
2. The Levenshtein distance between each word and every word in the dictionary is calculated.
3. Based on the minimum distance:
   - If all words are correct, the query is accepted.
   - If a word is too distant from the dictionary, the query cannot be corrected.
   - Otherwise, incorrect words are replaced with the closest words in the dictionary.

A maximum Levenshtein distance of **2** is currently allowed for automatic correction.

## Levenshtein Distance

The Levenshtein distance measures the minimum number of:

- Insertions
- Deletions
- Substitutions

required to transform one string into another.

The algorithm is implemented from scratch using a matrix, without external libraries.

## Dictionary

The dictionary contains words related to the scope of **Searchify**, together with commonly used Italian:

- Articles
- Prepositions
- Conjunctions

This allows the algorithm to work with queries related to company search, documents, information retrieval, software, and business processes.

## Example

Input:

```text
motore ricerac aziendale
```

Suggested correction:

```text
motore ricerca aziendale
```

Another example:

```text
motor ricerca aziendale
```

is corrected to:

```text
motore ricerca aziendale
```

## Limitations

The current implementation has some limitations:

- When multiple dictionary words have the same minimum Levenshtein distance, the first one found in the dictionary is selected.
- The correction is based only on Levenshtein distance and does not currently consider the context of the other words in the query.
- The dictionary is manually defined and limited to the project's specific domain.

## Technologies

- Python
- Levenshtein Distance
- Lists and matrices
- String processing

## Project Purpose

The project was developed to demonstrate how a simple search engine can detect spelling errors in user queries and suggest corrected versions without relying on external spelling-correction libraries.
