import json
import os
import shutil
import sys
import urllib.request
from random import randint

projectsPath = "D:\\Projects\\"
workspacePath = "D:\\Work Spaces"
repo = ""
visibility = ""
projectName = ""
description = ""
tempName = ""
technology = ""
workspaceName = ""
emojis = [":crown:", ":santa:", ":superhero:", ":unicorn:", ":lion:"]
commands = ['git add .',
            f'git commit -m "{emojis[randint(0, len(emojis)-1)]} Show Time!"',
            'git branch -M main']


def connect():
    try:
        urllib.request.urlopen("https://kingtechnologies.dev")
        return True
    except:
        return False


def flutter():
    os.system(f'flutter create {projectName} --org dev.kingtechnologies')


def php():
    os.mkdir(projectName)
    os.chdir(projectName)
    open("index.php", "w")
    os.system("composer self-update")
    os.chdir(projectsPath)


def nodejs():
    os.mkdir(projectName)
    os.chdir(projectName)
    os.system("npm init -y")
    os.chdir(projectsPath)


def python():
    os.mkdir(projectName)
    os.chdir(projectName)
    open("main.py", "w")
    os.chdir(projectsPath)


def web():
    os.mkdir(projectName)
    os.chdir(projectName)
    open("index.html", "w")
    open("style.css", "w")
    open("script.js", "w")
    os.chdir(projectsPath)


def react():
    os.mkdir(projectName)
    os.chdir(projectName)
    os.system("npx create-react-app .")
    os.chdir(projectsPath)


def angular():
    os.system(f"ng new {projectName} -g --strict")
    os.chdir(projectsPath)


def vue():
    os.chdir(projectsPath)
    os.system("npm init vue@latest")
    os.chdir(projectName)
    os.system("npm i")
    os.chdir(projectsPath)


def rust():
    print("Coming Soon...")
    exit("Exiting...")


def go():
    print("Coming Soon...")
    exit("Exiting...")


def laravel():
    # Working Fine
    os.system("composer self-update")
    os.system(f"composer create-project laravel/laravel {projectName}")


def ci():
    os.system("composer self-update")
    print("Coming Soon...")
    exit("Exiting...")


def net():
    print("Coming Soon...")
    exit("Exiting...")


# Choose repo type i.e. Local, Global or Organization
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


# Choose repo visibility i.e. private or public
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


# Choose Technology by Their respective number
def chooseTechnology():
    global technology
    print('''Choose Technology:
    1. Flutter
    2. PHP
    3. NodeJS
    4. Python
    5. Basic Web
    6. React
    7. Angular
    8. Vue
    9. Rust
    10. Go
    11. Laravel
    12. CodeIgniter
    13. .Net'''.replace("  ", "").replace("\n", "\n\t"))
    x = input("Technology: ")
    if x == "1":
        technology = "Flutter"
    elif x == "2":
        technology = "PHP"
    elif x == "3":
        technology = "NodeJS"
    elif x == "4":
        technology = "Python"
    elif x == "5":
        technology = "Basic Web"
    elif x == "6":
        technology = "React"
    elif x == "7":
        technology = "Angular"
    elif x == "8":
        technology = "Vue"
    elif x == "9":
        technology = "Rust"
    elif x == "10":
        technology = "Go"
    elif x == "11":
        technology = "Laravel"
    elif x == "12":
        technology = "CodeIgniter"
    elif x == "13":
        technology = ".Net"
    else:
        y = input(
            "Wrong Input, Wanna Try again! or Exit(y/Y): ")
        if (y.lower() == "y"):
            exit("Exiting...")
        else:
            chooseVisibility(y)


