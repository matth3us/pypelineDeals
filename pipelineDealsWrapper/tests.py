from pipelineDeals import *
from objects import *
from lists import *
import json

# # Teste da autenticação
# au = pipelineDeals()
# print(au.api_key)
# print(au.app_key)
# print(au.hasApplicationKey())
# print(au.hasKey())
# au.addKey("test-key")
# au.addApplicationKey("test-app-key")
# print(au.api_key)
# print(au.app_key)
# print(au.hasApplicationKey())
# print(au.hasKey())

# # Teste do Retrieve de objeto
# test_id = "117327336" #codent 1000000
# test_api_key = "C0ibjzdk6ZTe7si8QGzp"
# cp = pipelineDealsObject()
# cp.addKey(test_api_key)
# cp.setTypeCompanies()
# cp.addOrUpdateParams({"id": test_id})
# cp.retrive()
# print(cp.params)

# Testar List retornando lista python de objetos 
test_api_key = "C0ibjzdk6ZTe7si8QGzp"
li = pipelineDealsList()
li.addKey(test_api_key)
li.setTypeListUsers()
li.retrieveList()
print(type(li.listOfObjects))
print(len(li.listOfObjects))
print(li.listOfObjects[0].api_key)
print(li.listOfObjects[0].params)

# PARA CONVERTER ESSA LISTA EM PANDAS DATA FRAME: https://stackoverflow.com/questions/20638006/convert-list-of-dictionaries-to-a-pandas-dataframe



# with open('data.json', 'w') as f:
#     json.dump(data, f)

# with open('data.json') as f:
#   data = json.load(f)

# for x in data['entries']:
#   print(x)