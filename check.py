import sys
fileinput = sys.argv[1]
arg = sys.argv[2]
if arg == "N":
    with open(fileinput, 'r') as f:
        f_count = f.read()
    print(f_count)
    print("The process has been completed in normal mode.")

elif arg == "S":
    print("The process has been completed in silent mode.")

else:
    print("Please enter a valid flag.")