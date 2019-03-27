import cherrypy

import execution
import tokenmanager

class ErrorHandler(object):
    def __init__(self, errorDictonary):
        self.errorDictonary = errorDictonary
        self.uniqueErrorMessage = "Unique Error"

    def handleError(self, errorCode):
        cherrypy.response.headers['Status'] = str(errorCode)
        try:
            return self.errorDictonary[errorCode]
        except: 
            return self.uniqueErrorMessage

scriptManager = execution.ScriptManager()
errorHandler = ErrorHandler({
    400: "400 - Bad Request",
    401: "401 - Unauthorized Access",
    404: "404 - Request Not Found"
})

def init():
    cherrypy.tree.mount(API(), '/api', 'src/api.conf')
    cherrypy.tree.mount(UserAPI(), '/api/user', 'src/api.conf')
    cherrypy.tree.mount(ScriptAPI(), '/api/script', 'src/api.conf')


def apiEndpoint(function):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def _(*args, **kwargs):
        return function(*args, **kwargs)
    return _

class UserAPI(object):
    @cherrypy.expose
    def default(self):
        return "This is meant for user interaction with the server to run scripts"

    @apiEndpoint
    def result(self, scriptName=""):
        with RequestHandling("GET", False, errorHandler, scriptName) as result:
            return {"Request": result}

    @apiEndpoint
    def run(self, scriptName="", scriptParams={}):
        with RequestHandling("POST", False, errorHandler, scriptName, scriptParams) as result:
            return {"Request": result}

class ScriptAPI(object):
    @cherrypy.expose
    def default(self):
        return "In order to use the script api you need to pass the token located on the server that is changed every so often."

    @apiEndpoint
    def params(self, scriptName=""):
        with RequestHandling("GET", True, errorHandler, scriptName) as result:
            return {"Request": result}

    @apiEndpoint
    def run(self, scriptName="", scriptParams={}):
        with RequestHandling("POST", True, errorHandler, scriptName, scriptParams) as result:
            return {"Request": result}

    @apiEndpoint
    def results(self, scriptName="", scriptResults={}):
        with RequestHandling("PUT", True, errorHandler, scriptName, scriptResults) as result:
            return {"Request": result}

class API(object):
    @cherrypy.expose
    def default(self, params = None):
        return "API Route, Use /api/user for user opperations or /api/script for script operations"

class RequestHandling(object):
    def __init__(self, requestType = "GET", needsToken = False, errorHandler = ErrorHandler({}), *queryies):
        self.needsToken = needsToken
        self.requestType = requestType
        self.queries = queryies
        self.errorHandler = errorHandler
        self.error = 0

        #* Headers
        cherrypy.response.headers['Content-Type'] = 'application/json'
        cherrypy.response.headers['Status'] = "200"
    
    def __enter__(self):
        #* Compare Token Given With Token On Server (401)
        if self.needsToken:
            #! Get Token From Request
            token = ""
            if not (tokenmanager.compare(token)):
                self.error = 401

        # if cherrypy.request.headers['Content-Type'] != 'application/json':
        #     self.error = 400

        #* Check If Script Name Specified (400)
        if(self.queries[0] == ""):
            self.error = 400

        #* Check if Request Type Matches (400)
        if cherrypy.request.method != self.requestType:
            self.error = 400

        #* Results (200)
        if self.error != 0:
            return {"Error": self.errorHandler.handleError(self.error)}
        elif len(self.queries) == 2:
            return self.queries[1]
        else:
            return {}

    def __exit__(self, type, value, traceback):
        pass

    
