# SQL Query Performance Analysis

## Overview

This README provides an analysis of three different SQL scripts that involve creating tables with random data and performing joins. The scripts are categorized based on the presence or absence of indexes, which significantly affects query performance.

## SQL Script Variations

1. **random.sql**: Creates tables `TEST1`, `TEST2`, and `TEST3` filled with random values. Joins are performed without any indexes, making them relatively slower.
2. **random_cover_indexed.sql**: Similar to `random.sql`, but adds covering indexes to `TEST2` and `TEST3`, thereby enhancing the query's efficiency.
3. **random_indexed.sql**: Similar to the first two, but the indexes created are not covering indexes.

## Pseudo-Code for Fast Query

Assuming that the fast query is implemented in `random_cover_indexed.sql`, the following pseudo-code describes its working mechanism:

```pseudo
1. Load Index idx_test2_x into memory
2. Load Index idx_test3_yz into memory

3. For each row R1 in TEST1:
    3.1 Find matching rows in TEST2 using idx_test2_x where R1.x == R2.x
        3.1.1 For each matching row R2 in TEST2:
            3.1.1.1 Find matching rows in TEST3 using idx_test3_yz where R1.y == R3.y AND R3.z > R1.z
            3.1.1.2 Count the matches
```

## Asymptotic Scaling Behavior

For Fast Query
If N represents the number of rows in each table:

Reading from TEST1 is O(N)
Searching in TEST2 is O(logN) per row due to indexing.
Searching in TEST3 is O(logN) per row due to indexing.
The overall time complexity for the fast query would be O(NlogN).

For Creating an Index
The time complexity for creating an index is usually
O(NlogN), as it involves sorting the key.

Conclusion
Indexes play a pivotal role in optimizing SQL queries. They can significantly reduce the time complexity, especially in scenarios involving joins over large datasets.
