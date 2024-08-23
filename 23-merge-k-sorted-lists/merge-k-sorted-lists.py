# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        def merge(list1, list2):
            node = ListNode()
            dummy = node
            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    node = node.next
                    list1 = list1.next
                else:
                    node.next = list2
                    node = node.next
                    list2 = list2.next
            if list1:
                node.next = list1
            if list2:
                node.next = list2
            return dummy.next
        while len(lists) != 1:
            newList = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i+1 not in range(len(lists)):
                    list2 = None
                else:
                    list2 = lists[i+1]
                newList.append(merge(list1, list2))
            lists = newList
        return lists[0]


        