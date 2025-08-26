# Vector-Search-Engine

A simple Python-based search engine that uses vector embeddings and Euclidean distance to find the closest matches to a query. Demonstrates fundamental AI/ML concepts such as vectorization and nearest neighbor search.

# How to Modify

Modifying this script is simple. To add new "searches" or "vectors," locate the VECTORS variable, which contains the names and their corresponding vector points.

Vector points define the position of each item:

x value: Represents the "class" or category.
Example: Both 'dog' and 'cat' have x = 1 because they belong to the same class (animals).

y value: Represents closeness or similarity within the class.
Example: 'dog' might have y = 2 and 'cat' y = 2.2 because they are similar but not identical.

Example: Adding another animal like 'mouse' → x = 1 and y slightly larger than 'dog' (e.g., y = 2.4).
Adding a new category like 'car' → x = 2 (incremented from animals), and y starts at 2; each car can increment y by 0.1–0.9 depending on similarity.

# Limits

The script only works with items already in the database.

New words not in VECTORS cannot be automatically recognized.

Vector positions are precise, but the word database is fixed.

# How It Works

Database: Each word has a vector position.

Input: User provides a vector or a word (converted into a vector).

Distance Calculation: The script measures the Euclidean distance between the input vector and every vector in the database.

Ranking: Distances are sorted from closest to furthest.

Final Results: The closest vector positions are converted back to words and returned as a finalized list.
