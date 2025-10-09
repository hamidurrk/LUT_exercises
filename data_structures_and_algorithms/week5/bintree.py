from __future__ import annotations

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


if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()

    print(Tree.search(6))
    print(Tree.search(8))

    Tree.remove(1)
    Tree.preorder()
    Tree.remove(9)
    Tree.preorder()
    Tree.remove(3)
    Tree.preorder()