# Add Entry to Workspace and Open it
def addEntryToWorkspace():
    global workspaceName
    if technology == "Flutter":
        workspaceName = 'Flutter.code-workspace'
    elif technology == "PHP":
        workspaceName = 'Php.code-workspace'
    elif technology == "NodeJS":
        workspaceName = 'Node.code-workspace'
    elif technology == "Python":
        workspaceName = 'Python.code-workspace'
    elif technology == "Basic Web":
        workspaceName = 'Web.code-workspace'
    elif technology == "React":
        workspaceName = 'React.code-workspace'
    elif technology == "Angular":
        workspaceName = 'Angular.code-workspace'
    elif technology == "Vue":
        workspaceName = 'Vue.code-workspace'
    elif technology == "Rust":
        workspaceName = 'Rust.code-workspace'
    elif technology == "Go":
        workspaceName = 'Go.code-workspace'
    elif technology == "Laravel":
        workspaceName = 'Php.code-workspace'
    elif technology == "CodeIgniter":
        workspaceName = 'Php.code-workspace'
    elif technology == ".Net":
        workspaceName = 'Net.code-workspace'
    else:
        print("Workspace Not Found")
        exit("Exiting...")
    os.chdir(workspacePath)
    with open(workspaceName, 'r', encoding="utf-8") as json_file:
        data = json_file.read()
        data = json.loads(data.replace("'", "\"").replace("\t", "").replace(
            "  ", "").replace("\n", "").replace(",}", "}").replace(",]", "]"))
        data["folders"].insert(0, {"path": "../Projects/"+projectName})
    with open(workspaceName, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    os.startfile(workspacePath+'\\'+workspaceName)


# Create Local Repo
def localRepo():
    _dir = projectsPath + '/' + projectName
    os.chdir(_dir)
    os.system('git init')


# Create Global Repo or Organization Repo
def globalRepo():
    global projectName
    global technology
    global description
    _dir = projectsPath + '/' + projectName
    description = input(f"Enter Description for {tempName}: ")
    try:
        os.chdir(_dir)
        os.system('git init')
        os.chdir(projectsPath)
        if repo == "global":
            if visibility == "private":
                os.system(
                    f'gh repo create {projectName} --private --description="{description}" --homepage="https://kingtechnologies.dev/" -s {projectName}')
            else:
                os.system(
                    f'gh repo create {projectName} --public --description="{description} Project" --homepage="https://kingtechnologies.dev/" -s {projectName}')
        else:
            if visibility == "private":
                os.system(
                    f'gh repo create king-technologies/{projectName} --private --description="{description}" --homepage="https://kingtechnologies.dev/" -s {projectName}')
            else:
                os.system(
                    f'gh repo create king-technologies/{projectName} --public --description="{description}" --homepage="https://kingtechnologies.dev/" -s {projectName}')
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


# Create Repo local or global based on choice
def createRepo():
    if repo == "local":
        localRepo()
    else:
        globalRepo()


# Naming Scheme according to the language
def prepareProject():
    global projectName
    os.chdir(projectsPath)
    if technology == "Flutter":
        projectName = tempName.lower()
    elif technology == "PHP":
        projectName = tempName
    elif technology == "NodeJS":
        projectName = tempName.lower()
    elif technology == "Python":
        projectName = tempName
    elif technology == "Basic Web":
        projectName = tempName
    elif technology == "React":
        projectName = tempName.lower()
    elif technology == "Angular":
        projectName = tempName.lower()
    elif technology == "Vue":
        projectName = tempName.lower()
    elif technology == "Rust":
        projectName = tempName
    elif technology == "Go":
        projectName = tempName
    elif technology == "Laravel":
        projectName = tempName.title()
    elif technology == "CodeIgniter":
        projectName = tempName.title()
    elif technology == ".Net":
        projectName = tempName
    else:
        exit("Wrong Technology")


# Call the respective function based on choice
def createProject():
    if technology == "Flutter":
        os.system(f'flutter upgrade -f')
        flutter()
    elif technology == "PHP":
        php()
    elif technology == "NodeJS":
        nodejs()
    elif technology == "Python":
        python()
    elif technology == "Basic Web":
        web()
    elif technology == "React":
        react()
    elif technology == "Angular":
        angular()
    elif technology == "Vue":
        vue()
    elif technology == "Rust":
        rust()
    elif technology == "Go":
        go()
    elif technology == "Laravel":
        laravel()
        commands.append("composer update")
    elif technology == "CodeIgniter":
        ci()
    elif technology == ".Net":
        net()
    else:
        exit("Exiting...")


# Add images folder, Readme File and Github Templates
def addUtilities():
    os.makedirs('assets/images')
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


# Check for the sys argument have -y or not
if "-y" in sys.argv:
    repo = "global"
    visibility = "public"
else:
    chooseRepoType()
    chooseVisibility()
tempName = str(sys.argv[1])
chooseTechnology()
prepareProject()
createProject()
createRepo()
addUtilities()
for c in commands:
    os.system(c)
addEntryToWorkspace()
