
**Python code:**
```python
class Solution:
    def closestKValues(self, root, target, k):
        values = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        values.sort(key=lambda x: abs(x - target))

        return values[:k]
