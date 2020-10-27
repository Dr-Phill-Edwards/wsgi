class Application:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = "200 OK"
        headers = [("Content-type", "text/plain")]
        self.start(status, headers)
        for chunk in [b"Welcome" b" " b"to" b" " b"WSGI!\n"]:
            yield chunk

