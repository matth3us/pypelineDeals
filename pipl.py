#https://readthedocs.org
#preparar documentação!

#https://semaphoreci.com/community/tutorials/building-and-testing-an-api-wrapper-in-python
#organizar pastas

class pipelineDealsAuthenticator:
    api_key = ""
    api_application_key = ""

    def __init__(self):
        self.api_key = ""
        self.api_application_key = ""
    def addKey (self, api_key):
        self.api_key = api_key
    def addApplicationKey(self, api_application_key):
        self.api_application_key = api_application_key

class pipelineDeals(pipelineDealsAuthenticator):
    pass