# Closest Binary Search Tree Value II

LeetCode 272

## Problem Statement

Given the root of a binary search tree, a target value, and an integer `k`, return the `k` values in the BST that are closest to the target.

The returned values can be in any order.

## Solution

This solution first performs an inorder traversal of the binary search tree and stores all the node values in a list.

The values are then sorted based on their absolute difference from the target value. Finally, the first `k` values from the sorted list are returned.

## Example

### Input

```text
root = [4,2,5,1,3]
target = 3.714286
k = 2
```

### Output

```text
[4,3]
```

### Explanation

The values closest to `3.714286` are `4` and `3`.

Their differences from the target are:

```text
|4 - 3.714286| = 0.285714
|3 - 3.714286| = 0.714286
```

Therefore, the output is:

```text
[4,3]
```

## Approach

1. Traverse the BST using inorder traversal.
2. Store every node value in a list.
3. Sort the values according to their distance from the target.
4. Select the first `k` values.
5. Return those values as the answer.

## Algorithm

1. Create an empty list called `values`.
2. Perform an inorder traversal of the BST.
3. Add each node value to `values`.
4. Sort `values` using `abs(value - target)` as the sorting key.
5. Return the first `k` elements from the sorted list.

## Complexity

* Time Complexity: O(n log n)
* Space Complexity: O(n)

## Author

T. Nandhini
