import sys
import os
import urllib.request
import json
from distutils.dir_util import copy_tree
from random import randint
import shutil
from pathlib import Path


projectsPath = "D:\\Projects\\"
workspacePath = "D:\\Work Spaces"
repo = ""
visibility = ""
projectName = ""
tempName = ""
technology = ""
workspaceName = ""
emojis = [":crown:",
          ":man_technologist:", ":santa:", ":superhero:", ":unicorn:", ":lion:"]
commands = ['git add .',
            f'git commit -m "{emojis[randint(0, len(emojis)-1)]} Show Time!"',
            'git branch -M main']


def connect():
    try:
        urllib.request.urlopen("https://kingtechnologies.in")
        return True
    except:
        return False


def flutter():
    os.system(f'flutter upgrade')
    os.system(f'flutter create .')


def chooseRepoType(x=0):
    global repo
    if(x == 0):
        print('''Choose Repository Type:
        1. Local Repository
        2. Global Repository
        3. Organization Repository'''.replace("  ", "").replace("\n", "\n\t"))
        x = input("Repository Type: ")
    if x == "1":
        repo = "local"
    elif x == "2":
        repo = "global"
    elif x == "3":
        repo = "organization"
    else:
        y = input(
            "Wrong Input, Wanna Try again! or Exit(y/Y): ")
        if (y.lower() == "y"):
            exit("Exiting...")
        else:
            chooseRepoType(y)


def chooseVisibility(x=0):
    global visibility
    if repo == "global" or repo == "organization":
        if x == 0:
            print('''Choose Project Visibility:
                1. Public
                2. Private'''.replace("  ", "").replace("\n", "\n\t"))
            x = input("Project Visibility: ")
        if x == "1":
            visibility = "public"
        elif x == "2":
            visibility = "private"
        else:
            y = input(
                "Wrong Input, Wanna Try again! or Exit(y/Y): ")
            if (y.lower() == "y"):
                exit("Exiting...")
            else:
                chooseVisibility(y)


def chooseTechnology():
    global technology
    print('''Choose Technology:
    1. Flutter
    2. PHP
    3. Node
    4. Python
    5. Basic Web
    6. React
    7. Angular
    8. Vue
    9. Rust
    10. Go'''.replace("  ", "").replace("\n", "\n\t"))
    x = input("Technology: ")
    if x == "1":
        technology = "Flutter"
    else:
        y = input(
            "Wrong Input, Wanna Try again! or Exit(y/Y): ")
        if (y.lower() == "y"):
            exit("Exiting...")
        else:
            chooseVisibility(y)


def addEntryToWorkspace():
    global workspaceName
    if technology == "Flutter":
        workspaceName = 'Flutter.code-workspace'
    os.chdir(workspacePath)
    with open(workspaceName) as json_file:
        data = json_file.read()
        data = json.loads(data.replace("'", "\"").replace("\t", "").replace(
            "  ", "").replace("\n", "").replace(",}", "}").replace(",]", "]"))
        data["folders"].append({"path": "..\\Projects\\"+projectName})
        tempList = sorted(
            list({v["path"]: v for v in data["folders"]}.values()), key=lambda k: k["path"])
        data["folders"] = tempList
    with open(workspaceName, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    os.startfile(workspacePath+'\\'+workspaceName)


def localRepo():
    _dir = projectsPath + '/' + projectName
    os.mkdir(_dir)
    os.chdir(_dir)
    os.system('git init')


def globalRepo():
    global projectName
    _dir = projectsPath + '/' + projectName
    os.chdir(projectsPath)
    try:
        if repo == "global":
            if visibility == "private":
                os.system(f'gh repo create {projectName} --private -y')
            else:
                os.system(f'gh repo create {projectName} --public -y')
        else:
            if visibility == "private":
                os.system(
                    f'gh repo create king-technologies/{projectName} --private  -y')
            else:
                os.system(
                    f'gh repo create king-technologies/{projectName} --public -y')
        commands.append("git push -u origin main")
        os.chdir(_dir)
    except:
        x = input(
            f'{projectName} Repo already exist Try another name or exit(y): ')
        if (x.lower() == "y"):
            exit("Exit")
        elif (connect()):
            projectName = x
            globalRepo(projectName)
        else:
            y = input(
                "No Internet Connection! Want to work locally (y) or exit: ")
            if (y.lower() == "y"):
                projectName = x
                localRepo(x)
            else:
                exit("Exit")


def createRepo():
    if repo == "local":
        localRepo()
    else:
        globalRepo()


def prepareProject():
    global projectName
    if(technology == "Flutter"):
        projectName = tempName.lower().replace(" ", "_")


def createProject():
    if technology == "Flutter":
        flutter()


def addUtilities():
    os.makedirs('assets/images')
    description = input(f"Enter Description for {tempName}: ")
    repoTitle = tempName.capitalize()
    repoEmail = tempName.capitalize().replace(" ", "%20")
    with open("D:\Projects\Project-Initiator\ReadMeTemplate.md", "r", encoding="utf-8") as f:
        d = f.readlines()

    with open("README.md", "w", encoding="utf-8") as r:
        for i in d:
            y = i
            if repo == "global":
                y = i.replace("<repo-owner>", "Rohit19060")
            else:
                y = i.replace("<repo-owner>", "king-technologies")
            y = y.replace("<repo-name>", projectName)
            y = y.replace("<repo-desc>", description)
            y = y.replace("<repo-lang>", technology)
            y = y.replace("<repo-title>", repoTitle)
            y = y.replace("<repo-email>", repoEmail)
            r.write(y)
    src = "D:\Projects\Project-Initiator\Templates"
    import subprocess
    proc = subprocess.Popen(["cd"],
                            stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    dst = str(out).strip().replace("\\n", "").replace(
        "b'", "").replace("'", "").replace("\\r", "")
    if not os.path.exists(dst+"\\.github") and os.path.exists(src):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy(s, d)


if len(sys.argv) <= 2:
    tempName = str(sys.argv[1])
    chooseRepoType()
    chooseVisibility()
    chooseTechnology()
    prepareProject()
    createRepo()
    createProject()
    addUtilities()
    for c in commands:
        os.system(c)
    addEntryToWorkspace()
