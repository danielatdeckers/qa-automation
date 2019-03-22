import cherrypy

def init():
    cherrypy.tree.mount(FrontEnd(), '/', 'src/client.conf')

class FrontEnd(object):
    @cherrypy.expose
    def index(self):
        #* Angular Frontend
        return open("src/public/index.html")