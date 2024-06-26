# sdx_lc_client
You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/). 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 2.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import sdx_lc_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sdx_lc_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import sdx_lc_client
from sdx_lc_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sdx_lc_client.ConnectionApi(sdx_lc_client.ApiClient(configuration))
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of the connection that needs to be deleted

try:
    # Delete connection order by ID
    api_instance.delete_connection(connection_id)
except ApiException as e:
    print("Exception when calling ConnectionApi->delete_connection: %s\n" % e)

# create an instance of the API class
api_instance = sdx_lc_client.ConnectionApi(sdx_lc_client.ApiClient(configuration))
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | ID of connection that needs to be fetched

try:
    # Find connection by ID
    api_response = api_instance.getconnection_by_id(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->getconnection_by_id: %s\n" % e)

# create an instance of the API class
api_instance = sdx_lc_client.ConnectionApi(sdx_lc_client.ApiClient(configuration))
body = sdx_lc_client.Connection() # Connection | order placed for creating a connection

try:
    # Place an connection request from the SDX-Controller
    api_response = api_instance.place_connection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->place_connection: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/SDX-LC/2.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConnectionApi* | [**delete_connection**](docs/ConnectionApi.md#delete_connection) | **DELETE** /connection/{connection_id} | Delete connection order by ID
*ConnectionApi* | [**getconnection_by_id**](docs/ConnectionApi.md#getconnection_by_id) | **GET** /connection/{connection_id} | Find connection by ID
*ConnectionApi* | [**place_connection**](docs/ConnectionApi.md#place_connection) | **POST** /conection | Place an connection request from the SDX-Controller
*LinkApi* | [**add_link**](docs/LinkApi.md#add_link) | **POST** /link | add a new link to the topology
*LinkApi* | [**delete_link**](docs/LinkApi.md#delete_link) | **DELETE** /link | Deletes a link
*LinkApi* | [**get_link**](docs/LinkApi.md#get_link) | **GET** /link | get an existing link
*LinkApi* | [**update_link**](docs/LinkApi.md#update_link) | **PUT** /link | Update an existing link
*NodeApi* | [**add_node**](docs/NodeApi.md#add_node) | **POST** /node | add a new node to the topology
*NodeApi* | [**delete_node**](docs/NodeApi.md#delete_node) | **DELETE** /node | Deletes a node
*NodeApi* | [**get_node**](docs/NodeApi.md#get_node) | **GET** /node | get an existing node
*NodeApi* | [**update_node**](docs/NodeApi.md#update_node) | **PUT** /node | Update an existing node
*TopologyApi* | [**add_topology**](docs/TopologyApi.md#add_topology) | **POST** /topology | Send a new topology to SDX-LC
*TopologyApi* | [**delete_topology**](docs/TopologyApi.md#delete_topology) | **DELETE** /topology | Deletes a topology
*TopologyApi* | [**delete_topology_version**](docs/TopologyApi.md#delete_topology_version) | **DELETE** /topology/{version} | Deletes a topology version
*TopologyApi* | [**get_topology**](docs/TopologyApi.md#get_topology) | **GET** /topology | get an existing topology
*TopologyApi* | [**get_topologyby_version**](docs/TopologyApi.md#get_topologyby_version) | **GET** /topology/{version} | Find topology by version
*TopologyApi* | [**topology_version**](docs/TopologyApi.md#topology_version) | **GET** /topology/version | Finds topology version
*TopologyApi* | [**update_topology**](docs/TopologyApi.md#update_topology) | **PUT** /topology | Update an existing topology
*TopologyApi* | [**upload_file**](docs/TopologyApi.md#upload_file) | **POST** /topology/{topology_id}/uploadImage | uploads an topology image
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /user | Create user
*UserApi* | [**create_users_with_array_input**](docs/UserApi.md#create_users_with_array_input) | **POST** /user/createWithArray | Creates list of users with given input array
*UserApi* | [**create_users_with_list_input**](docs/UserApi.md#create_users_with_list_input) | **POST** /user/createWithList | Creates list of users with given input array
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /user/{username} | Delete user
*UserApi* | [**get_user_by_name**](docs/UserApi.md#get_user_by_name) | **GET** /user/{username} | Get user by user name
*UserApi* | [**login_user**](docs/UserApi.md#login_user) | **GET** /user/login | Logs user into the system
*UserApi* | [**logout_user**](docs/UserApi.md#logout_user) | **GET** /user/logout | Logs out current logged in user session
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /user/{username} | Updated user

## Documentation For Models

 - [ApiResponse](docs/ApiResponse.md)
 - [Connection](docs/Connection.md)
 - [Link](docs/Link.md)
 - [LinkMeasurementPeriod](docs/LinkMeasurementPeriod.md)
 - [Location](docs/Location.md)
 - [Node](docs/Node.md)
 - [Port](docs/Port.md)
 - [Service](docs/Service.md)
 - [Topology](docs/Topology.md)
 - [User](docs/User.md)

## Documentation For Authorization

 All endpoints do not require authorization.


## Author

yxin@renci.org
