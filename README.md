# Reop

Um gerenciador de projetos pra linux

Você vai criar um arquivo de configuração em ~/.config/reop/config.json

Nesse arquivo você vai ter duas opções

{<br>
  "editor": "comando para iniciar o seu editor, exemplo: nvim",<br>
  "projects": {<br>
    lista de projetos, exemplo:<br>
    "Reop": {<br>
      path = "~/Reop"<br>
    }<br>
  }<br>
}<br>

depois crie um scrip sh em /bin com o seguinte conteúdo:

python /caminho/para/open.py

ao iniciar você vai ver uma lista com os projetos que você definiu em config.json
