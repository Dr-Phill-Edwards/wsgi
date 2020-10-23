from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from .WSGIRunner import WSGIRunner

define("port", default=8080, help="Listener port")
options.parse_command_line()
application = Application([("(/.*)", WSGIRunner)])
server = HTTPServer(application)
server.listen(options.port)
print("Listening on port", options.port)
IOLoop.current().start()
