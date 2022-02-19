import os
import re

def findWord(path, word):
    dirs = os.listdir(path)
    print(dirs)

path = os.getcwd()
print(path)

inputs = input('Insert command: ')
cmds = inputs.split()

if (cmds[0] == "find"):
    findWord(path, cmds[1])


