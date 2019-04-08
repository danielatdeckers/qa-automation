import cherrypy
import tokenmanager
from config import configManager

class ErrorHandler(object):
    def __init__(self):
        self.errorDictionary = configManager.getConfig()["error"]["errorManagement"]
        self.fallback = configManager.getConfig()["error"]["fallback"]

    def error(self, status, message, traceback, version):
        if status.split(" ")[0] in self.errorDictionary:
            cherrypy.response.headers["Content-Type"] = self.errorDictionary[status.split(" ")[0]]["type"]
            return self.errorDictionary[status.split(" ")[0]]["message"]
        cherrypy.response.headers["Content-Type"] = self.fallback["type"]
        return self.fallback["message"]

    def refresh(self):
        self.errorDictionary = configManager.getConfig()["error"]["errorManagement"]
        self.fallback = configManager.getConfig()["error"]["fallback"]

class Request(object):
    def __init__(self, requestType = "GET", needsToken = False, successCode = 200):
        self.needsToken = needsToken
        self.requestType = requestType
        self.status = 200
    
    def __enter__(self):
        return (self._checkHandler("enter"), self.changeStatus)

    def __exit__(self, type, value, traceback):
        self._checkHandler("exit")

    def changeStatus(self, result):
        if isinstance(result, int) and result != 200:
            self.status = result

    #* Private Methods
    def _checkHandler(self, type = ""):
        if type == "enter":
            if not self._checkRequest():
                return False
            if self.needsToken:
                return self._requestAuthorization()
            return True
        elif type == "exit":
            if self.status != 200:
                raise cherrypy.HTTPError(self.status)
        else:
            return True

    def _requestAuthorization(self):
        if "Authorization" in cherrypy.request.headers:
            authList = cherrypy.request.headers["Authorization"].split(" ")
            if len(authList) == 2 and authList[0] == "token":
                token = cherrypy.request.headers["Authorization"].split(" ")[1]
            else:
                self.status = 400
                return False
        else:
            self.status = 400
            return False

        if not (tokenmanager.compare(token)):
            self.status = 401
            return False
        return True

    def _checkRequest(self):
        if not('Content-Type' in cherrypy.request.headers and cherrypy.request.headers['Content-Type'] == "application/json"):
            self.status = 400
            return False
        if cherrypy.request.method.lower() != self.requestType.lower():
            self.status = 400
            return False
        return True

def endpoint(function):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def _(*args, **kwargs):
        return function(*args, **kwargs)
    return _

def init():
    cherrypy.config.update({
        'error_page.400': errorHandler.error,
        'error_page.401': errorHandler.error,
        'error_page.404': errorHandler.error,
        'error_page.500': errorHandler.error,
    })

def refresh():
    errorHandler.refresh()

def group(apiObject, rootRoute):
    config = {}
    config[rootRoute] = {
        'tools.staticdir.on': False
    }
    cherrypy.tree.mount(apiObject, rootRoute, config=config)

tokenmanager.init()
errorHandler = ErrorHandler()