from webob import Response,Request,dec,exc
from wsgiref.simple_server import make_server

class Application:

    routeable = {}
    @classmethod
    def register(cls,path):
        def wrapper(handler):
            cls.routeable[path] = handler
            return handler
        return wrapper

    @dec.wsgify
    def __call__(self, request:Request) -> Response:
        try:
            return self.routeable.get(request.path)(request)
        except:
            raise exc.HTTPNotFound("not found")


@Application.register('/')  # indexd = application.register('/')(index)
def index(request: Request):
    res = Response()
    res.body = "<h1>马哥教育root</ha>".encode()
    return res

@Application.register('/python')
def showpython(request: Request):
    res = Response()
    res.body = "<h1>马哥教育python</ha>".encode() 
    return res

# Application.register('/',index)
# Application.register('/python',showpython)


if __name__ == "__main__":
    ip = '0.0.0.0'
    port = 9999
    server = make_server(ip,port,Application())
    try:
        server.serve_forever()
    except:
        pass
    finally:
        server.server_close()

