# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def merge_sort(self, begin, end):
        if begin.next is end:
            return begin
        
        pass

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.merge_sort(begin=head, end=None)