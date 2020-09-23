import sys
import os
import urllib.request

path = '<Your Project Folder here>'


def connect():
    # Checking internet connection
    try:
        urllib.request.urlopen('http://google.com')
        return True
    except:
        return False


def localrepo(folder=str(sys.argv[1]).title()):
    try:
        _dir = path + "/"+folder
        commands = ['git init', f'echo #{folder}>Readme.md',
                    'git add Readme.md', 'git commit -m "Initial Commit"']
        os.mkdir(_dir)
        os.chdir(_dir)
        for c in commands:
            os.system(c)
        print(f'{folder} create Locally')
        os.system('code .')
    except:
        x = input(f'{folder} already exits try another name or exit(y): ')
        if(x.lower() == 'y'):
            exit('Exit')
        else:
            localrepo(x)


def globalrepo(folder=str(sys.argv[1]).title()):
    try:
        _dir = path + "/" + folder
        # https://github.com/setting/tokens
        token = '<Your Token here>'
        g = Github(token)
        user = g.get_user()
        login = user.login
        repo = user.create_repo(folder)
        commands = ['git init', f'git remote add origin https://github.com/{login}/{folder}.git', f'echo # {folder}>Readme.md',
                    'git add Readme.md', 'git commit -m "Initial Commit"', 'git push -u origin master']
        os.mkdir(_dir)
        os.chdir(_dir)
        for c in commands:
            os.system(c)
        print(f'{folder} created Globally')
        os.system('code .')
    except:
        x = input(
            f'{folder} repo/folder already exit try another name or exit(y): ')
        if(x.lower() == 'y'):
            exit('Exit')
        elif(connect()):
            globalrepo(x)
        else:
            x = input(f'No Internet Connection want to work locally(y) or exit: ')
            if(x.lower() == 'y'):
                localrepo(x)
            else:
                exit('Exit')


if len(sys.argv) == 2:
    # Pygithub package
    from github import Github
    if(connect()):
        globalrepo()
    else:
        y = input('No internet connection want to create local repo (y) or exit')
        if(y.lower() == 'y'):
            localrepo()
        else:
            exit('Exit')
elif sys.argv[2] == 'l':
    localrepo()
