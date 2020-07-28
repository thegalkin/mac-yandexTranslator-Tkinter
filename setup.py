"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

try:
    with open("secretKey.txt", "r") as f:
        secretKey = f.read()
except FileNotFoundError:
    secretKeyInput = ""
    while secretKeyInput == "":
        secretKeyInput = input("Please type in your yandex.Translate key    ")
    with open("secretKey.txt", "w+") as f:
        f.write(secretKeyInput)
    
    
from setuptools import setup

APP = ['Yandex.Translator.py']
DATA_FILES = ['yandex.icns', 'secretKey.txt']
OPTIONS = {
    'iconfile' : 'yandex.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
