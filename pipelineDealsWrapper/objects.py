# por nos testes: apenas parâmetros permitidos para cada; tipos permitidos de parâmetros; parâmetros obrigatórios tem que ser passados;
from authenticator import pipelineDeals

class pipelineDealsObject(pipelineDeals):
    def __init__(self):
        self.path = ""
        self.id = NULL
        self.url = "https://api.pipelinedeals.com/api/v3/"
    
    #def create(self, params):
        #POST
    #def retrive(self, id):
        #GET
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