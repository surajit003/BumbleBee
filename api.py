from webob import Request, Response
from parse import parse


class API:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper

    def __call__(self, environ, start_response):
        request = Request(environ)
        response = self.handle_request(request)
        return response(environ, start_response)

    def find_handler(self, request):
        for path, handler in self.routes.items():
            parse_result = parse(path, request.path)
            if parse_result is not None:
                return handler, parse_result.named

    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found."

    def handle_request(self, request):
        user_agent = request.environ.get("HTTP_USER_AGENT", "No User Agent Found")
        response = Response()
        handler, kwargs = self.find_handler(request)
        if handler:
            handler(request, response, **kwargs)
        else:
            self.default_response(response)
        return response
