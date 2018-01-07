import random
import time
import os
import psutil
import scipy.stats
import threading
import pylab

import numpy as np

from matplotlib import pyplot as plt
from matplotlib import animation

global count
global compareCount
global timer
global peakMemory

global datastatus


count = 0
compareCount = 0
timer = 0

def insertSort(data):
    
    global count
    global compareCount
    global peakMemory
    global datastatus
    
    global timer
    global datastatus
    
    plt.bar(height=datastatus,left=range(1,51))
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.savefig("insertsortimage/img" + '%04d' % timer + ".png")
    plt.clf()
    timer += 1
    
    p1 = psutil.Process(os.getpid())
    
    for i in range(1,len(data)):
        
        compareCount += 1
        if data[i-1] >= data[i]:
             
            temp = data[i]
            j = i
                        
            while (j > 0 and data[j-1] > temp):
                compareCount+=1
                
                data[j] = data[j-1]
                j = j-1
                #if peakMemory < p1.memory_percent():
                    #peakMemory = p1.memory_percent()
               
            
            compareCount+=1    
            data[j] = temp
            count = count + 1
            plt.bar(height=datastatus,left=range(1,51))
            plt.xlabel('Index')
            plt.ylabel('Value')
            plt.savefig("insertsortimage/img" + '%04d' % timer + ".png")
            timer += 1
            plt.clf()
                       
                 
             
        
    
    return

def selectSort(data):
    global count
    global compareCount
    global peakMemory
    
    global timer
    global datasatus
    
    plt.bar(height=datastatus,left=range(1,51))
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.savefig("selectsortimage/img" + '%04d' % timer + ".png")
    plt.clf()
    timer += 1
    
    p1 = psutil.Process(os.getpid())
    
    for i in range(0,len(data)):
        
        min = data[i]
        min_index = i
        j = i
        while (j < len(data)):
            compareCount += 1
            if data[j] < min:
                min = data[j]
                min_index = j
            j += 1
            
        if min_index != i:
            
            temp = data[i]
            data[i] = data[min_index]
            data[min_index] = temp
            count = count + 1
            
            plt.bar(height=datastatus,left=range(1,51))
            plt.xlabel('Index')
            plt.ylabel('Value')
            plt.savefig("selectsortimage/img" + '%04d' % timer + ".png")
            plt.clf()
            timer += 1
            #if peakMemory < p1.memory_percent():
                #peakMemory = p1.memory_percent()
    

    return

def bubbleSort(data):
    global count
    global compareCount
    global peakMemory
    
    global timer
    global datastatus
    
    plt.bar(height=datastatus,left=range(1,51))
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.savefig("bubblesortimage/img" + '%04d' % timer + ".png")
    plt.clf()
    timer += 1
    
    
    p1 = psutil.Process(os.getpid())
    
    for i in range(0,len(data)):
        
        j = i
        while (j < len(data)):
            compareCount += 1
            if(data[i]>data[j]):
                
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
                count = count + 1
                
                plt.bar(height=datastatus,left=range(1,51))
                plt.xlabel('Index')
                plt.ylabel('Value')
                plt.savefig("bubblesortimage/img" + '%04d' % timer + ".png")
                plt.clf()
                timer += 1
                #if peakMemory < p1.memory_percent():
                    #peakMemory = p1.memory_percent() 
            
            j += 1
    
    return
    
    
def merge(data,first,mid,last,sorted):
    global count
    global compareCount
    global peakMemory
    
    global timer
    global datastatus
    
    p1 = psutil.Process(os.getpid())
    
    i = first
    j = mid
    k = 0
    
    while(i < mid and j < last):
        compareCount +=1
        if(data[i]<data[j]):
        
            sorted[k] = data[i]
            k = k+1
            i = i+1
            
        else:
            
            sorted[k] = data[j]
            k = k+1
            j = j+1
            
    while (i<mid):
           
        sorted[k] = data[i]
        k = k+1
        i = i+1
         
            
    while (j<last):
           
        sorted[k] = data[j]
        k = k+1
        j = j+1
        
            
    v = 0
    while(v < k):
        data[first+v] = sorted[v]
        v=v+1
        count = count + 1 
        
    plt.bar(height=datastatus,left=range(1,51))
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.savefig("mergesortimage/img" + '%04d' % timer + ".png")
    plt.clf()
    timer += 1
    
    #if peakMemory < p1.memory_percent():
        #peakMemory = p1.memory_percent()         
    
    return
            
def mergeSort(data,first,last,sorted):
    
    global timer
    global datastatus
    
    plt.bar(height=datastatus,left=range(1,51))
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.savefig("mergesortimage/img" + '%04d' % timer + ".png")
    plt.clf()
    timer += 1
    
    if (first + 1 < last):
        
        mid = int((first+last)/2)
        mergeSort(data, first, mid, sorted)
        mergeSort(data, mid,last, sorted)
        merge(data,first,mid,last,sorted)
        
    
    return


def quickPartition(data,low,high):
    global count
    global compareCount
    global peakMemory
    
    global timer
    global datastatus    
    
    p1 = psutil.Process(os.getpid())
    
    pivot = data[low]

    
    while(low < high):
        
        while(low<high and data[high] > pivot ):
            compareCount += 1
            high-=1
            
        #temp = data[low]        
        data[low] = data[high]
        count = count + 1 
        #data[high] =temp
    
        while(low<high and data[low] <= pivot ):
            compareCount += 1
            low += 1
        #temp = data[high]
        data[high] = data[low]
        count = count + 1 
        #data[low] = temp
            
        data[low] = pivot
        #if peakMemory < p1.memory_percent():
            #peakMemory = p1.memory_percent()
    
    plt.bar(height=datastatus,left=range(1,51))
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.savefig("quicksortimage/img" + '%04d' % timer + ".png")
    plt.clf()
    timer += 1
    
    
    return low
    
def quickSort(data,low,high): 
        
    global count
    global compareCount
    
        
    global timer
    global datastatus
    
    plt.bar(height=datastatus,left=range(1,51))
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.savefig("quicksortimage/img" + '%04d' % timer + ".png")
    plt.clf()
    timer += 1
    
    
    loc = 0
    if(low<high):
        loc = quickPartition(data, low, high)
        quickSort(data, low, loc-1)
        quickSort(data, loc+1, high)
        
    
    return



origindata = list(range(51,1,-1))
#origindata = list(range(1,51))

np.random.shuffle(origindata)
#print(data)
#data = np.random.randint(20)

'''plt.bar(height=origindata,left=range(1,51))
plt.show()

plt.clf()

plt.bar(height=range(1,51),left=origindata)
plt.show()'''

data = origindata.copy()
datastatus = data
timer = 0
bubbleSort(data)

data = origindata.copy()
datastatus = data
timer = 0
quickSort(data,0,len(data)-1)

data = origindata.copy()
datastatus = data
timer = 0
sorted =[]
for i in range(0,len(data)):
    sorted.append(i)

mergeSort(data, 0, len(data), sorted)

data = origindata.copy()
datastatus = data
timer = 0
insertSort(data)

data = origindata.copy()
datastatus = data
timer = 0
selectSort(data)




