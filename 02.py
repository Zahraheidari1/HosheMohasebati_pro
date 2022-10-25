from audioop import cross
import random
import numpy as np
from copy import deepcopy
"""""
def Crossover(parent1,parent2,point):
    p1,p2 = list(parent1),list(parent2) #convert str to list
    cx=[]
    j=0
    for i in range(point,len(p1)):
        cx[j]=p1[i]
        cx[j+1]=p2[i]
        i=p2[i]
        j=j+1
    return cx
parent1 = '9821745063'        #parents' Chromosomes
parent2 = '1234567890'
print('Parent1:',parent1)
print('Parent2:',parent2)
point = random.randint(1,len(parent1))  #Crossover point
print('Crossover Point:',point)
offspring1,offspring2 = Crossover(parent1,parent2,point)
print('Offspring1:',offspring1)         #Offspring Chromosomes
print('Offspring2:',offspring2)
"""
def cx(pc):
  p1 =  np.array([9,8,2,1,7,4,5,0,6,3])
  p2=   np.array([1,2,3,4,5,6,7,8,9,0]) 
  c1=np.array([-1]*len(p1))  
  if np.random.random() < pc:  # if pc is greater than random number
        p1_copy = p1
        p2_copy = p2
        swap = True
        count = 0
        pos = 0   

        while True:
            if count>len(p1): break
            for i in range(len(p1)):
                if c1[i]==-1:
                    pos=i
                    break

            if swap==True:
                while True:
                    c1[pos] = p1[pos]
                    count+=1
                    pos = p2.index(p1[pos])
                    #pos = p2+p1[pos]    
                    if p1_copy[pos] == -1:
                        swap = False
                        break
                    p1_copy[pos] = -1
            elif swap==False:
                while True:
                    c1[pos] = p2[pos]
                    count+=1
                    pos = p1.index(p2[pos])
                    if p2_copy[pos] == -1:
                        swap = True
                        break
                    p2_copy[pos] = -1
"""""
cross=cx(1)
for i in range(len(cross)):
      (cross[i])
      """