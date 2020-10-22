class Environment:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = "200 OK"
        headers = [("Content-type", "text/plain")]
        self.start(status, headers)
        bodylist = [
            '{key}: {value}'.format(key=key, value=value) for key, value in sorted(self.environ.items())
        ]
        body = '\n'.join(bodylist)
        body += '\n'
        yield body.encode()
