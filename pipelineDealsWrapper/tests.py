from objects import *


au = pipelineDeals()
print(au.api_key)
print(au.app_key)
print(au.hasApplicationKey())
print(au.hasKey())
au.addKey("test-key")
au.addApplicationKey("test-app-key")
print(au.api_key)
print(au.app_key)
print(au.hasApplicationKey())
print(au.hasKey())