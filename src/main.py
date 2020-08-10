from argParsing import argParser
from seleniumProcesses import seleniumProcesses

def main():
    seleniumProcesses(argParser())
    

if __name__ == "__main__":
    main()
