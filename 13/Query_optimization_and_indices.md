## 1. Pseudo-code for the case that there are no indexes:

1. Initialize an empty list called 'result'
2. For each row in the Customer table:
   2.1 If Gender == 'f' AND ZipCode == '90210':
   2.1.1 Add the Name and Phone of the row to 'result'
3. Return 'result'

## 2. Pseudo-code for the case that there is an index on Gender:

1. Initialize an empty list called 'result'
2. Use the Gender index to find rows where Gender == 'f'
3. For each row found in step 2:
   3.1 If ZipCode == '90210':
   3.1.1 Add the Name and Phone of the row to 'result'
4. Return 'result'

Efficiency: If the gender distribution is similar to the general population, roughly 50% of the customers would be female. So, you would only need to scan through about half of the Customer table. This would make it roughly twice as efficient as having no index.

## 3. Pseudo-code for the case that there is an index on ZipCode:

1. Initialize an empty list called 'result'
2. Use the ZipCode index to find rows where ZipCode == '90210'
3. For each row found in step 2:
   3.1 If Gender == 'f':
   3.1.1 Add the Name and Phone of the row to 'result'
4. Return 'result'

Efficiency: If there are 10,000 different zip codes, then the index would make this query roughly 10,000 times more efficient than having no index.

## 4. Composite Index:

A good composite index for this query would be on (ZipCode, Gender).

1. Initialize an empty list called 'result'
2. Use the composite index to find rows where ZipCode == '90210' AND Gender == 'f'
3. For each row found in step 2:
   3.1 Add the Name and Phone of the row to 'result'
4. Return 'result'

## 5. Covering Index:

A covering index for this query would include all the columns that the query needs: (ZipCode, Gender, Name, Phone).

1. Initialize an empty list called 'result'
2. Use the covering index to find rows where ZipCode == '90210' AND Gender == 'f'
3. For each row found in step 2:
   3.1 Add the Name and Phone of the row to 'result'
4. Return 'result'

Efficiency Comparison: A covering index is generally more efficient than a composite index for this specific query because it can return all the needed information directly from the index, avoiding the need to go back to the table for additional data. However, covering indexes can be less efficient in terms of storage and maintenance, especially if the table has many columns.
