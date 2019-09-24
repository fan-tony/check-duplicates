"""
Tony Fan
Program to check if two lines in a text file are identical
Nov.22/18
"""

def file_len(fName):
    with open(fName) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#scan the file and return a list where each index holds each line
def scanFile(fName):
    f = open(fName,"r");
    myList = f.readlines();

    for i in range(len(myList)):
        myList[i].rstrip('\n') #Removes the trailing newline character from reading the file
    return myList;
    f.close()

def checkIfIn(link,theList):
    for i in theList:
        if link == i:
            return True
    return False;
        
            
def printList(theList):
    for i in theList:
        print (i + "\n"); 

def removeRepeats(theList):
    numRemoved = 0
    indexI = 0#initialize values of the index in for loops underneath to 0; These respresent the value of the index that the current iteration of the for loop is on
    indexJ = 0
    for i in theList:#i represents the element of the current index of lol
        while (theList.count(i)) > 1:#If an element appears in the list more than once, remove that link
            if theList.count(i) == 2:
                print(i);
            theList.remove(i);#While there exists more than one copy of the element, remove them all until only one remains
            numRemoved += 1; #Add one to the counter to see how many were removed

    if (numRemoved == 0):
        print("There weren't any repeats");
    else:
        print( "\n\n" + str(numRemoved) + " links need to be removed. They are listed above.");
    
def main():

    lol = scanFile("givenStrings.txt"); #lol stands for list of links; givenLinks.txt is the name of the file

    removeRepeats(lol);
    #printList(lol)
    #print(checkIfIn("https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2744227/" + "\n",lol));       




main();
