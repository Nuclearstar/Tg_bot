import pip
import subprocess

def install(name):
    subprocess.call(['pip', 'install', name])

install('python-telegram-bot')