# Reop

## Sobre

Um gerenciador de projetos pra linux

## Instalação

### Nix

- [Overlay](https://github.com/Jhuan-Nycolas/NixDotfiles/tree/main/Overlays/Reop)

**Preparando flake e logo estará disponível no [FlakeHub](https://www.flakehub.com)**

## Configuração

Crie um arquivo em `~/.config/reop/config.json`

### Definindo editor

Para definir o editor que será usado nos projetos adicione:

```
{
  "editor": "nix run github:Jhuan-Nycolas/Nvim"
}
```

**O valor na opção editor precisa ser o comando que executa o editor**

### Definindo projetos

Para definir os projetos você usa as seguintes opções

```
{
  "editor": "nix run github:Jhuan-Nycolas/Nvim",

  "projects": {
    "Nome Do Projeto1": {
      "path": "~/pasta/para/o/projeto1"
    }
    
    "Nome Do Projeto2": {
      "path": "~/pasta/para/o/projeto2"
    }
  }
}
```

**Logo mais opções estarão disponíveis**
