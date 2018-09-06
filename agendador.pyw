import subprocess
class Script:

    def lancar(self, app):
        lancamento = 'python ' + app
        subprocess.call(lancamento, shell = True)

def main():

    app = Script()
    app_agendado = 'cancelados_sem_custa.py'
    app.lancar(app_agendado)

if __name__ == "__main__":
    main()