import requests as rq
import json as js
import pipelineDeals as pd
import objects as ob

class pipelineDealsList(pd.pipelineDeals):
    def __init__(self):
        super().__init__()
        self.path = None
        self.url = "https://api.pipelinedeals.com/api/v3/"
        self.objectType = None
        self.listOfObjects = []
        self.totalPages = 1
    
    def setTypeListActivities(self):
        self.path = "notes"
        self.objectType = "activities"

    def setTypeListCompanies(self):
        self.path = "companies"
        self.objectType = "companies"

    def setTypeListCustomFieldCompanyGroups(self): 
        self.path = "admin/company_custom_field_groups"
        self.objectType = "customfieldcompanygroups"

    def setTypeListCustomFieldCompanyLabels(self): 
        self.path = "admin/company_custom_field_labels"
        self.objectType = "customfieldcompanylabels"

    def setTypeListCustomFieldDealsGroups(self): 
        self.path = "admin/deal_custom_field_groups"
        self.objectType = "customfielddealsgroups"

    def setTypeListCustomFieldDealsLabels(self): 
        self.path = "admin/deal_custom_field_labels"
        self.objectType = "customfielddealslabels"

    def setTypeListCustomFieldLabelDropdownEntries(self): 
        self.path = "admin/custom_field_label_dropdown_entries"
        self.objectType = "customfieldlabeldropdownentries"

    def setTypeListDeals(self): 
        self.path = "deals"
        self.objectType = "deals"

    def setTypeListPeople(self): 
        self.path = "people"
        self.objectType = "people"

    def setTypeListUsers(self):
        self.path = "admin/users"
        self.objectType = "users"

    def hasObjectType(self):
        return self.objectType is not None

    def createObject(self, api_response_entry):
        pipelineObject = ob.pipelineDealsObject()
        keyToObject = self.api_key
        pipelineObject.addKey(keyToObject)
        if(self.objectType == "activities"):
            pipelineObject.setTypeActivities()
        if(self.objectType == "companies"): 
            pipelineObject.setTypeCompanies()
        if(self.objectType == "customfieldcompanygroups"): 
            pipelineObject.setTypeCustomFieldCompanyGroups()
        if(self.objectType == "customfieldcompanylabels"): 
            pipelineObject.setTypeCustomFieldCompanyLabels()
        if(self.objectType == "customfielddealsgroups"): 
            pipelineObject.setTypeCustomFieldDealsGroups()
        if(self.objectType == "customfielddealslabels"): 
            pipelineObject.setTypeCustomFieldDealsLabels()
        if(self.objectType == "customfieldlabeldropdownentries"): 
            pipelineObject.setTypeCustomFieldLabelDropdownEntries()
        if(self.objectType == "deals"): 
            pipelineObject.setTypeDeals()
        if(self.objectType == "people"): 
            pipelineObject.setTypePeople()
        if(self.objectType == "users"): 
            pipelineObject.setTypeUsers()
        pipelineObject.addOrUpdateParams(api_response_entry)
        return pipelineObject
    
    def retrieveList(self):
        if(self.hasObjectType() & self.hasKey()):
            passParams = {"api_key": self.api_key, "page": 1}    
            request = rq.get(self.url + self.path, data = passParams)
            response = request.json()
            totalPages = response['pagination'].pages
            for entry in response['entries']:
                self.listOfObjects.append(self.createObject(entry))
            #Continuação se houver mais páginas
            while(totalPages <=  self.totalPages):
                passParams.page = passParams.page + 1
                request = rq.get(self.url + self.path, data = passParams)
                response = request.json()
                for entry in response['entries']:
                    self.listOfObjects.append(self.createObject(entry))
                self.totalPages = self.totalPages + 1
        if not (self.hasObjectType()):
            print("No object type defined.")
        if not (self.hasKey()):
            print("No API Key provided.")