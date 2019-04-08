import os, subprocess

from config import configManager

class ScriptManager(object):
    def __init__(self):
        self.scriptArray = {}
        self.macroConfig = {}
        self.results = {}
        self.refresh()
    
    def add(self, scriptName = "", args = ""):
        scriptCommand = None
        for script in self.scriptArray:
            if script["name"] == scriptName:
                scriptCommand = script["execution"]
        if scriptCommand != None:
            process = subprocess.Popen("{} {}".format(scriptCommand, args).split(" "))

        try:
            process.wait(timeout = self.macroConfig["timeout"])
        except:
            process.kill()

    def setResult(self, scriptName, result = ""):
        self.results[scriptName] = result

    def getResult(self, scriptName):
        if scriptName in self.results:
            result = self.results[scriptName]
            self.results.pop(scriptName, None)
            return result
        return 404

    def refresh(self):
        configManager.refresh()
        config = configManager.getConfig()
        self.macroConfig = config["macro-config"]
        self.scriptArray = config["scripts"]
    