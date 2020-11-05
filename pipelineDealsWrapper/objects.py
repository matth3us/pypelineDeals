# por nos testes: apenas parâmetros permitidos para cada; tipos permitidos de parâmetros; parâmetros obrigatórios tem que ser passados;
import requests as rq
from authenticator import pipelineDeals

def removeNonesDictionary(dictio):
    filtered = dict(filter(lambda item: item[1] is not None, dictio.items()))
    return filtered

class pipelineDealsObject(pipelineDeals):
    def __init__(self):
        self.url = "https://api.pipelinedeals.com/api/v3/"
        self.path = ""
        self.params = None
    
    def addParam(self, param, newValue):
        self.params[param] = newValue

    def hasId(self):
        return self.params['id'] is not None

    # def create(self, params):
    #     if(self.hasId() & self.hasKey()):
    #         params.api_key = self.api_key
    #         request = rq.post(self.path, data = params)
    #         response = request.json()
    #         return response

    def retrive(self):
        if(self.hasId() & self.hasKey()):
            self.addParam("api_key", self.api_key)
            passParams = removeNonesDictionary(self.params)
            request = rq.get(self.url + self.path, data = passParams)
            response = request.json()
            return response
        
    #def update(self, id, params):
        #PUT
    #def delete(self, id):
        #DELETE

class activities(pipelineDealsObject): 
    def __init__(self):
        self.path = "notes"

class companies(pipelineDealsObject): 
    def __init__(self):
        super().__init__()
        self.path = "companies"
        self.params = {"api_key": None, "id": None}

class customFieldCompanyGroups(pipelineDealsObject): 
    def __init__(self):
        self.path = "admin/company_custom_field_groups"

class customFieldDealsGroups(pipelineDealsObject): 
    def __init__(self): 
        self.path = "admin/deal_custom_field_groups"
        
class customFieldCompanyLabels(pipelineDealsObject): 
    def __init__(self):
        self.path = "admin/company_custom_field_labels"

class customFieldDealsLabels(pipelineDealsObject): 
    def __init__(self):
        self.path = "admin/deal_custom_field_labels"

class customFieldLabelDropdownEntries(pipelineDealsObject): 
    def __init__(self):
        self.path = "admin/custom_field_label_dropdown_entries"

class deals(pipelineDealsObject): 
    def __init__(self):
        self.path = "deals"

class people(pipelineDealsObject): 
    def __init__(self):
        self.path = "people"

class users(pipelineDealsObject): 
    def __init__(self):
        self.path = "admin/users"