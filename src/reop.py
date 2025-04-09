from gets import *
from func import proj
from json import load
from os import getlogin
import argparse

version = "0.2.2"

parser = argparse.ArgumentParser(
    description="Reop - Gerenciador de projetos para Linux"
)

parser.add_argument(
    "-v", "--version", action="store_true", help="Exibe a versão do programa"
)

args = parser.parse_args()

if args.version:
    print(f"Reop - {version}")

with open(f"/home/{getlogin()}/.config/reop/config.json") as config:
    conf = load(config)
    setConfig(conf)

shell = getCmdp()

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
            proj(editor, path, conf["projects"][project]["nixShell"], shell)
        opt += 1
