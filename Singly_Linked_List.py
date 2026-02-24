"""
Singly Linked List
A linear collection of nodes where each node points to the next.
Operations: insert at head, insert at tail, delete by value, search, traverse.
Time complexities:
    - Insert at head: O(1)
    - Insert at tail: O(n)
    - Delete by value: O(n)
    - Search: O(n)
Space: O(n)
"""

import unittest

class ListNode:
    """Node of a singly linked list."""
    def __init__(self, val: int = 0, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    """Singly linked list with head pointer."""

    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_head(self, val: int) -> None:
        """Insert new node at beginning."""
        new_node = ListNode(val, self.head)
        self.head = new_node
        self.size += 1

    def insert_at_tail(self, val: int) -> None:
        """Insert new node at end."""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def delete_by_value(self, val: int) -> bool:
        """Delete first occurrence of val. Return True if deleted."""
        if not self.head:
            return False
        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return True
        curr = self.head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                self.size -= 1
                return True
            curr = curr.next
        return False

    def search(self, val: int) -> bool:
        """Return True if val exists in list."""
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False

    def to_list(self) -> list:
        """Convert linked list to Python list for testing."""
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def __len__(self):
        return self.size

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_empty_list(self):
        self.assertEqual(len(self.ll), 0)
        self.assertFalse(self.ll.search(5))
        self.assertFalse(self.ll.delete_by_value(10))

    def test_insert_at_head(self):
        self.ll.insert_at_head(3)
        self.ll.insert_at_head(2)
        self.ll.insert_at_head(1)
        self.assertEqual(self.ll.to_list(), [1,2,3])
        self.assertEqual(len(self.ll), 3)

    def test_insert_at_tail(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.ll.insert_at_tail(3)
        self.assertEqual(self.ll.to_list(), [1,2,3])
        self.assertEqual(len(self.ll), 3)

    def test_mixed_inserts(self):
        self.ll.insert_at_head(2)
        self.ll.insert_at_tail(3)
        self.ll.insert_at_head(1)
        self.ll.insert_at_tail(4)
        self.assertEqual(self.ll.to_list(), [1,2,3,4])

    def test_delete_existing(self):
        self.ll.insert_at_tail(1)
        self.ll.insert_at_tail(2)
        self.ll.insert_at_tail(3)
        self.assertTrue(self.ll.delete_by_value(2))
        self.assertEqual(self.ll.to_list(), [1,3])
        self.assertEqual(len(self.ll), 2)
        # delete head
        self.assertTrue(self.ll.delete_by_value(1))
        self.assertEqual(self.ll.to_list(), [3])
        # delete tail
        self.assertTrue(self.ll.delete_by_value(3))
        self.assertEqual(self.ll.to_list(), [])
        self.assertEqual(len(self.ll), 0)

    def test_delete_non_existent(self):
        self.ll.insert_at_tail(1)
        self.assertFalse(self.ll.delete_by_value(2))
        self.assertEqual(self.ll.to_list(), [1])

    def test_search(self):
        self.ll.insert_at_tail(5)
        self.ll.insert_at_tail(10)
        self.assertTrue(self.ll.search(5))
        self.assertTrue(self.ll.search(10))
        self.assertFalse(self.ll.search(7))

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
    # Manual demo
    ll = LinkedList()
    ll.insert_at_head(10)
    ll.insert_at_tail(20)
    print("Linked list:", ll.to_list())