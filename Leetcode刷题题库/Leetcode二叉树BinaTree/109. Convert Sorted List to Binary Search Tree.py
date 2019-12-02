# 给定一个单链列表，其中元素按升序排序，请将其转换为高度平衡的BST。
# 对于此问题，将高度平衡的二叉树定义为一个二叉树，其中每个节点的两个子树的深度相差不超过1。
# 例：
# 给定排序的链表：[-10，-3,0,5,9]，
# 一个可能的答案是：[0，-3,9，-10，null，5]，它表示以下高度平衡的BST：
#       0
#      / \
#    -3   9
#    /  /
#  -10  5
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:  # 边界条件链表的头节点为空，是一个空的二叉树
            return None
        if head.next is None:  # 边界条件
            return TreeNode(head.val)  # 返回链表的头节点即是二叉树的根节点

        prev = None  # 定义一个虚拟节点
        slow = head  # 定义一个慢指针指向头节点
        fast = head.next  # 定义一个快指针指向下一个节点

        while fast and fast.next:  # 当头节点后的两个节点都有值时，一直执行循环
            prev = slow  # 三个指针一次向后移动一位
            slow = slow.next
            fast = fast.next.next

        if prev:  # 如果prev虚节点一直存在,则循环直到终点prev.next是空
            prev.next = None
        else:
            head = None

        node = TreeNode(slow.val)  # 根节点
        node.left = self.sortedListToBST(head)  # 递归place左子树
        node.right = self.sortedListToBST(slow.next)  # 递归place右子树

        return node  # 循环结束返回根节点
