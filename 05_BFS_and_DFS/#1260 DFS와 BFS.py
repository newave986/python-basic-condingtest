# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:37:22 2021

@author: newave986.git
"""

from collections import deque

def DFS(x):
    
    global edg_info
    global visitDFS
    global stack
    
    print(x, end = ' ')
    visitDFS[x] = True
    
    for y in edg_info[x]:
        if visitDFS[y] == False:
            DFS(y)
    
                
def BFS(x):
    
    # edg_info를 전역 변수로 선언
    global edg_info
    global visitBFS
    
    # BFS를 구현하기 위해 queue 선언
    queue = deque()
    # queue에 초기값 x in
    queue.append(x)
    visitBFS[x] = True
    
    # BFS 구현
    while queue:
        q1 = queue.popleft()
        print(q1, end = ' ')
        for q2 in edg_info[q1]:
            if visitBFS[q2] == False:
                visitBFS[q2] = True
                queue.append(q2)
                

# n, m, v 함수를 사용자로부터 입력받는다.
n, m, v = map(int, input().split())
# 간선(edg) 정보를 저장할 리스트를 선언한다.
edg_info = list([] for _ in range(n + 11))
    
# 간선(edg) 정보를 입력받는다.
for k in range(m):
    a, b = map(int, input().split())
        
    edg_info[a].append(b)
    edg_info[b].append(a)
    
for k in range(n + 1):
    edg_info[k].sort()

stack = []
visitDFS = [False for _ in range(n + 1)]
DFS(v)

print()

visitBFS = [False for _ in range(n + 1)]
BFS(v)
