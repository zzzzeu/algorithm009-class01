# 学习笔记

### Array时间复杂度
    prepend     O(1)
    append      O(1)
    lookup      O(1)
    insert      O(n)
    delete      O(n)

### Linkedlist时间复杂度
    prepend     O(1)
    append      O(1)
    lookup      O(n)
    insert      O(1)
    delete      O(1)


### Stack & Queue & Deque & Priority Queue
    Stack: First in - Last out, 添加删除时间复杂度为O(1)
    Queue: First in - First out, 添加删除时间复杂度为O(1)
    Deque: double ended queue, 插入删除时间复杂度为O(1)
    Priority Queue: 插入时间复杂度为O(1), 按元素优先级取出, 时间复杂度为O(logn), 底层具体实现的数据结构有heap、bst、treap