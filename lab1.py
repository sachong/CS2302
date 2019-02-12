import numpy as np
import math
import matplotlib.pyplot as plt
"""
@author Samuel Chong
Lab 1
"""

def draw_squares(ax,n,coord,r):
    if n>0:
        #the function for p is to draw the complete square, if one coordinate
        #is missing then the square is incomplete or it draws a triangle
        p = np.array(((coord[0] - r,coord[1] - r),(coord[0] + r,coord[1] - r),
                    (coord[0] + r,coord[1] + r), (coord[0] - r,coord[1] + r),
                    (coord[0] - r,coord[1] - r)))
        ax.plot(p[:,0],p[:,1],color='k')
        #this recursion call creates the bottom left square
        draw_squares(ax,n-1,(coord[0] - r,coord[1] - r), r/2)
        #this recursion call creates the bottom right square
        draw_squares(ax,n-1,(coord[0] + r,coord[1] - r), r/2)
        #this recursion call creates the top left square
        draw_squares(ax,n-1,(coord[0] - r,coord[1] + r), r/2)
        #this recursion call creates the top right square
        draw_squares(ax,n-1,(coord[0] + r,coord[1] + r), r/2)
        
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        #in order for the circle to be moved to the left you need to 
        #add radius to x
        ax.plot(x+radius,y,color='k')
        draw_circles(ax,n-1,center,radius*w,w)
        
        
def draw_tree(ax,n,orig,x,y):
    if n>0:
        #to draw a line to the left then we must subtract x to our original 'x'
        #coordinate and subtract y to out  original 'y' in order for the line
        #to go down or else it would be a straight line
        ax.plot((orig[0],orig[0]-x), (orig[1],orig[1]-y),color='k')
        #same applies for the right line but in this case you need to add x
        #so the line inclines the other way
        ax.plot((orig[0],orig[0]+x), (orig[1],orig[1]-y),color='k')
        #call the method twice so there is two children per level
        #divide x by 2 so when adding or subtracting x to coordinate it moves 
        #left and right equally, subtract 1 to y so it goes down one level
        draw_tree(ax,n-1,((orig[0]-x,orig[1]-y)), x/2, y-1)
        draw_tree(ax,n-1,((orig[0]+x,orig[1]-y)), x/2, y-1)
       
def draw_in_circles(ax,n,center,rad):
    if n>0:
        
        #creates the original circle
        x,y = circle(center,rad)
        ax.plot(x,y,color='k')
        
        #creates center circle
        x,y = circle((center[0],center[1]),rad/3)
        ax.plot(x,y,color='k')
        draw_in_circles(ax,n-1,(center[0],center[1]),rad/3) 
        
        #creates the left circle
        x,y = circle((center[0]-(rad/3)*2,center[1]),rad/3)
        ax.plot(x,y,color='k')
        draw_in_circles(ax,n-1,(center[0]-(rad/3)*2,center[1]),rad/3)
        
        #creates the right circle
        x,y = circle((center[0]+(rad/3)*2,center[1]),rad/3)
        ax.plot(x,y,color='k')
        draw_in_circles(ax,n-1,(center[0]+(rad/3)*2,center[1]),rad/3)
        
        #creates bottom circle
        x,y = circle((center[0],center[1]-(rad/3)*2),rad/3)
        ax.plot(x,y,color='k')
        draw_in_circles(ax,n-1,(center[0],center[1]-(rad/3)*2),rad/3)
        
        #creates top circle
        x,y = circle((center[0],center[1]+(rad/3)*2),rad/3)
        ax.plot(x,y,color='k')
        draw_in_circles(ax,n-1,(center[0],center[1]+(rad/3)*2),rad/3)
        
        
plt.close("all") 
fig, ax = plt.subplots()


#coordinates for the original square
coord = [800,800] 
#1a uses only 2 so it only creates 2 squares
#draw_squares(ax,2,coord,200)

#1b uses only 3 so it only creates 3 squares
#draw_squares(ax,3,coord,200)

#1c uses only 4 so it only creates 4 squares
#draw_squares(ax,4,coord,200)


#2a calls the method 5 times but the circle keeps getting smaller because
#the radius is been multiplied by 'w'
#draw_circles(ax, 10, [100,0], 100,.5)
 
#2b calls the method 45 times
#draw_circles(ax, 45, [100,0], 100,.9)

#2c calls the method 100 times
#draw_circles(ax, 100, [100,0], 100,.95)


#initial point for binary tree
origin = [0,0]
#3a calls the method 3 times so there are 3 levels
#draw_tree(ax,3,origin,5,5)

#3b calls the method 4 times so there are 4 levels
#draw_tree(ax,4,origin,5,5)

#3c#3a calls the method 7 times so there are 7 levels
#draw_tree(ax,10,origin,8,8) 


#4a calls the method 2 times 
#draw_in_circles(ax, 2, [100,0], 100)

#4b calls the method 3 times
draw_in_circles(ax, 3, [100,0], 100)

#4c calls the method times
#draw_in_circles(ax, 4, [100,0], 100)

ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('lab1.png')   



