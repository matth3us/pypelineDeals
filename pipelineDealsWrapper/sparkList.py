import requests as rq
import json as js
import pipelineDeals as pd
import objects as ob
from pyspark.sql import *
from pyspark.sql.functions import expr
from pyspark.sql.types import LongType

class pipelineDealsList(pd.pipelineDeals):
    def __init__(self):
        super().__init__()
        self.path = None
        self.url = "https://api.pipelinedeals.com/api/v3/"
        self.objectType = None
        self.totalPages = 1
        self.listOfObjects = None
    
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
    
    def retrievePageList(page):
            passParamsSpark = {"api_key": self.api_key, "page": page}
            attempts = 0
            success = False
            while status != True and attempts < 50:
                request = rq.get(self.url + self.path, data = passParams)
                response = request.json()["entries"]
                attempts += 1
                status = response.status_code
                if status != 200:
                    time.sleep(Math.exp(attempts)
                    
                    # retry
                    continue
                
                success = True
            
            if attempts == 50:
                print('Daily Limit Reached')
                
            return Row('page', 'entry')(page, response)
    
    def retrieveList(self):
        if(self.hasObjectType() & self.hasKey()):
            passParams = {"api_key": self.api_key, "page": 1}    
            request = rq.get(self.url + self.path, data = passParams)
            response = request.json()
            self.totalPages = response['pagination'].pages
            self.listOfObjects = spark.sql('select 1 as page').\
                withColumn("entries", expr("json(" + response['entries'] + ")"))
            
            listOfEntries = spark.sql('select explode(sequence(2,' + totalPages + ')) as page')
            listOfEntries = listOfEntries.select("page", retrievePageList("page").alias("entries"))
            self.listOfObjects = self.listOfObjects.union(listOfEntries)

        if not (self.hasObjectType()):
            print("No object type defined.")
        if not (self.hasKey()):
            print("No API Key provided.")