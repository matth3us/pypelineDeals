class pipelineDeals:
    def __init__(self):
        self.api_key = None
        self.app_key = None
    
    def addKey (self, api_key):
        self.api_key = api_key
    
    def addApplicationKey(self, app_key):
        self.app_key = app_key
    
    def hasKey(self):
        return self.api_key is not None
    
    def hasApplicationKey(self):
        return self.app_key is not None
