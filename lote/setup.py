from cx_Freeze import setup, Executable

setup(
    name="Multi Renomeador",
    version = "1.0.2",
    description = "Renomeia varios arquivos",
    executables = [Executable("mult_renomeacao2.py")])