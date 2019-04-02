import cherrypy

import api
from api import RequestHandler
from execution import ScriptManager


scriptManager = ScriptManager()
api.init()

def init():
    cherrypy.tree.mount(FrontEnd(), '/', 'src/client.conf')
    cherrypy.tree.mount(UserAPI(), '/api/user', 'src/api.conf')
    cherrypy.tree.mount(ScriptAPI(), '/api/script', 'src/api.conf')

class FrontEnd(object):
    @cherrypy.expose
    def index(self):
        #* Angular Frontend
        return open("src/public/index.html")

class UserAPI(object):
    @api.endpoint
    def result(self, scriptName=""):
        with RequestHandler("GET", False) as requestResult:
            return {"Request": "yep"}

    @api.endpoint
    def run(self, scriptName="", scriptParams={}, args = ""):
        with RequestHandler("POST", False) as requestResult:
            if requestResult[0]:
                result = scriptManager.run(scriptName)
                if result != 200:
                    requestResult[1](result)
                else:
                    return {"Result":"Completed"}

class ScriptAPI(object):
    @api.endpoint
    def params(self, scriptName=""):
        with RequestHandler("GET", True) as requestResult:
            return {"Request": "yep"}

    @api.endpoint
    def run(self, scriptName="", scriptParams={}, args = ""):
        with RequestHandler("POST", True) as requestResult:
            if requestResult[0]:
                result = scriptManager.run(scriptName)
                if result != 200:
                    requestResult[1](result)
                else:
                    return {"Result":"Completed"}

    @api.endpoint
    def results(self, scriptName="", scriptResults={}):
        with RequestHandler("PUT", True) as requestResult:
            return {"Request": "yep"}
    
    @api.endpoint
    def update(self):
        with RequestHandler("GET", False) as requestResult:
            if requestResult[0]:
                scriptManager.refresh()
                api.refresh()
                return {"Request": "yep"}