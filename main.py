from distutils import command
import os

path = os.getcwd()
def findCharacter(string, character):
    return [position for position, char in enumerate(string) if char == character]

def dir():
    return os.listdir(".")

def mkdir(name):
    try:
        os.mkdir(path+'/'+name[0])
        return "Directorio creado exitosamente"
    except OSError:
        return "Creation of the directory failed"

def error():
    return "Comando no válido"

def commands(cmds):
    cmdSplit = cmds.split()
    switcher = {
        "dir": dir,
        "mkdir": mkdir
    }
    return switcher[cmdSplit[0]](cmdSplit[1:])


cmds = input("->")
print(commands(cmds))

