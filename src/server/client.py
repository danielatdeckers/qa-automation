import cherrypy

def init():
    pass

def group(clientObj, rootRoute):
    cherrypy.tree.mount(clientObj, rootRoute, 'src/client.conf')

def endpoint(function):
    @cherrypy.expose
    def _(*args, **kwargs):
        return function(*args, **kwargs)
    return _