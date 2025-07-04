import click

from bioHerramientas import ncbiAPI 
from bioHerramientas import uniprotAPI

# CLI para realizar busquedas:
@click.group()
def cli():
    pass

# Buscar un gen, proteina o transcrito por su ID:
@cli.command()
@click.argument("prompt")
def buscar_gen(prompt):
    print(ps.buscar_gen(prompt))

@cli.command()
@click.argument("prompt")
def buscar_transcrito(prompt):
    print(ps.buscar_transcrito(prompt))

@cli.command()
@click.argument("prompt")
def buscar_proteina(prompt):
    print(ps.buscar_proteina(prompt))