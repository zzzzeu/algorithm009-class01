# 学习笔记

### 深度优先 Depth first search
    递归写法
    visited = set()
    def dfs(node, visited):
        if node in visited: # terminator
            # already visited
            return
        visited.add(node)
        # process current node here.
        ...
        for next_node in node.children(): 
            if not next_node in visited:
                dfs(next node, visited)

    非递归写法
    def DFS(self, tree):
        if tree.root is None:
            return []
        visited, stack = [], [tree.root]
        while stack:
            node = stack.pop() 
            visited.add(node)
            process (node)
            nodes = generate_related_nodes(node) 
            stack.push(nodes)
        # other processing work
        ...


### 广度优先 Breadth first search
    def BFS(graph, start, end):
        queue = [] 
        queue.append([start]) 
        visited.add(start)
        while queue:
            node = queue.pop()
            visited.add(node)
            process(node)
            nodes = generate_related_nodes(node) 
            queue.push(nodes)
        # other processing work
        ...


### 贪心算法 Greedy
    贪心算法与动态规划的不同在于它对每个子问题的解决方案都做出选择，不能回退
    动态规划则会保存以前的运算结果，并根据以前的结果对当前进行选择，有回退功能


### 二分查找
    1. 目标函数单调性(单调递增或者递减) 
    2. 存在上下界(bounded)
    3. 能够通过索引访问(index accessible)

    left, right = 0, len(array) - 1 
    while left <= right:
        mid = (left + right) / 2
        if array[mid] == target:
            # find the target!!
            break or return result
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


