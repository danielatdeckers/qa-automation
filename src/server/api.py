import cherrypy
import json

import execution
import logger
import tokenmanager

scriptManager = execution.ScriptManager()
logger = logger.Log()
tokenmanager.init()

'''

'''
def init():
    cherrypy.tree.mount(API(), '/api', 'src/api.conf')
    cherrypy.tree.mount(UserAPI(), '/api/user', 'src/api.conf')
    cherrypy.tree.mount(ScriptAPI(), '/api/script', 'src/api.conf')

'''

'''
class UserAPI(object):
    @cherrypy.expose
    def index(self):
        return "This is meant for user interaction with the server to run scripts"

    @cherrypy.expose
    def result(self, scriptName):
        #? GET Operation
        pass

    @cherrypy.expose
    def run(self, scriptName):
        #? Post Operation
        pass

'''

'''
class ScriptAPI(object):
    @cherrypy.expose
    def index(self):
        return "In order to use the script api you need to pass the token located on the server that is changed every so often."

    @cherrypy.expose
    def log(self, scriptName):
        #? Post
        pass

    @cherrypy.expose
    def run(self, scriptName):
        #? Post
        pass

    @cherrypy.expose
    def results(self, scriptName):
        #? Put
        pass

'''
Used to direct users to the right Api routes for their appropriate uses
'''
class API(object):
    @cherrypy.expose
    def index(self):
        return "API Route, Use /api/user for user opperations or /api/script for script operations"


'''

'''
class ErrorHandler(object):
    def __init__(self, errorDictonary):
        errorDictonary = errorDictonary

    def handleError(self, errorCode):
        pass
'''

'''
class RequestHandling(object):
    def __init__(self, requestType = "GET", needsToken = False, errorHandler = ErrorHandler({}), *queryies):
        self.needsToken = needsToken
        self.requestType = requestType
        self.queries = queryies
        self.errorHandler = errorHandler
    
    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        pass

    def authorized(self, token):
        if(self.needsToken):
            return tokenmanager.compare(token)
        return True
