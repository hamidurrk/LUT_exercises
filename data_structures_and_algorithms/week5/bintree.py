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
        self._mirrored: bool = False

    def _compare(self, key: int, node_key: int) -> int:
        if key == node_key:
            return 0
        if self._mirrored:
            return -1 if key > node_key else 1
        return -1 if key < node_key else 1

    def _find_max(self, node: Node) -> Node:
        current = node
        while True:
            next_node = current.left if self._mirrored else current.right
            if next_node is None:
                return current
            current = next_node

    def _find_min(self, node: Node) -> Node:
        current = node
        while True:
            next_node = current.right if self._mirrored else current.left
            if next_node is None:
                return current
            current = next_node

    def insert(self, key: int) -> None:
        if not isinstance(key, int):
            raise TypeError("BST only supports integer keys")

        def _insert(node: Optional[Node], key: int) -> Node:
            if node is None:
                return Node(key)
            cmp = self._compare(key, node.key)
            if cmp < 0:
                node.left = _insert(node.left, key)
            elif cmp > 0:
                node.right = _insert(node.right, key)
            return node

        self.root = _insert(self.root, key)

    def search(self, key: int) -> bool:
        node = self.root
        while node is not None:
            cmp = self._compare(key, node.key)
            if cmp == 0:
                return True
            node = node.left if cmp < 0 else node.right
        return False

    def remove(self, key: int) -> None:
        def _remove(node: Optional[Node], key: int) -> Optional[Node]:
            if node is None:
                return None
            cmp = self._compare(key, node.key)
            if cmp < 0:
                node.left = _remove(node.left, key)
            elif cmp > 0:
                node.right = _remove(node.right, key)
            else:  
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left

                if not self._mirrored:
                    replacement = self._find_max(node.left)
                    node.key = replacement.key
                    node.left = _remove(node.left, replacement.key)
                else:
                    replacement = self._find_max(node.right)
                    node.key = replacement.key
                    node.right = _remove(node.right, replacement.key)
            return node

        self.root = _remove(self.root, key)

    def mirror(self) -> None:
        def _mirror(node: Optional[Node]) -> None:
            if node is None:
                return
            node.left, node.right = node.right, node.left
            _mirror(node.left)
            _mirror(node.right)

        _mirror(self.root)
        self._mirrored = not self._mirrored

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

    Tree.preorder()
    Tree.mirror()
    Tree.preorder()

    Tree.insert(8)
    Tree.remove(3)
    print(Tree.search(2))
    Tree.preorder()
    Tree.mirror()
    Tree.preorder()