

import atexit
import subprocess as sp
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        def kill_server(p):
            if os.name == 'nt':
                # p.kill is not adequate
                sp.call(['taskkill', '/F', '/T', '/PID', str(p.pid)])
            elif os.name == 'posix':
                p.kill()
            else:
                pass
        
        # file_url = 'D:/03. Learning/01. Coder/00. Git_code_backup/Streamlit/run_streamlit.bat'
        file_url = 'D:/03. Learning/01. Coder/00. Git_code_backup/Streamlit/run_strealit_main.bat'
        # cmd = f'streamlit run {file_url} --server.headless=True'

        p = sp.Popen(file_url, shell=True, stdout = sp.PIPE)
        atexit.register(kill_server, p)

        hostname = 'localhost'
        port = 8501

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(f'http://{hostname}:{port}'))

        self.setCentralWidget(self.browser)

        self.show()

app = QApplication(sys.argv)
window = MainWindow()

app.exec_()