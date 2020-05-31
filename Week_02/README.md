# 学习笔记

### 哈希表 Hash Table
    是根据关键码值(Key value)而直接进行访问的数据结构
    通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度

    1.Search: O(1)/O(n)

    2.Insertion: O(1)/O(n)

    3.Delete: O(1)/O(n)

### 二叉树 Binary Tree
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left, self.right = None, None

    前序遍历(Pre-order)
        def preorder(self, root):
            if root: 
                self.traverse_path.append(root.val) 
                self.preorder(root.left) 
                self.preorder(root.right)

    中序遍历(In-order)
        def inorder(self, root):
            if root:
                self.inorder(root.left) 
                self.traverse_path.append(root.val) 
                self.inorder(root.right)

    后序遍历(Post-order)
        def postorder(self, root):
            if root:
                self.postorder(root.left) 
                self.postorder(root.right) 
                self.traverse_path.append(root.val)

###  二叉搜索树 Binary Search Tree
    1.查询Search: O(log(n))/O(n)

    2.插入新节点Insertion: O(log(n))/O(n) 

    3.删除Delete: O(log(n))/O(n)

### 堆 Heap
    1.find-max: O(1)

    2.delete-max: O(log(n))

    3.insert(create): O(log(n))/O(1)


### 二叉堆  Binary Heap
    是一颗二叉完全树且树中任意节点的值总是>=其子节点的值

    根节点(顶堆元素): a[0]

    1.索引为i的左孩子的索引: (2 * i + 1)

    2.索引为i的右孩子的索引: (2 * i + 2)

    3.索引为i的父节点的索引: floor((i - 1) / 2)

    Insert
        新元素一律插到尾部, 依次向上调整结构
    
    Delete Max
        将堆尾元素替换到顶部, 依次向下调整结构

