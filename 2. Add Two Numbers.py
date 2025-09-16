class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def list_to_listnode(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next



def addTwoNumbers(l1, l2):
    num1, num2, result = "", "", []
    
    while l1:
        num1 = str(l1.val) + num1
        l1 = l1.next
    while l2:
        num2 = str(l2.val) + num2
        l2 = l2.next

    soma = str(int(num1) + int(num2))
    for i in soma:
        result.insert(0, int(i))
    
    return list_to_listnode(result)



l1 =[2,4,3]
l2 = [5,6,4]

l1 = list_to_listnode(l1)
l2 = list_to_listnode(l2)
print(type(l1))

a = addTwoNumbers(l1, l2)
print(a)