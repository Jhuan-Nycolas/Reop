# Reop

Um gerenciador de projetos pra linux

Você vai criar um arquivo de configuração em ~/.config/reop/config.json

Nesse arquivo você vai ter duas opções

{
  "editor": "comando para iniciar o seu editor, exemplo: nvim",
  "projects": {
    lista de projetos, exemplo:
    "Reop": {
      path = "~/Reop"
    }
  }
}

depois crie um scrip sh em /bin com o seguinte conteúdo:

python /caminho/para/open.py

ao iniciar você vai ver uma lista com os projetos que você definiu em config.json
