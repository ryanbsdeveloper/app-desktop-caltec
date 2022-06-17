import webbrowser
import os
from datetime import datetime

def open_link(url):
    webbrowser.open(url)

def name_locauser():
    return os.getlogin()