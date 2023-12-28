l = int(input())
for i in range(l):
    home = 'Home'
    current = home
    graph = {current : []}

    n = int(input())
    for j in range(n):
        s = input()
        if (s not in graph):
            graph[current].append(s)
            graph[s] = []
        
        current = s

    deepest = 0

    def dfs(start, depth):
        depth += 1
        global deepest 

        if (depth > deepest):
            deepest = depth
    
        for s in graph[start]:
            dfs(s, depth)

    dfs(home, -1)
    print((n - deepest * 2) * 10)
