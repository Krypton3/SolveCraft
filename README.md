# SolveCraft
Competitive Programming / Skill Checker

This is a repository that holds different competitive problem-solving using Python and C++, which can be useful for the developer interview process. This repository contains problems ranging from easy to hard. 

Important Factors in Programming:

# Time Complexity
Time complexity refers to the amount of time an algorithm takes to run as a function of the size of its input. It gives an upper bound on the time needed to solve a problem as the input size grows.

Big-O Notation: Time complexity is often expressed using Big-O notation, which describes the worst-case scenario (the longest time the algorithm could take). Common time complexities include:

- O(1): Constant time – the algorithm takes the same amount of time regardless of the input size.
- O(log n): Logarithmic time – the time increases logarithmically as the input size increases.
- O(n): Linear time – the time increases linearly with the input size.
- O(n log n): Linearithmic time – common in efficient sorting algorithms like merge sort.
- O(n^2): Quadratic time – the time increases quadratically, often seen in nested loops.
- O(2^n): Exponential time – time doubles with each additional input, often seen in recursive algorithms.
- O(n!): Factorial time – time increases factorially, often associated with problems involving permutations.

Example:
1. Linear Search: Searching for an item in an unsorted list has a time complexity of O(n), because in the worst case, the algorithm might have to check every element.
2. Binary Search: Searching in a sorted list has a time complexity of O(log n), as the search space is halved with each step.

# Space Complexity
Space complexity refers to the amount of memory an algorithm uses as a function of the size of its input. It considers both the space needed to hold the input data and the additional space required during computation (e.g., for variables, call stacks, and data structures).

Big-O Notation: Like time complexity, space complexity is also expressed using Big-O notation.

- O(1): Constant space – the algorithm uses a fixed amount of memory regardless of input size.
- O(n): Linear space – the memory usage grows linearly with the input size.
- O(n^2): Quadratic space – memory usage grows quadratically with the input size, often seen in algorithms using a 2D array.

Example:
1. In-place Sorting: An algorithm like quicksort, which sorts the data in place, has a space complexity of O(1) because it doesn't use extra memory for storing data.
2. Merge Sort: An algorithm like merge sort has a space complexity of O(n) because it requires extra space for temporary arrays during the merge process.

# Summary
1. Time Complexity: Measures how the runtime of an algorithm scales with input size.
2. Space Complexity: Measures how the memory usage of an algorithm scales with input size.
3. Big-O Notation: A mathematical notation used to express both time and space complexity, focusing on the worst-case scenario.