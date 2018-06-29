import pip
import subprocess

def install(name):
    subprocess.call(['pip', 'install', name])

install('pip')
install('sqlalchemy')
install('psycopg2-binary')
install('python-telegram-bot')
