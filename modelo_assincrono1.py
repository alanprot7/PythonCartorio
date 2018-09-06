import asyncio
import subprocess

@asyncio.coroutine
def primeiroProcesso():
 
    yield   # Usa-se o yield para o agendador colocar em execução separada
    subprocess.call('python check_distribuidor.py')


@asyncio.coroutine
def segundoProcesso():
    # Sem o yield o processo segue fluxo normal
    subprocess.call('python cancelados_sem_custa.py')


ioloop = asyncio.get_event_loop()  # Event Loop

tasks = [ioloop.create_task(primeiroProcesso()),
         ioloop.create_task(segundoProcesso())]

wait_tasks = asyncio.wait(tasks)

ioloop.run_until_complete(wait_tasks)

ioloop.close()