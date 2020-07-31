# CSC3002F Assignment 3
# Author: JNRLEA001

import random
import sys

def main():
    size = int(sys.argv[1]) # generate this number of pages
    pages = []
    #pages = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    for i in range(0,16):
        x = random.randint(0,9)
        pages.append(x)
    print(pages)

    print ("FIFO = ", FIFO(size,pages), " page faults")
    print ("LRU = ", LRU(size,pages), "page faults")
    print ("OPT = ", OPT(size,pages), "page faults")

def FIFO(size, pages):
    currentPages = []
    pageFaults = 0

    for i in range(len(pages)):
        if (len(currentPages) < size):
            if (pages[i] not in currentPages):
                currentPages.append(pages[i])
                pageFaults += 1
                #print(currentPages)
        else:
            if (pages[i] not in currentPages):
                currentPages.pop(0)
                currentPages.append(pages[i])
                pageFaults += 1
                #print(currentPages)
            #else:
                #print(currentPages)

    return pageFaults;

def LRU(size, pages):
    currentPages = []
    pageFaults = 0

    for i in range(len(pages)):
        if (len(currentPages) < size):
            if (pages[i] not in currentPages):
                currentPages.append(pages[i])
                pageFaults += 1
                #print(currentPages)
        else:
            if (pages[i] not in currentPages):
                currentPages.pop(0)
                currentPages.append(pages[i])
                pageFaults += 1
                #print(currentPages)
            else:
                for k in range(size):
                    if (currentPages[k] == pages[i]):
                        currentPages.pop(k)
                        currentPages.append(pages[i])
                #print(currentPages)
    return pageFaults;

def OPT(size, pages):
    currentPages = []
    pageFaults = 0

    for i in range(len(pages)):
        if (len(currentPages) < size):
            if (pages[i] not in currentPages):
                currentPages.append(pages[i])
                pageFaults += 1
                #print(currentPages)
        else:
            if (pages[i] not in currentPages):
                maxVal = -1
                index = 0
                for j in range(size): 
                    found = False
                    for k in range(i,len(pages)):
                        if (currentPages[j] == pages[k]):
                            found = True
                            if (k > maxVal):
                                maxVal = k;
                                index = j;
                            break
                    if not found:
                        index = j;
                        break
                currentPages[index] = pages[i]
                pageFaults +=1
                #print(currentPages)

            #else:
                #print(currentPages)

    return pageFaults;


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python paging.py [number of pages]")
    if int(sys.argv[1]) < 1 or int(sys.argv[1]) > 7:
        print("Number of pages must be between 1 and 7.")
    else:
        main()
