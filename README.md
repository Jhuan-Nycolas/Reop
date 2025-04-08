# Reop

## Sobre

Um gerenciador de projetos pra linux

## Instalação

### Nix

- [Overlay](https://github.com/Jhuan-Nycolas/NixDotfiles/tree/main/Overlays/Reop)

**Preparando flake e logo estará disponível no [FlakeHub](https://www.flakehub.com)**

## Outras distros

Eu ainda não buildei uma versão para outras distros fora o NixOS.

Se você quiser pode usar o [Nix](https://nixos.org) Package Manager para usar o meu [Overlay](https://github.com/Jhuan-Nycolas/NixDotfiles/tree/main/Overlays/Reop) até eu buildar o Reop para outras distribuições Linux

Se você não quer usar o Nix por algum motivo você pode instalar o python na sua distro:

 - **Fedora**: `sudo dnf install python`
 - **Arch Linux**: `sudo pacman -Syu python`
 - **Ubuntu**: `sudo apt install python`

Depois crie o arquivo reop em /usr/bin com o seguinte conteúdo

```
#!/bin/bash

python3 /caminho/para/open.py
```

depois execute:

```
chmod +x ./reop
```

Depois disso você vai precisar reiniciar o seu terminal e logo após poderá executar reop no terminal e ver os projetos que você configurou

## Configuração

Crie um arquivo em `~/.config/reop/config.json`

### Definindo editor e o Shell padrão

Para definir o editor que será usado nos projetos adicione:

```
{
  "editor": "nix run github:Jhuan-Nycolas/Nvim"
}
```

**O valor na opção editor precisa ser o comando que executa o editor**

Para definir o Shell que será usado use:

```
{
  "editor": "nix run github:Jhuan-Nycolas/Nvim",
  "shell": "fish"
}
```

### Definindo projetos

Para definir os projetos você usa as seguintes opções

```
{
  "editor": "nix run github:Jhuan-Nycolas/Nvim",
  "shell": "fish",

  "projects": {
    "Nome Do Projeto1": {
      "path": "~/pasta/para/o/projeto1"
    },
    
    "Nome Do Projeto2": {
      "path": "~/pasta/para/o/projeto2"
    }
  }
}
```

## Usando Nix DevShells

Se você usa Nix/NixOS você pode definir o Reop para  abrir um projeto com um DevShell que você configurou. Para fazer isso use:

```
{
  "editor": "nix run github:Jhuan-Nycolas/Nvim",
  "shell": "fish",

  "projects": {
    "Nome Do Projeto1": {
	  "nixShell": {
	    "path": "~/caminho/para/um/flake.nix",
	    "host": "aqui vem oque viria depois do #, aqui pode ser vazio também"
	  },

      "path": "~/pasta/para/o/projeto1"
    },
    
    "Nome Do Projeto2": {
      "path": "~/pasta/para/o/projeto2"
    }
  }
}
```
