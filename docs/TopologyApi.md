# sdx_lc_client.TopologyApi

All URIs are relative to *https://virtserver.swaggerhub.com/SDX-LC/2.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_topology**](TopologyApi.md#add_topology) | **POST** /topology | Send a new topology to SDX-LC
[**delete_topology**](TopologyApi.md#delete_topology) | **DELETE** /topology | Deletes a topology
[**delete_topology_version**](TopologyApi.md#delete_topology_version) | **DELETE** /topology/{version} | Deletes a topology version
[**get_topology**](TopologyApi.md#get_topology) | **GET** /topology | get an existing topology
[**get_topologyby_version**](TopologyApi.md#get_topologyby_version) | **GET** /topology/{version} | Find topology by version
[**topology_version**](TopologyApi.md#topology_version) | **GET** /topology/version | Finds topology version
[**update_topology**](TopologyApi.md#update_topology) | **PUT** /topology | Update an existing topology
[**upload_file**](TopologyApi.md#upload_file) | **POST** /topology/{topology_id}/uploadImage | uploads an topology image

# **add_topology**
> Topology add_topology(body)

Send a new topology to SDX-LC

### Example
```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.TopologyApi()
body = sdx_lc_client.Topology() # Topology | placed for adding a new topology

try:
    # Send a new topology to SDX-LC
    api_response = api_instance.add_topology(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->add_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Topology**](Topology.md)| placed for adding a new topology | 

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topology**
> delete_topology(topology_id)

Deletes a topology

### Example
```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.TopologyApi()
topology_id = 789 # int | ID of topology to delete

try:
    # Deletes a topology
    api_instance.delete_topology(topology_id)
except ApiException as e:
    print("Exception when calling TopologyApi->delete_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_id** | **int**| ID of topology to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topology_version**
> delete_topology_version(topology_id, version)

Deletes a topology version

### Example
```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.TopologyApi()
topology_id = 789 # int | ID of topology to return
version = 789 # int | topology version to delete

try:
    # Deletes a topology version
    api_instance.delete_topology_version(topology_id, version)
except ApiException as e:
    print("Exception when calling TopologyApi->delete_topology_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_id** | **int**| ID of topology to return | 
 **version** | **int**| topology version to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology**
> str get_topology()

get an existing topology

ID of the topology

### Example
```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.TopologyApi()

try:
    # get an existing topology
    api_response = api_instance.get_topology()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_topology: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topologyby_version**
> Topology get_topologyby_version(topology_id, version)

Find topology by version

Returns a single topology

### Example
```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.TopologyApi()
topology_id = 789 # int | ID of topology to return
version = 789 # int | version of topology to return

try:
    # Find topology by version
    api_response = api_instance.get_topologyby_version(topology_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->get_topologyby_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_id** | **int**| ID of topology to return | 
 **version** | **int**| version of topology to return | 

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_version**
> Topology topology_version(topology_id)

Finds topology version

Topology version

### Example
```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.TopologyApi()
topology_id = 'topology_id_example' # str | topology id

try:
    # Finds topology version
    api_response = api_instance.topology_version(topology_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->topology_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_id** | **str**| topology id | 

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topology**
> update_topology(body)

Update an existing topology

ID of topology that needs to be updated. \\\\ The topology update only updates the addition or deletion \\\\ of node, port, link.

### Example
```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.TopologyApi()
body = sdx_lc_client.Topology() # Topology | topology object that needs to be sent to the SDX LC

try:
    # Update an existing topology
    api_instance.update_topology(body)
except ApiException as e:
    print("Exception when calling TopologyApi->update_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Topology**](Topology.md)| topology object that needs to be sent to the SDX LC | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file**
> ApiResponse upload_file(topology_id, body=body)

uploads an topology image

### Example
```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.TopologyApi()
topology_id = 789 # int | ID of topology to update
body = sdx_lc_client.Object() # Object |  (optional)

try:
    # uploads an topology image
    api_response = api_instance.upload_file(topology_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologyApi->upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_id** | **int**| ID of topology to update | 
 **body** | **Object**|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

