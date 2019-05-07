
"""
@author: Samuel Chong
MW 10:30-11:50
Olac Fuentes
TAs: Anindita Nath and Maliheh Zargaran
The purpose for this lab was to print the adjacency 
list from a graph, print the path by using breadth-first
search, depth-first search and depth-first recursively, 
and print the maze.
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import time
import queue

def printPath(prev, v):
    if prev[v] != -1: #repeat until prev[v] is -1
        printPath(prev, prev[v])
        print("-", end=' ')
        print(v, end=' ')
        

def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def find_c(S,i): #Find with path compression 
    if S[i]<0: 
        return i
    r = find_c(S,S[i]) 
    S[i] = r 
    return r

def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1  

def numSets(S): #return the number of sets
    count = 0
    for i in S:
        if i < 0: #if it is -1 then it is a root so add 1
            count += 1
    return count

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j)
    if ri!=rj:
        S[rj] = ri
        return True
    return False

def union_c(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj:
        S[rj] = ri
        return True
    return False

def unionSize(S,i,j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S,i) 
    rj = find_c(S,j)
    if ri!=rj: #if different root
        if S[ri] > S[rj]: #if ri is bigger than rj then rj goes to ri
            S[rj] += S[ri]
            S[ri] = rj
            return True
        else:
            S[ri] += S[rj] #if rj is bigger than ri then ri goes to rj
            S[rj] = ri
            return True
    return False



def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)



def AdjList(rows,cols,walls):
    G = completeList(rows,cols)
    for i in walls:
        G[i[0]].remove(i[1]) #remove at that position
        G[i[1]].remove(i[0])
    return G

def completeList(rows,cols):
    G =[[]for i in range(rows * cols)] #size of the full maze
    for i in range(cols):
        for j in range(cols):
            temp = j + (i * cols)
            if i is not 0: 
                G[temp].append(temp - cols) #append to the bottom
            if j is not (cols - 1): 
                G[temp].append(temp + 1) #append to the right side
            if temp % cols is not 0:
                G[temp].append(temp - 1) #append to the left side
            if i is not rows - 1:
                G[temp].append(temp + cols)#append to the upper side
    return G


def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w

    
def cases(maze, remWalls):
    if maze < remWalls -1:
        print("A path from source to destination is not guaranteed to exist")
    elif maze == remWalls-1:
        print("The is a unique path from source to destination")
    elif maze > remWalls -1:
        print("There is at least one path from source to destination")
    

def BFS(G, v):
    visited = [False for i in range(len(G))]#make everything False
    prev = [-1 for i in range(len(G))] #all set to -1
    Q = queue.Queue()
    Q.put(v) #enqueue
    visited[v] = True #if index v was visited then True
    while not Q.empty(): #while it has something
        u = Q.get() #dequeue
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                Q.put(t)
    return prev

    
def DFS(G,s):
    global visited_DFS
    global prev_DFS
    visited_DFS[s] = True
    for t in G[s]:
        if not visited_DFS[t]:
            visited_DFS[t] = True
            prev_DFS[t] = s
            DFS(G,t)
        
def DFSstack(G,v):
    visited = [False for i in range(len(G))]#make everything False
    prev = [-1 for i in range(len(G))] #all set to -1
    S = [] #create stack
    S.append(v)
    visited[v] = True #when visited make it True
    while len(S) is not 0: #while it is not empty
        u = S.pop()
        for t in G[u]:
            if not visited[t]: 
                visited[t] = True
                prev[t] = u
                S.append(t) #push
    return prev


    

    
plt.close("all") 
maze_rows = 10
maze_cols = 10
maze = maze_rows * maze_cols

print("The number of cells in the maze is: ", maze_rows * maze_cols)
remWalls = int(input("How many walls do you want to remove?"))
print()

walls = wall_list(maze_rows,maze_cols)
draw_maze(walls,maze_rows,maze_cols,cell_nums=True) 
newS = DisjointSetForest(maze_rows * maze_cols)

cases(maze_rows*maze_cols, remWalls)
print()
while numSets(newS) > 1:
     d = random.randint(0,len(walls)-1) #chooses a random integer
     if union(newS, walls[d][0], walls[d][1]) is not False: #if they are part of two different sets
         walls.pop(d) 

G = AdjList(maze_rows, maze_cols, walls)


visited_DFS = [False for i in range(len(G))]
prev_DFS = [-1 for i in range(len(G))]
print("Adjacency List: ")
print(G)
#print(AdjList(walls, originalWalls, maze))
print()



print("Breadth-first search: ")
sg1 = time.time()
G1 = BFS(G,0)
printPath(G1, len(G1)-1)
eg1 = time.time()
print()
print("Running Time in seconds for BFS: ", eg1-sg1)

print()
print("DFS Stack: ")
sg2 = time.time()
G2 = DFSstack(G,0)
printPath(G2, len(G2)-1)
eg2 = time.time()
print()
print("Running Time in seconds for DFSstack: ", eg2-sg2)

print()
print("DFS recursion: ")
sg3 = time.time()
DFS(G,0)
printPath(prev_DFS,maze-1)
eg3 = time.time()
print()
print("Running Time in seconds for DFS: ", eg3-sg3)

draw_maze(walls,maze_rows,maze_cols) 
