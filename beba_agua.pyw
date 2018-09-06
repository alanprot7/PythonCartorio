import os
import time

class BebaAgua:

    def contaTempo(self, hora):
        tempo = 3600 * hora
        time.sleep(tempo)

    def comandoBloqueiaTela(self):
        os.system("rundll32 user32.dll,LockWorkStation")

def main():

    prog = BebaAgua()
    while (True):
        prog.contaTempo(1)
        prog.comandoBloqueiaTela()

if __name__ == "__main__":
    main()