import sys
from tornado.web import RequestHandler
from .Application import Application
from .Environment import Environment

class WSGIRunner(RequestHandler):
    headers = []
    url_map = {
        '/': Application,
        '/env': Environment
    }

    def get(self, path):
        path = '/' + path
        self.set_environment('GET', path)
        if path in WSGIRunner.url_map:
            self.run(WSGIRunner.url_map[path])
        else:
            self.send_error(404)

    def set_environment(self, method, path):
        self.environ = {
            'wsgi.errors': sys.stderr,
            'wsgi.input': sys.stdin.buffer,
            'wsgi.multiprocess': True,
            'wsgi.multithread': False,
            'wsgi.run_once': False,
            'wsgi.url_scheme': 'http',
            'wsgi.version': (1, 0),
            'HTTP_ACCEPT': self.request.headers['Accept'],
            'HTTP_HOST': self.request.headers['Host'],
            'HTTP_HTTP_USER_AGENT': self.request.headers['User-Agent'],
            'REQUEST_METHOD': method,
            'PATH_INFO': '/' + path
        }

    @staticmethod
    def start_response(status, response_headers):
        headers = response_headers

    def run(self, application):
        result = application(self.environ, WSGIRunner.start_response)
        for header in WSGIRunner.headers:
            self.set_header(header[0], header[1])
        for data in result:
            self.write(data)
