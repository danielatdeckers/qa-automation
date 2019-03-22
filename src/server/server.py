import cherrypy
from cherrypy._cpserver import Server

import dispatcher
import api

#* Server Setup
cherrypy.server.unsubscribe()

dispatchServer = Server()
dispatchServer.socket_port = 4000
dispatchServer.subscribe()

if __name__ == "__main__":
    #* Deployment Instance
    api.init()
    dispatcher.init()
    cherrypy.engine.start()
    cherrypy.engine.block()
    