# swagger_client.TopologyApi

All URIs are relative to *https://virtserver.swaggerhub.com/YufengXin/SDX-LC/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_topology**](TopologyApi.md#add_topology) | **POST** /topology | Send a new topology to SDX-LC
[**delete_topology**](TopologyApi.md#delete_topology) | **DELETE** /topology | Deletes a topology
[**delete_topology_version**](TopologyApi.md#delete_topology_version) | **DELETE** /topology/{version} | Deletes a topology version
[**get_topology**](TopologyApi.md#get_topology) | **GET** /topology | get an existing topology
[**get_topologyby_version**](TopologyApi.md#get_topologyby_version) | **GET** /topology/{version} | Find topology by version
[**topology_version**](TopologyApi.md#topology_version) | **GET** /topology/version | Finds topology version
[**update_node**](TopologyApi.md#update_node) | **PUT** /node | Update an existing node
[**update_topology**](TopologyApi.md#update_topology) | **PUT** /topology | Update an existing topology
[**upload_file**](TopologyApi.md#upload_file) | **POST** /topology/{topologyId}/uploadImage | uploads an topology image

# **add_topology**
> add_topology(body)

Send a new topology to SDX-LC

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: topology_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TopologyApi(swagger_client.ApiClient(configuration))
body = swagger_client.Topology() # Topology | topology object that needs to be sent to the SDX LC

try:
    # Send a new topology to SDX-LC
    api_instance.add_topology(body)
except ApiException as e:
    print("Exception when calling TopologyApi->add_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Topology**](Topology.md)| topology object that needs to be sent to the SDX LC | 

### Return type

void (empty response body)

### Authorization

[topology_auth](../README.md#topology_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topology**
> delete_topology(topology_id, api_key=api_key)

Deletes a topology

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: topology_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TopologyApi(swagger_client.ApiClient(configuration))
topology_id = 789 # int | ID of topology to delete
api_key = 'api_key_example' # str |  (optional)

try:
    # Deletes a topology
    api_instance.delete_topology(topology_id, api_key=api_key)
except ApiException as e:
    print("Exception when calling TopologyApi->delete_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_id** | **int**| ID of topology to delete | 
 **api_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[topology_auth](../README.md#topology_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_topology_version**
> delete_topology_version(topology_id, version, api_key=api_key)

Deletes a topology version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: topology_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TopologyApi(swagger_client.ApiClient(configuration))
topology_id = 789 # int | ID of topology to return
version = 789 # int | topology version to delete
api_key = 'api_key_example' # str |  (optional)

try:
    # Deletes a topology version
    api_instance.delete_topology_version(topology_id, version, api_key=api_key)
except ApiException as e:
    print("Exception when calling TopologyApi->delete_topology_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topology_id** | **int**| ID of topology to return | 
 **version** | **int**| topology version to delete | 
 **api_key** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[topology_auth](../README.md#topology_auth)

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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TopologyApi()

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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TopologyApi(swagger_client.ApiClient(configuration))
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

[api_key](../README.md#api_key)

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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: topology_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TopologyApi(swagger_client.ApiClient(configuration))
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

[topology_auth](../README.md#topology_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

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

# Configure OAuth2 access token for authorization: topology_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TopologyApi(swagger_client.ApiClient(configuration))
body = swagger_client.Node() # Node | node object that needs to be sent to the SDX LC

try:
    # Update an existing node
    api_instance.update_node(body)
except ApiException as e:
    print("Exception when calling TopologyApi->update_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Node**](Node.md)| node object that needs to be sent to the SDX LC | 

### Return type

void (empty response body)

### Authorization

[topology_auth](../README.md#topology_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_topology**
> update_topology(body)

Update an existing topology

ID of topology that needs to be updated. \\\\ The topology update only updates the addition or deletion \\\\ of node, port, link.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: topology_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TopologyApi(swagger_client.ApiClient(configuration))
body = swagger_client.Topology() # Topology | topology object that needs to be sent to the SDX LC

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

[topology_auth](../README.md#topology_auth)

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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: topology_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.TopologyApi(swagger_client.ApiClient(configuration))
topology_id = 789 # int | ID of topology to update
body = swagger_client.Object() # Object |  (optional)

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

[topology_auth](../README.md#topology_auth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

