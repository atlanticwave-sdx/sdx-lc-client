# swagger_client.ConnectionApi

All URIs are relative to *https://virtserver.swaggerhub.com/SDX-LC/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_connection**](ConnectionApi.md#delete_connection) | **DELETE** /connection/{connectionId} | Delete connection order by ID
[**getconnection_by_id**](ConnectionApi.md#getconnection_by_id) | **GET** /connection/{connectionId} | Find connection by ID
[**place_connection**](ConnectionApi.md#place_connection) | **POST** /conection | Place an connection request from the SDX-Controller

# **delete_connection**
> delete_connection(connection_id)

Delete connection order by ID

delete a connection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
connection_id = 789 # int | ID of the connection that needs to be deleted

try:
    # Delete connection order by ID
    api_instance.delete_connection(connection_id)
except ApiException as e:
    print("Exception when calling ConnectionApi->delete_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **int**| ID of the connection that needs to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getconnection_by_id**
> Connection getconnection_by_id(connection_id)

Find connection by ID

connection details

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
connection_id = 789 # int | ID of connection that needs to be fetched

try:
    # Find connection by ID
    api_response = api_instance.getconnection_by_id(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->getconnection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **int**| ID of connection that needs to be fetched | 

### Return type

[**Connection**](Connection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_connection**
> Connection place_connection(body)

Place an connection request from the SDX-Controller

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConnectionApi()
body = swagger_client.Connection() # Connection | order placed for creating a connection

try:
    # Place an connection request from the SDX-Controller
    api_response = api_instance.place_connection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->place_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Connection**](Connection.md)| order placed for creating a connection | 

### Return type

[**Connection**](Connection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

