import json

class ConfigManager(object):
    def __init__(self):
        self.config = {}
        self.refresh()

    def refresh(self):
        try:
            script_json = open("src\server\config.json", "r")
            self.config = json.load(script_json)
            return 0
        except Exception:
            print("Failed To Get Config")
            return 500
    
    def getConfig(self):
        return self.config

configManager = ConfigManager()