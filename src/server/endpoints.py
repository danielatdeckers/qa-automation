import api
import execution
import client

scriptManager = execution.ScriptManager()
api.init()
client.init()

def init():
    client.group(FrontEnd(), "/")
    api.group(UserAPI(), "/api/user")
    api.group(ScriptAPI(), "/api/script")

class FrontEnd(object):
    @client.endpoint
    def index(self):
        return open("src/public/index.html")

class UserAPI(object):
    @api.endpoint
    def result(self, scriptName=""):
        with api.Request("GET", False) as (authorized, status):
            if authorized:
                result = scriptManager.getResult(scriptName)
                status(result)
                return result

    @api.endpoint
    def run(self, scriptName="", scriptParams={}, args = ""):
        with api.Request("POST", False) as (authorized, status):
            if authorized:
                scriptManager.add(scriptName)
                return {"Result":"Completed"}

class ScriptAPI(object):
    @api.endpoint
    def run(self, scriptName="", args = ""):
        with api.Request("POST", True) as (authorized, status):
            if authorized:
                scriptManager.add(scriptName)
                return {"Result":"Completed"}

    @api.endpoint
    def result(self, scriptName="", scriptResults={}):
        with api.Request("GET", False) as (authorized, status):
            if authorized:
                scriptManager.setResult(scriptName, scriptResults)
                return {"Result":"Completed"}
    
    @api.endpoint
    def update(self):
        with api.Request("GET", False) as (authorized, status):
            if authorized:
                scriptManager.refresh()
                api.refresh()
                return {"Result":"Completed"}