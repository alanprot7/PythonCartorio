import asyncio
import subprocess
class TesteAsync:

    def __init__(self):
        self.ioloop = asyncio.get_event_loop()
        self.tasks = []

    def task(self, programa, tempo):
        minutos = tempo * 60
        while True:
            yield from asyncio.sleep(minutos)
            subprocess.call(programa, shell=True)

    def ioloopCreatTask(self, task, programa, tempo):
        self.tasks.append(self.ioloop.create_task(task(programa, tempo)))

    def run(self):
        wait_tasks = asyncio.wait(self.tasks)
        self.ioloop.run_until_complete(wait_tasks)
        self.ioloop.close()

def main():

    app = TesteAsync()
    programa = 'python envia_email_adalberto.py'
    minutos = 5
    app.ioloopCreatTask(app.task, programa, minutos)
    app.run()

if __name__ == '__main__':
    main()