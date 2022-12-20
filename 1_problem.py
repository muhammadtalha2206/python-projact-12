def readfile(Filename):
    try:
        with open(Filename,'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"This file {Filename} is not present.")
readfile("1.txt")
readfile("2.txt")
readfile("3.txt")