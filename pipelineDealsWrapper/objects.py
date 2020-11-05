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
    
    def addOrUpdateParams(self, newValuesDictionary):
        self.params.update(newValuesDictionary)

    def hasId(self):
        return self.params['id'] is not None

    def create(self):
        if(self.hasKey()):
            self.addOrUpdateParams({"api_key": self.api_key})
            passParams = removeNonesDictionary(self.params)
            request = rq.post(self.url + self.path, data = passParams)
            response = request.json()
            # INSERIR NO FUTURO; PEGAR O ID DO OBJETO CRIADO E DEVOLVAR AO OBJETO PYTHON
            return response

    def retrive(self):
        if(self.hasId() & self.hasKey()):
            self.addOrUpdateParams({"api_key": self.api_key})
            passParams = removeNonesDictionary(self.params)
            request = rq.get(self.url + self.path, data = passParams)
            response = request.json()
            return response
        
    def update(self):
        if(self.hasId() & self.hasKey()):
            self.addOrUpdateParams({"api_key": self.api_key})
            passParams = removeNonesDictionary(self.params)
            request = rq.put(self.url + self.path, data = passParams)
            response = request.json()
            return response

    def delete(self):
        if(self.hasId() & self.hasKey()):
            self.addOrUpdateParams({"api_key": self.api_key})
            passParams = removeNonesDictionary(self.params)
            request = rq.delete(self.url + self.path, data = passParams)
            response = request.json()
            return responseput(

class activities(pipelineDealsObject): 
    def __init__(self):
        super().__init__()
        self.path = "notes"
        self.params = {"api_key": None, "id": None}

class companies(pipelineDealsObject): 
    def __init__(self):
        super().__init__()
        self.path = "companies"
        self.params = {"api_key": None, "id": None}

class customFieldCompanyGroups(pipelineDealsObject): 
    def __init__(self):
        super().__init__()
        self.path = "admin/company_custom_field_groups"
        self.params = {"api_key": None, "id": None}

class customFieldDealsGroups(pipelineDealsObject): 
    def __init__(self): 
        super().__init__()
        self.path = "admin/deal_custom_field_groups"
        self.params = {"api_key": None, "id": None}
        
class customFieldCompanyLabels(pipelineDealsObject): 
    def __init__(self):
        super().__init__()
        self.path = "admin/company_custom_field_labels"
        self.params = {"api_key": None, "id": None}

class customFieldDealsLabels(pipelineDealsObject): 
    def __init__(self):
        super().__init__()
        self.path = "admin/deal_custom_field_labels"
        self.params = {"api_key": None, "id": None}

class customFieldLabelDropdownEntries(pipelineDealsObject): 
    def __init__(self):
        super().__init__()
        self.path = "admin/custom_field_label_dropdown_entries"
        self.params = {"api_key": None, "id": None}

class deals(pipelineDealsObject): 
    def __init__(self):
        super().__init__()
        self.path = "deals"
        self.params = {"api_key": None, "id": None}

class people(pipelineDealsObject): 
    def __init__(self):
        super().__init__()
        self.path = "people"
        self.params = {"api_key": None, "id": None}

class users(pipelineDealsObject): 
    def __init__(self):
        super().__init__()
        self.path = "admin/users"
        self.params = {"api_key": None, "id": None}