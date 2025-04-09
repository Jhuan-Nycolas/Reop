import argparse
import program

version = "0.3.2"

parser = argparse.ArgumentParser(
    description="Reop - Gerenciador de projetos para Linux"
)

parser.add_argument(
    "-v", "--version", action="store_true", help="Exibe a versão do programa"
)

args = parser.parse_args()

if args.version:
    print(f"Reop - {version}")
else:
    try:
        program.run()
    except KeyboardInterrupt:
        print("\nStoped")
