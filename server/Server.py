import os, sys
from tornado.web import Application
from .WSGIRunner import WSGIRunner

class Server(Application):
    def __init__(self):
        super(Server, self).__init__([
            ("/(.*)", WSGIRunner),
        ])
