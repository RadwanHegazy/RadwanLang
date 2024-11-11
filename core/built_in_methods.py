import os


def cleanScreen () :
    os.system('cls')

def write (*args) : 
    for i in args: 
        print(i, end="\n")