import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
else:
    print("Usage: python greet.py [your_name]")
