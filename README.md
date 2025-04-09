# Reop

## Sobre

Um gerenciador de projetos para Linux.

## Instalação

### Nix

Você pode procurar no [FlakeHub](https://flakehub.com) por "Jhuan Reop" e usar a ferramenta `fh` para utilizar o flake.

Se, por algum motivo, você não quiser usar o FlakeHub, pode adicionar um input no seu flake do Home Manager:

```
reop.url = "github:Jhuan-Nycolas/Reop";
```

Depois, importe-o em **modules**:

```
modules = [
  # ...
  inputs.reop.homeManagerModules.reop
];
```

E, por fim, ative-o no seu `home.nix` usando:

```
{
  reop.enable = true;
}
```

## Outras distribuições

Para instalar o Reop em outras distros linux, basta baixar o binário na pasta dist e mover para `/usr/bin`

Após isso, será necessário reiniciar o terminal e, em seguida, poderá executar `reop` no terminal para visualizar os projetos que configurou.

## Configuração

Crie o arquivo `~/.config/reop/config.json`.

### Definindo editor e shell padrão

Para definir o editor que será utilizado nos projetos, adicione:

```
{
  "editor": "nix run github:Jhuan-Nycolas/Nvim"
}
```

**O valor da opção `editor` deve ser o comando que executa o editor.**

Para definir o shell que será utilizado, use:

```
{
  "editor": "nix run github:Jhuan-Nycolas/Nvim",
  "shell": "fish"
}
```

### Definindo projetos

Para configurar os projetos, utilize as seguintes opções:

```
{
  "editor": "nix run github:Jhuan-Nycolas/Nvim",
  "shell": "fish",

  "projects": {
    "Projeto 1": {
      "path": "~/pasta/para/o/projeto1"
    },

    "Projeto 2": {
      "path": "~/pasta/para/o/projeto2"
    }
  }
}
```

## Usando Nix DevShells

Se você usa Nix/NixOS, pode configurar o Reop para abrir um projeto com um DevShell que você definiu. Para isso, use:

```
{
  "editor": "nix run github:Jhuan-Nycolas/Nvim",
  "shell": "fish",

  "projects": {
    "Projeto 1": {
      "nixShell": {
        "path": "~/caminho/para/um/flake.nix",
        "host": "aqui vem o que viria depois do # (vazio para default)"
      },
      "path": "~/pasta/para/o/projeto1"
    },

    "Projeto 2": {
      "path": "~/pasta/para/o/projeto2"
    }
  }
}
```

### Configurando Reop com Nix

Se preferir configurar o Reop de forma declarativa, pode definir as opções normalmente em um arquivo `.nix`. Por exemplo:

```
{
  reop = {
    enable = true; # Necessário para instalar o Reop

    settings = {
      editor = "nix run github:Jhuan-Nycolas/Nvim";
      shell = "fish";

      projects = {
        projeto1 = {
          path = "~/Projeto1";

          nixShell = {
            path = "~/Projeto1/Nix";
            host = ""; # Indica que usará o host padrão
          };
        };
      };
    };
  };
}
```