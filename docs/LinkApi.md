# sdx_lc_client.LinkApi

All URIs are relative to *https://virtserver.swaggerhub.com/SDX-LC/2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_link**](LinkApi.md#add_link) | **POST** /link | add a new link to the topology
[**delete_link**](LinkApi.md#delete_link) | **DELETE** /link | Deletes a link
[**get_link**](LinkApi.md#get_link) | **GET** /link | get an existing link
[**update_link**](LinkApi.md#update_link) | **PUT** /link | Update an existing link

# **add_link**
> add_link(body)

add a new link to the topology

### Example
```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.LinkApi()
body = sdx_lc_client.Link() # Link | link object that needs to be sent to the SDX LC

try:
    # add a new link to the topology
    api_instance.add_link(body)
except ApiException as e:
    print("Exception when calling LinkApi->add_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Link**](Link.md)| link object that needs to be sent to the SDX LC | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_link**
> delete_link(node_id)

Deletes a link

### Example
```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.LinkApi()
node_id = 789 # int | ID of link to delete

try:
    # Deletes a link
    api_instance.delete_link(node_id)
except ApiException as e:
    print("Exception when calling LinkApi->delete_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **int**| ID of link to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link**
> get_link()

get an existing link

ID of the link

### Example
```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.LinkApi()

try:
    # get an existing link
    api_instance.get_link()
except ApiException as e:
    print("Exception when calling LinkApi->get_link: %s\n" % e)
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

# **update_link**
> update_link(body)

Update an existing link

ID of link that needs to be updated.

### Example
```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.LinkApi()
body = sdx_lc_client.Link() # Link | link object that needs to be sent to the SDX LC

try:
    # Update an existing link
    api_instance.update_link(body)
except ApiException as e:
    print("Exception when calling LinkApi->update_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Link**](Link.md)| link object that needs to be sent to the SDX LC | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

