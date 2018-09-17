# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
      self.val = x
      self.next = None

class Solution(object):
  
  
    
  def addTwoNumbers(self, l1, l2):
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_sum = self.get_sum(l1)
        second_sum = self.get_sum(l2)
        total = first_sum + second_sum
        root = ListNode(0)
        dummy_front = root
        sum =0
        
        while total >=10:
            last_digit = sum %((sum/10) *10)
            dummy_front.next = ListNode(last_digit)
            sum = sum/10
            dummy_front = dummy_front.next
        dummy_front.next =ListNode(sum)
        return root.next
    
  def get_sum(self, listNode):
        sum =0
        pos =1
        listNode = listNode.next
        while listNode:
            sum +=pos*listNode.val
            pos *= 10
        return sum


    
    
