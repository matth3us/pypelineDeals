# por nos testes: apenas parâmetros permitidos para cada; tipos permitidos de parâmetros; parâmetros obrigatórios tem que ser passados;
import requests as rq
from authenticator import pipelineDeals

def returnJsonResponseIfAvailable(request):
    if(request.raise_for_status()):
        response = {"response": None, "status": request.status_code}
        return(response)
    else:
        response = {"response": request.json(), "status": request.status_code}
        return(response)

class pipelineDealsObject(pipelineDeals):
    def __init__(self):
        self.path = ""
        self.id = None
        self.url = "https://api.pipelinedeals.com/api/v3/"
    
    def hasId(self):
        return self.id is not None

    def create(self, params):
        if(self.hasId() & self.hasKey()):
            params.api_key = self.api_key
            request = rq.post(self.path, data = params)
            response = returnJsonResponseIfAvailable(request)
            return response

    def retrive(self, id):
        if(self.hasId() & self.hasKey()):
            params.api_key = self.api_key
            request = rq.get(self.path, data = params)
            response = returnJsonResponseIfAvailable(request)
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
        self.path = "companies"

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