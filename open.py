from gets import *
from func import proj, setConfig
from json import load
from os import getlogin

with open(f"/home/{getlogin()}/.config/reop/config.json") as config:
    conf = load(config)
    setConfig(conf)

editor = getEditor()

projects = getProjects()

opt = 1

print("0. Exit")

for project in projects:
    path = conf["projects"][project]["path"]
    print(f"{opt}. {project}: {path}")
    opt += 1

print()

enter = 0


def choose():
    global enter
    enter = int(input("> "))


try:
    choose()
except TypeError:
    print("Por favor escolha um número. Please choose a number.")
    choose()

if enter != 0:
    opt = 1

    for project in projects:
        path = conf["projects"][project]["path"]
        if enter == opt:
            proj(editor, path)
        opt += 1
