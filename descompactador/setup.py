from cx_Freeze import setup, Executable

setup(
    name="descompactador",
    version = "1.0.1",
    description = "Descompactador de arquivos",
    executables = [Executable("descompactardor_zip.py")])