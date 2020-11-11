import requests as rq
import json as js
from pipelineDeals import pipelineDeals
from objects import pipelineDealsObject
from pyspark.sql import Row
from pyspark.sql.types import *
from pyspark.sql.functions import expr, col, lit, array

class pipelineDealsList(pipelineDeals):
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

    def setTypeListCustomFieldPeopleGroups(self): 
        self.path = "admin/person_custom_field_groups"
        self.objectType = "customfieldpeoplegroups"

    def setTypeListCustomFieldPeopleLabels(self): 
        self.path = "admin/person_custom_field_labels"
        self.objectType = "customfieldpeoplelabels"

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
        pipelineObject = pipelineDealsObject()
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
        if(self.objectType == "customfieldpeoplegroups"): 
            pipelineObject.setTypeCustomFieldPeopleGroups()
        if(self.objectType == "customfieldpeoplelabels"): 
            pipelineObject.setTypeCustomFieldPeopleLabels()
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
            totalPages = response['pagination']['pages']
            firstPage = response['entries']
            for entry in firstPage:
                self.listOfObjects.append(self.createObject(entry))
            if totalPages == 1: return
            for p in range(2, totalPages+1):
                passParams['page'] = p
                request = rq.get(self.url + self.path, data = passParams)
                response = request.json()['entries']
                for entry in response:
                    self.listOfObjects.append(self.createObject(entry))
        if not (self.hasObjectType()):
            print("No object type defined.")
        if not (self.hasKey()):
            print("No API Key provided.")

    def retrieveSparkList(self):
        def retrieveSparkPageDataFrame(page, api_key, url, path):
            #Incluir exceções para caso de erro na API
            fullPath = url + path
            response = rq.get(fullPath, data = {'api_key':api_key, 'page': page}).json()['entries']
            return(response)

        retrieveSparkPageDataFrameUdf = udf(retrieveSparkPageDataFrame, ArrayType(StringType()))

        if(self.hasKey()):
            passParams = {"api_key": self.api_key, "page": 1}
            request = rq.get(self.url + self.path, data = passParams)
            response = request.json()
            self.totalPages = string(response['pagination'].pages)

            # Criar DF spark com as entries
            self.listOfObjects = spark.sql('select explode(sequence(1,' + self.totalPages + ')) as page')\
                .withColumn('page', expr('string(page)'))\
                .withColumn('pageEntries', retrieveSparkPageDataFrameUdf(col('page'), lit(passParams['api_key']), lit(self.url), lit(self.path)))

        if not (self.hasObjectType()):
            print("No object type defined.")
        if not (self.hasKey()):
            print("No API Key provided.")