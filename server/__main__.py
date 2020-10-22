from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.wsgi import WSGIContainer
from .Application import Application
from .Environment import Environment
from .Server import Server

define("port", default=8080, help="Listener port")
options.parse_command_line()
#container = WSGIContainer(Application)
#container = WSGIContainer(Environment)
container = Server()
server = HTTPServer(container)
server.listen(options.port)
print("Listening on port", options.port)
IOLoop.current().start()
