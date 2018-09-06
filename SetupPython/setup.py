from cx_Freeze import setup, Executable

setup(
    name="Pesquisa Titulos",
    version = "1.0.0",
    description = "Faz uma pesquisa na pasta de 2018",
    executables = [Executable("pesquisa_gildo.py")])