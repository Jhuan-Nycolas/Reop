from os import system
from time import sleep


def proj(editor, path, shell, cmdp):
    if shell == None:
        cmd = f"cd {path}"
        print(f"\nEntrando no diretório {path}")
        sleep(1)

        system(f"{cmd}; {editor}")
    else:
        cmd = f'cd {path}; nix develop {shell["path"]}#{shell["host"]} --command {cmdp} -c "{editor}"'
        print(f"\nEntrando no diretório {path}")
        sleep(1)
        print(f"Iniciando DevShell da pasta {shell["path"]}#{shell["host"]}")
        sleep(1)

        system(f"{cmd}")
