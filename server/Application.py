class Application:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = "200 OK"
        headers = [("Content-type", "text/plain")]
        self.start(status, headers)
        yield b"Welcome to WSGI!\n"
