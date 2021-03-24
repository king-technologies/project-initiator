import sys
import os
import urllib.request

path = "D:\\Projects\\"


def connect():
    # checking internet connection
    try:
        urllib.request.urlopen("https://kingtechnologies.in")
        return True
    except:
        return False


def localRepo(folder=str(sys.argv[1])):
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
            localRepo(x)


def globalRepo(folder=str(sys.argv[1])):
    try:
        _dir = path + '/' + folder
        commands = [f'echo # {folder}> README.md',
                    'git add README.md',
                    'git commit -m "Initial commit"',
                    'git branch -M main',
                    'git push -u origin main']
        os.chdir(path)

        if sys.argv[2] == "-g":
            if len(sys.argv) == 4:
                os.system(f'gh repo create {folder} --private -y')
            else:
                os.system(f'gh repo create {folder} --public -y')
        elif sys.argv[2] == "-o":
            if len(sys.argv) == 4:
                os.system(
                    f'gh repo create king-technologies/{folder} --private  -y')
            else:
                os.system(
                    f'gh repo create king-technologies/{folder} --public -y')

        if len(sys.argv) >= 3:
            os.chdir(_dir)
            for c in commands:
                os.system(c)
            print(f'{folder} created globally')
            os.system('code .')
        else:
            print("Not a valid Input")

    except:
        x = input(
            f'{folder} Repo already exist Try another name or exit(y): ')
        if (x.lower() == "y"):
            exit("Exit")
        elif (connect()):
            globalRepo(x)
        else:
            y = input(
                "No Internet Connection! Want to work locally (y) or exit: ")
            if (y.lower() == "y"):
                localRepo(x)
            else:
                exit("Exit")


if len(sys.argv) == 2:
    localRepo()
elif len(sys.argv) >= 3:
    if(connect()):
        globalRepo()
    else:
        y = input(
            "No Internet Connection! Want to work locally (y) or exit:")
        if (y.lower() == "y"):
            localRepo()
        else:
            exit("Exit")
