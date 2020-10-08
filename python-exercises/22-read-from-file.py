"""
Exercise from: https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html
Code created by Ruben Jimenez
"""

def run():
    counter_dict = {}
    with open('Training_01.txt', 'r') as f:
        line = f.readline()
        while line:
            line = line[3:-26]
            if line in counter_dict:
                counter_dict[line] += 1
            else:
                counter_dict[line] = 1
            line = f.readline()
    print(counter_dict)


if __name__ == "__main__":
    run()