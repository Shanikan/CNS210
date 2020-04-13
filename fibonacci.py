# Do *not* test this thing with -n 5
import os.path
import argparse
import sys

def Main():
    parser = argparse.ArgumentParser(description="This program should find a requested number of the fibonnacci sequence. It should then print the results to a file. Functions in both Python 2 and 3.")
    parser.add_argument('-n', metavar='number', type=int, nargs='+', help="Integer in fibonacci sequence.")
    parser.add_argument('-f', metavar='filename', type=str, nargs='+', help="File for the program results to be written to.")
    y = "y"
    args = parser.parse_args()
    try:
        file = args.f[0]
    except:
        print("You can bring up the requested parameters with -h.")
        sys.exit()
    try:
        f = open(file, "r")
        try:
            erresp = input("This File Already Exists, would you like to overwrite? y/[n]: ")
            if erresp == y:
                f = open(file, "w") 
            else:
                print("No File to Write to, aborting program")
                
        except:
            print("No File to Write to, aborting program")
    except:
        print("File does not exist, creating new file...")
        f = open(file, "w")
            
        #f = open(file, "x")
    #try:
     #   erresp = input("This File Already Exists, would you like to overwrite? y/[n]: ")
      #  if erresp == y:
       #    f = open(file, "w") 
        #else:
         #   print("No File to Write to, aborting program")
                
   # except:
     #   print("No File to Write to, aborting program")
# 1==1 is to allow exceptions to stop any write attempts if they shouldn't happen,
# while printing nothing to console or file
    def fib(n):
        x, y = 0, 1
        count = 0
        # ^ For future loop ^
            
        if n <= 0:
            print("Please enter a positive integer")
        elif n == 1:
            try:
                f.write("Fibonacci sequence until requested number:")
                f.write(os.linesep)
                f.write(str(x))
            except:
                1 == 1
        else:
            try:
                f.write("Fibonacci sequence until requested number:")
            except:
                1 == 1
        while count <= n:
            try:
                f.write(os.linesep)
                f.write(str(x))
            except:
                1 == 1
            # Will go through with or without file, updates values to keep in loop
            nth = x + y
            x = y
            y = nth
            count += 1
        else:
            try:
                f.close()
            except:
                1 == 1
    
    # Don't know why following code quite works, but it does.
    result = fib(args.n[0])
if __name__ == '__main__':
    Main()
