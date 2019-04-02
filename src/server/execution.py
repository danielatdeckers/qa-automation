import os
import subprocess
from config import configManager


class ScriptManager(object):
    def __init__(self):
        self.scriptData = {}
        self.executionTimeout = 10
        self.refresh()

    def refresh(self):
        configManager.refresh()
        config = configManager.getConfig()
        self.scriptData = config["scripts"]
        self.executionTimeout = config["executionTimeout"]
    
    def shutdown(self, process):
        try:
            process.wait(timeout = self.executionTimeout)
        except Exception:
            process.terminate()

    def run(self, scriptName = "", args = [""]):
        return self.runHelper(scriptName, args)

    def runHelper(self, scriptName = "", args = [""]):
        for script in self.scriptData:
            if script["name"] == scriptName:
                
                scriptCommand = " ".join(script["execution"].split(" ") + args)
                newProcess = subprocess.Popen(scriptCommand, shell = False)
                self.shutdown(newProcess)
                return 200
        return 404

    def result(self, scriptName, result = ""):
        pass