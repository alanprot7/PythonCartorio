from cx_Freeze import setup, Executable

setup(
    name="Gera Movimento",
    version = "1.0.0",
    description = "Gera Relatorio Movimento",
    executables = [Executable("gera_relatorio_movimento.py")])