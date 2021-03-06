# swagger_client.NodeApi

All URIs are relative to *https://virtserver.swaggerhub.com/SDX-LC/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_node**](NodeApi.md#add_node) | **POST** /node | add a new node to the topology
[**delete_node**](NodeApi.md#delete_node) | **DELETE** /node | Deletes a node
[**get_node**](NodeApi.md#get_node) | **GET** /node | get an existing node
[**update_node**](NodeApi.md#update_node) | **PUT** /node | Update an existing node

# **add_node**
> Node add_node(body)

add a new node to the topology

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()
body = swagger_client.Node() # Node | node object that needs to be sent to the SDX LC

try:
    # add a new node to the topology
    api_response = api_instance.add_node(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeApi->add_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Node**](Node.md)| node object that needs to be sent to the SDX LC | 

### Return type

[**Node**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_node**
> delete_node(node_id, api_key=api_key)

Deletes a node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()
node_id = 789 # int | ID of node to delete
api_key = 'api_key_example' # str |  (optional)

try:
    # Deletes a node
    api_instance.delete_node(node_id, api_key=api_key)
except ApiException as e:
    print("Exception when calling NodeApi->delete_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**| ID of node to delete | 
 **api_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node**
> get_node()

get an existing node

ID of the node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()

try:
    # get an existing node
    api_instance.get_node()
except ApiException as e:
    print("Exception when calling NodeApi->get_node: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node**
> update_node(body)

Update an existing node

ID of node that needs to be updated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NodeApi()
body = swagger_client.Node() # Node | node object that needs to be sent to the SDX LC

try:
    # Update an existing node
    api_instance.update_node(body)
except ApiException as e:
    print("Exception when calling NodeApi->update_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Node**](Node.md)| node object that needs to be sent to the SDX LC | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

