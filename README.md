# pypelineDeals

Python wrapper for the Pipeline Deals API. For mor information on the Pipeline Deals API, see: url

## Quick Start

### Installation

(soon...)

## Basic Usage

There are two basic ways of using the wrapper, lists and objects.

### Lists

There are, for now, twelve types of object lists that can be retrieved with the wrapper:

- Activities
- Companies
- CustomFieldCompanyGroups
- CustomFieldCompanyLabels
- CustomFieldDealsGroups
- CustomFieldDealsLabels
- CustomFieldLabelDropdownEntries
- CustomFieldPeopleGroups
- CustomFieldPeopleLabels
- Deals
- People
- Users

To retrieve them, you must create an instance of the class `pipelineDealsLists` and pass the proper authentication to it, as such:

```python
object_list = pipelineDealsList()
object_list.addKey(api_key)
```

Remember to always store safely your api keys!

After that, you must set the type of object list you want to retrieve and actually retrieve it. If, for instance, you want to retrieve all your companies, you must run the following code:

```
object_list.setTypeListCompanies()
object_list.retriveList()
```

The list of objects will be available in the property `listOfObjects`. It will be in a python list where each object is a instance of the `pipelineDealsObject` class, that will be explained in further details down below.

Every kind of object list of the list above can be retrieve with a method that looks as `setTypeList...`

### Objects

There are, for now, twelve types of object lists that can be retrieved with the wrapper:

- Activities
- Companies
- CustomFieldCompanyGroups
- CustomFieldCompanyLabels
- CustomFieldDealsGroups
- CustomFieldDealsLabels
- CustomFieldLabelDropdownEntries
- CustomFieldPeopleGroups
- CustomFieldPeopleLabels
- Deals
- People
- Users

To interact with them, you'll use a instance of the `pipelineDealsObject` class. If the object was generated from a list, they'll already have the `api key` and the `id` properties filled, but otherwise, they'll be just a blank slate. The properties of an pipeline object will be available in the `params` property of the instance, as a python dictionary. 

#### Create Object

To interact with a blank slate object, you'll need to set its api key and it's `id`, if it has been already created in your pipeline deals database. If you're trying to create a new object, then there won't be an id. So, you can easily create it as such:

```python
properties_object = {...}
pipeline_object = pipelineDealsObject()
pipeline_object.addKey(apiKey)
pipeline_object.setTypeCompanies()
pipeline_object.create(properties_object)
```

The properties of the object must be passed as an dictionary. You can check which properties you must pass to each object in the API documentation. After creating an object, it's pipeline properties will be updated in the `params` property.

#### Retrieve Object

If you just need to retrieve an object properties, you need its id. As such, you'll be able to run the following code:

```python
pipeline_object = pipelineDealsObject()
pipeline_object.addKey(apiKey)
pipeline_object.addId(id_object)
pipeline_object.setTypeCompanies()
pipeline_object.retrieve()
```

The id must preferably be passed as a string, but it can be passed as an integer. The object's pipeline properties will be updated in its `params` property.

#### Update object

You can also pass a dictionary to update an existing object. You'll need an id for that, so you can run a code like this:

```python
properties_object = {...}
pipeline_object = pipelineDealsObject()
pipeline_object.addKey(apiKey)
pipeline_object.addId(id_object)
pipeline_object.setTypeCompanies()
pipeline_object.update(properties_object)
```

After updating an object, it's pipeline properties will be updated in the `params` property.

#### Delete Object

Finally, you can delete an object. You also need an id, as such:

```python
pipeline_object = pipelineDealsObject()
pipeline_object.addKey(apiKey)
pipeline_object.addId(id_object)
pipeline_object.setTypeCompanies()
pipeline_object.delete()
```

For more informations, send me a [linkedin message](https://www.linkedin.com/in/celso-mattheus/).