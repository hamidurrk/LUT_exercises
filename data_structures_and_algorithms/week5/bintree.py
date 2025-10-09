from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    key: int
    left: Optional[Node] = None
    right: Optional[Node] = None


class BST:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, key: int) -> None:
        if not isinstance(key, int):
            raise TypeError("BST only supports integer keys")

        def _insert(node: Optional[Node], key: int) -> Node:
            if node is None:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node

        self.root = _insert(self.root, key)

    def search(self, key: int) -> bool:
        node = self.root
        while node is not None:
            if key == node.key:
                return True
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def remove(self, key: int) -> None:
        def _remove(node: Optional[Node], key: int) -> Optional[Node]:
            if node is None:
                return None
            if key < node.key:
                node.left = _remove(node.left, key)
            elif key > node.key:
                node.right = _remove(node.right, key)
            else:  
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left

                max_node = node.left
                while max_node.right is not None:
                    max_node = max_node.right

                node.key = max_node.key
                node.left = _remove(node.left, max_node.key)
            return node

        self.root = _remove(self.root, key)

    def preorder(self) -> None:

        def _preorder(node: Optional[Node]) -> None:
            if node is None:
                return
            print(node.key, end=" ")
            _preorder(node.left)
            _preorder(node.right)

        _preorder(self.root)
        if self.root is not None:
            print()

    def postorder(self) -> None:

        def _postorder(node: Optional[Node]) -> None:
            if node is None:
                return
            _postorder(node.left)
            _postorder(node.right)
            print(node.key, end=" ")

        _postorder(self.root)
        if self.root is not None:
            print()

    def inorder(self) -> None:

        def _inorder(node: Optional[Node]) -> None:
            if node is None:
                return
            _inorder(node.left)
            print(node.key, end=" ")
            _inorder(node.right)

        _inorder(self.root)
        if self.root is not None:
            print()

    def breadthfirst(self) -> None:
        if self.root is None:
            return

        queue: deque[Node] = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.key, end=" ")
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        print()


if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)
   
    Tree.postorder()
    Tree.inorder()
    Tree.breadthfirst()