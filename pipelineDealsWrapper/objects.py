# por nos testes: apenas parâmetros permitidos para cada; tipos permitidos de parâmetros; parâmetros obrigatórios tem que ser passados;
import requests as rq
from pipelineDeals import pipelineDeals

def removeNonesDictionary(dictio):
    filtered = dict(filter(lambda item: item[1] is not None, dictio.items()))
    return filtered

class pipelineDealsObject(pipelineDeals):
    def __init__(self):
        super().__init__()
        self.url = "https://api.pipelinedeals.com/api/v3/"
        self.id = None
        self.path = None
        self.params = None

    def clearType(self):
        self.path = None
        self.params = None

    def setTypeActivities(self):
        self.path = "notes"
        self.params = {"api_key": self.api_key, "id": None}
    
    def setTypeCompanies(self): 
        self.path = "companies"
        self.params = {"api_key": self.api_key, "id": None}

    def setTypeCustomFieldCompanyGroups(self): 
        self.path = "admin/company_custom_field_groups"
        self.params = {"api_key": self.api_key, "id": None}

    def setTypeCustomFieldCompanyLabels(self): 
        self.path = "admin/company_custom_field_labels"
        self.params = {"api_key": self.api_key, "id": None}

    def setTypeCustomFieldDealsGroups(self): 
        self.path = "admin/deal_custom_field_groups"
        self.params = {"api_key": self.api_key, "id": None}

    def setTypeCustomFieldDealsLabels(self): 
        self.path = "admin/deal_custom_field_labels"
        self.params = {"api_key": self.api_key, "id": None}
    
    def setTypeCustomFieldPeopleGroups(self): 
        self.path = "admin/person_custom_field_groups"
        self.params = {"api_key": self.api_key, "id": None}
    
    def setTypeCustomFieldPeopleLabels(self): 
        self.path = "admin/person_custom_field_labels"
        self.params = {"api_key": self.api_key, "id": None}

    def setTypeCustomFieldLabelDropdownEntries(self): 
        self.path = "admin/custom_field_label_dropdown_entries"
        self.params = {"api_key": self.api_key, "id": None}

    def setTypeDeals(self): 
        self.path = "deals"
        self.params = {"api_key": self.api_key, "id": None}

    def setTypePeople(self):
        self.path = "people"
        self.params = {"api_key": self.api_key, "id": None}

    def setTypeUsers(self): 
        self.path = "admin/users"
        self.params = {"api_key": self.api_key, "id": None}

    def addOrUpdateParams(self, newValuesDictionary):
        self.params.update(newValuesDictionary)
    
    def hasId(self):
        return self.id is not None
    
    def addId(self, id):
        self.id = id
    
    def create(self, createParams):
        if(self.hasKey()):
            passUrl = self.url + self.path + ".json?api_key=" + self.api_key + '&check_for_duplicates=true'
            request = rq.post(passUrl, json = createParams)
            print(request.status_code)
            self.addOrUpdateParams(request.json())
            self.id = self.params['id']
        else:
            print("No API Key provided.")

    def retrieve(self):
        if(self.hasId() & self.hasKey()):
            self.addOrUpdateParams({"id": str(self.id)})
            self.addOrUpdateParams({"api_key": self.api_key})
            passParams = removeNonesDictionary(self.params)
            request = rq.get(self.url + self.path, data = passParams)
            response = request.json()
            self.addOrUpdateParams(response)
        elif not (self.hasId()):
            print("No id provided.")
        else:
            print("No API Key provided.")
        
    def update(self, updateParams):
        if(self.hasId() & self.hasKey()):
            passUrl = self.url + self.path + "/" + str(self.id) + ".json?api_key=" + self.api_key
            passHeaders = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
            request = rq.put(passUrl, json = updateParams, headers = passHeaders)
            print(request.status_code)
            self.addOrUpdateParams(request.json())
        elif not (self.hasId()):
            print("No id provided.")
        else:
            print("No API Key provided.")

    def delete(self):
        if(self.hasId() & self.hasKey()):
            passUrl = self.url + self.path + "/" + str(self.id) + ".json?api_key=" + self.api_key
            request = rq.delete(passUrl)
            print(request.status_code)
            return response
        elif not (self.hasId()):
            print("No id provided.")
        else:
            print("No API Key provided.")