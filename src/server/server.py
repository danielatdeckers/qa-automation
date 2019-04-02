import cherrypy
from cherrypy._cpserver import Server

import endpoints

#* Server Setup
cherrypy.server.unsubscribe()

dispatchServer = Server()
dispatchServer.socket_port = 4000
dispatchServer.subscribe()

if __name__ == "__main__":
    endpoints.init()
    cherrypy.engine.start()
    cherrypy.engine.block()
    