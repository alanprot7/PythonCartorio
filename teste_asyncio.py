import asyncio

class TesteAsync:


    def __init__(self):
        self.ioloop = asyncio.get_event_loop()
        self.tasks = []

    def primeiro(self, tempo):
        print('primeiro')
        yield from asyncio.sleep(tempo)
        print('primeiro completo')

    def segundo(self, tempo):
        print('segundo')
        yield from asyncio.sleep(tempo)
        print('segundo completo')

    def ioloopCreatTask(self, task, tempo):
        self.tasks.append(self.ioloop.create_task(task(tempo)))

    def run(self):
        wait_tasks = asyncio.wait(self.tasks)
        self.ioloop.run_until_complete(wait_tasks)
        self.ioloop.close()

def main():

    app = TesteAsync()
    app.ioloopCreatTask(app.primeiro, 3)
    app.ioloopCreatTask(app.segundo, 2)
    app.run()

if __name__ == '__main__':
    main()