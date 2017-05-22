# -*- coding: utf-8 -*-
"""
Created on Wed May 17 23:57:00 2017

@author: user
"""

import pygame
import numpy as np


CoeffD = 0.4    #coeff affecting the tendency to stay in direction 0.4
CoeffC = 0.002   #coeff affecting the tendency to move towards centre of mass 0.002
CoeffS = 0.8   #coeff affecting how much the birds move away from each other 0.8
n = 3     #number of birds
T = 100                          #fps
r0 = 70        #seperation distance
r1 = 100
white = (255,255,255)   #colour
wallx = 800     #size of the pygame surface
wally = 600     #size of the pygame surface
maxspeed = 10

boids1 = np.array([5.+wallx/2., 5.+wally/2., 20., 20.])  #[x,y,vx,vy]
boids2 = np.array([-5.+wallx/2., 0.+wally/2, 10., -20.])
boids3 = np.array([1.+wallx/2., -4.+wally/2, -20., -20.])
arrayx = np.random.uniform(low=10, high = wallx - 10, size=(n))
arrayy = np.random.uniform(low=10, high = wally - 10, size=(n))
arrayvx = np.random.uniform(low=10, high = maxspeed, size=(n))
arrayvy = np.random.uniform(low=10, high = maxspeed, size=(n))
arrx = arrayx.reshape((n,1))
arry = arrayy.reshape((n,1))
arrvx = arrayvy.reshape((n,1))
arrvy = arrayvy.reshape((n,1))
array = np.hstack([arrx,arry,arrvy,arrvy])
print array


ball = pygame.image.load('ball.png')



def boids(array):
    for k in range(0,n,1):
        x1 = array[k,0:1]
        y1 = array[k,1:2]
        cx = 0
        cy = 0
        vx = array[k, 2:3]
        vy = array[k, 3:4]
        if array[k,0:1] > wallx:
            vx = array[k, 2:3]
            x = array[k, 0:1] - wallx
        
        elif array[k, 0:1] < 0:
            vx = array[k, 2:3]
            x = wallx + array[k, 0:1]
            
        if array[k,1:2] > wally:
            vy = array[k,3:4]
            y = array[k, 1:2] - wally
        
        elif array[k, 1:2] < 0:
            vy = array[k, 3:4]
            y = array[k, 1:2] + wally
                
                
            
        for i in range(0,n,1):
                r = np.sqrt((array[k,0:1]-array[i,0:1])**2 + (array[k,1:2]-array[i,1:2])**2) 
                if r0 < r < r1 and i != k:
                    vx1 = 0
                    vy1 = 0
                    x1 = 0
                    y1 = 0
                    
                    
                    x1 += array[i,0:1]
                    y1 += array[i,1:2]
                    vx1 += array[i,2:3]
                    vy1 +=array[i,3:4]
                    vx = array[k,2:3] + CoeffD*(vx1 - array[k,2:3]) 
                    vy = array[k,3:4] + CoeffD*(vy1 - array[k,3:4]) 
                elif 0 < r < r0 and i != k:
                    mag = np.sqrt((array[k,0:1] - array[i,0:1])**2 + (array[k,1:2] - array[i,1:2])**2 )
                    cx += CoeffS*(array[k,0:1] - array[i,0:1])/mag
                    cy += CoeffS*(array[k,1:2] - array[i,1:2])/mag
                    vx = array[i,2:3]
                    vy = array[i,3:4]
        
        
        x = array[k,0:1] + vx + CoeffC*(x1 - array[k,0:1]) + cx
        y = array[k,1:2] + vy + CoeffC*(y1 - array[k,1:2]) + cy
        
        array[k,0:1] = x
        array[k,1:2] = y
        array[k,2:3] = vx
        array[k,3:4] = vy
        gameDisplay.blit(ball,(x,y))

pygame.init() #starting. it's necessary
gameDisplay = pygame.display.set_mode((wallx,wally)) #game size.
pygame.display.set_caption('Boids') #title
clock = pygame.time.Clock()   #internal clock... this is how it measures time

crashed = False #when something bad happened it becomes true

while not crashed:
    
    for event in pygame.event.get():   #event is something observed by the game
        if event.type == pygame.QUIT:  #ifsomeone closes the tab, its event == pygame.QUIT
            crashed = True #this gets out of the loop of "WHilte not crashed"
        
        
    gameDisplay.fill(white)
    boids(array)

    
    pygame.display.update() #this will show pictures per sec if you decide something
    
    clock.tick(T) #60 frames per sec( NOT THE SAME AS FPS...well kinda the same)
    
pygame.quit() #when you close the tab
quit() #you initialized, now you end

