import cherrypy
import json

import execution
import logger

scriptManager = execution.ScriptManager()
logger = logger.Log()

def getToken():
    return ""
    pass

def init():
    cherrypy.tree.mount(API(), '/api', 'src/api.conf')
    cherrypy.tree.mount(UserAPI(), '/api/user', 'src/api.conf')
    cherrypy.tree.mount(ScriptAPI(), '/api/script', 'src/api.conf')

class UserAPI(object):
    @cherrypy.expose
    def index(self):
        return "This is meant for user interaction with the server to run scripts"

    @cherrypy.expose
    def result(self, scriptName):
        #! Error Handling
        #? GET Operation
        pass

    @cherrypy.expose
    def run(self, scriptName):
        #! Error Handling
        requestBody = cherrypy.request.body.read()
        #? Post Operation
        pass

class ScriptAPI(object):
    @cherrypy.expose
    def index(self):
        return "In order to use the script api you need to pass the token located on the server that is changed every so often."

    @cherrypy.expose
    def log(self, scriptName):
        #! Error Handling
        requestBody = cherrypy.request.body.read()
        pass

    @cherrypy.expose
    def results(self, scriptName):
        #! Error Handling
        requestBody = cherrypy.request.body.read()
        pass

    def compareToken(self, token):
        serverToken = getToken()
        pass

class API(object):
    @cherrypy.expose
    def index(self):
        return "API Route, Use /api/user for user opperations or /api/script for script operations"