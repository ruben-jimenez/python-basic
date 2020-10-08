"""
Exercise from: https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html
Code created by Ruben Jimenez
"""

def filetoIntlist(theFile):
    theList = []
    with open(theFile,'r') as f:
        line = f.readline()
        while line:
            theList.append(int(line))
            line = f.readline()
    return theList


def run():
    primenum = filetoIntlist('primenumbers.txt')
    happynum = filetoIntlist('happynumbers.txt')
    overlap = [number for number in primenum if number in happynum]
    print(overlap)


if __name__ == "__main__":
    run()