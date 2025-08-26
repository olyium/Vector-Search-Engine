# Vector-Search-Engine
A simple Python-based search engine that uses vector embeddings and Euclidean distance to find the closest matches to a query. Demonstrates fundamental AI/ML concepts such as vectorization and nearest neighbor search.

# How you can modify it?

Modifying this script is simple. To add new "searches" or "vectors," locate the VECTORS variable, which contains the names and their corresponding vector points.

Vector points define the position of each item:

The x value represents the "class" or category. For example, both 'dog' and 'cat' have x = 1 because they belong to the same class (animals).

The y value represents closeness or similarity within the class. For example, 'dog' might have y = 2 and 'cat' y = 2.2 because they are similar but not identical.

If you add another animal, like 'mouse', it would also have x = 1 and a y slightly larger than 'dog' (e.g., y = 2.4) to reflect its relative closeness.
