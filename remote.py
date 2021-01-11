import sys
import os
import urllib.request

path = "E:\\King Technologies\\Repos"


def connect():
    # checking internet connection
    try:
        urllib.request.urlopen("http://google.com")
        return True
    except:
        return False


def localrepo(folder=str(sys.argv[1])):
    try:
        _dir = path + '/' + folder
        commands = ['git init',
                    f'echo # {folder}> README.md',
                    'git add README.md',
                    'git commit -m "Initial Commit"',
                    'git branch -M main']
        os.mkdir(_dir)
        os.chdir(_dir)
        for c in commands:
            os.system(c)
        print(f'{folder} created locally')
        os.system('code .')
    except:
        x = input(
            f'{folder} already exist Try another Folder name or exit(y): ')
        if (x.lower() == "y"):
            exit("Exit")
        else:
            localrepo(x)


def globalrepe(folder=str(sys.argv[1])):
    try:
        _dir = path + '/' + folder
        commands = [f'echo # {folder}> README.md',
                    'git add README.md',
                    'git commit -m "Initial commit"',
                    'git branch -M main',
                    'git push -u origin main']
        os.chdir(path)
        if len(sys.argv) == 4:
            os.system(f'gh repo create {folder} --private -y')
        else:
            os.system(f'gh repo create {folder} --public -y')
        os.chdir(_dir)
        for c in commands:
            os.system(c)
        print(f'{folder} created globally')
        os.system('code .')
    except:
        x = input(
            f'{folder} Repo already exist Try another name or exit(y): ')
        if (x.lower() == "y"):
            exit("Exit")
        elif (connect()):
            globalrepe(x)
        else:
            y = input(
                "No Internet Connection! Want to work locally (y) or exit: ")
            if (y.lower() == "y"):
                localrepo(x)
            else:
                exit("Exit")


def organrepe(folder=str(sys.argv[1])):
    try:
        _dir = path + '/' + folder
        commands = [f'echo # {folder}> README.md',
                    'git add README.md',
                    'git commit -m "Initial commit"',
                    'git branch -M main',
                    'git push -u origin main']
        os.chdir(path)
        if len(sys.argv) == 4:
            os.system(
                f'gh repo create king-technologies/{folder} --private  -y')
        else:
            os.system(
                f'gh repo create king-technologies/{folder} --public -y')
        os.chdir(_dir)
        for c in commands:
            os.system(c)
        print(f'{folder} created globally')
        os.system('code .')
    except:
        x = input(
            f'{folder} Repo already exist Try another name or exit(y): ')
        if (x.lower() == "y"):
            exit("Exit")
        elif (connect()):
            organrepe(x)
        else:
            y = input(
                "No Internet Connection! Want to work locally (y) or exit: ")
            if (y.lower() == "y"):
                localrepo(x)
            else:
                exit("Exit")


if len(sys.argv) == 2:
    localrepo()
elif len(sys.argv) >= 3:
    if(connect()):
        if sys.argv[2] == "-g":
            globalrepe()
        elif sys.argv[2] == "-o":
            organrepe()
        else:
            print("Not a valid Input")
    else:
        y = input(
            "No Internet Connection! Want to work locally (y) or exit:")
        if (y.lower() == "y"):
            localrepo()
        else:
            exit("Exit")
