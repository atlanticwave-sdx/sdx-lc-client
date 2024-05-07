# coding: utf-8

"""
    SDX LC

    You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: yxin@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from sdx_lc_client.api_client import ApiClient


class TopologyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_topology(self, body, **kwargs):  # noqa: E501
        """Send a new topology to SDX-LC  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_topology(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Topology body: placed for adding a new topology (required)
        :return: Topology
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.add_topology_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_topology_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_topology_with_http_info(self, body, **kwargs):  # noqa: E501
        """Send a new topology to SDX-LC  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_topology_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Topology body: placed for adding a new topology (required)
        :return: Topology
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_topology" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `add_topology`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/topology",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Topology",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_topology(self, topology_id, **kwargs):  # noqa: E501
        """Deletes a topology  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_topology(topology_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int topology_id: ID of topology to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_topology_with_http_info(
                topology_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_topology_with_http_info(
                topology_id, **kwargs
            )  # noqa: E501
            return data

    def delete_topology_with_http_info(self, topology_id, **kwargs):  # noqa: E501
        """Deletes a topology  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_topology_with_http_info(topology_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int topology_id: ID of topology to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["topology_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_topology" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'topology_id' is set
        if "topology_id" not in params or params["topology_id"] is None:
            raise ValueError(
                "Missing the required parameter `topology_id` when calling `delete_topology`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "topology_id" in params:
            query_params.append(("topology_id", params["topology_id"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/topology",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_topology_version(self, topology_id, version, **kwargs):  # noqa: E501
        """Deletes a topology version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_topology_version(topology_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int topology_id: ID of topology to return (required)
        :param int version: topology version to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_topology_version_with_http_info(
                topology_id, version, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_topology_version_with_http_info(
                topology_id, version, **kwargs
            )  # noqa: E501
            return data

    def delete_topology_version_with_http_info(
        self, topology_id, version, **kwargs
    ):  # noqa: E501
        """Deletes a topology version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_topology_version_with_http_info(topology_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int topology_id: ID of topology to return (required)
        :param int version: topology version to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["topology_id", "version"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_topology_version" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'topology_id' is set
        if "topology_id" not in params or params["topology_id"] is None:
            raise ValueError(
                "Missing the required parameter `topology_id` when calling `delete_topology_version`"
            )  # noqa: E501
        # verify the required parameter 'version' is set
        if "version" not in params or params["version"] is None:
            raise ValueError(
                "Missing the required parameter `version` when calling `delete_topology_version`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "version" in params:
            path_params["version"] = params["version"]  # noqa: E501

        query_params = []
        if "topology_id" in params:
            query_params.append(("topology_id", params["topology_id"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/topology/{version}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_topology(self, **kwargs):  # noqa: E501
        """get an existing topology  # noqa: E501

        ID of the topology  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_topology(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_topology_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_topology_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_topology_with_http_info(self, **kwargs):  # noqa: E501
        """get an existing topology  # noqa: E501

        ID of the topology  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_topology_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topology" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/topology",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="str",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_topologyby_version(self, topology_id, version, **kwargs):  # noqa: E501
        """Find topology by version  # noqa: E501

        Returns a single topology  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_topologyby_version(topology_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int topology_id: ID of topology to return (required)
        :param int version: version of topology to return (required)
        :return: Topology
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_topologyby_version_with_http_info(
                topology_id, version, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_topologyby_version_with_http_info(
                topology_id, version, **kwargs
            )  # noqa: E501
            return data

    def get_topologyby_version_with_http_info(
        self, topology_id, version, **kwargs
    ):  # noqa: E501
        """Find topology by version  # noqa: E501

        Returns a single topology  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_topologyby_version_with_http_info(topology_id, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int topology_id: ID of topology to return (required)
        :param int version: version of topology to return (required)
        :return: Topology
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["topology_id", "version"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topologyby_version" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'topology_id' is set
        if "topology_id" not in params or params["topology_id"] is None:
            raise ValueError(
                "Missing the required parameter `topology_id` when calling `get_topologyby_version`"
            )  # noqa: E501
        # verify the required parameter 'version' is set
        if "version" not in params or params["version"] is None:
            raise ValueError(
                "Missing the required parameter `version` when calling `get_topologyby_version`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "version" in params:
            path_params["version"] = params["version"]  # noqa: E501

        query_params = []
        if "topology_id" in params:
            query_params.append(("topology_id", params["topology_id"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/topology/{version}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Topology",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def topology_version(self, topology_id, **kwargs):  # noqa: E501
        """Finds topology version  # noqa: E501

        Topology version  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.topology_version(topology_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str topology_id: topology id (required)
        :return: Topology
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.topology_version_with_http_info(
                topology_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.topology_version_with_http_info(
                topology_id, **kwargs
            )  # noqa: E501
            return data

    def topology_version_with_http_info(self, topology_id, **kwargs):  # noqa: E501
        """Finds topology version  # noqa: E501

        Topology version  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.topology_version_with_http_info(topology_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str topology_id: topology id (required)
        :return: Topology
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["topology_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method topology_version" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'topology_id' is set
        if "topology_id" not in params or params["topology_id"] is None:
            raise ValueError(
                "Missing the required parameter `topology_id` when calling `topology_version`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "topology_id" in params:
            query_params.append(("topology_id", params["topology_id"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/topology/version",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="Topology",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_topology(self, body, **kwargs):  # noqa: E501
        """Update an existing topology  # noqa: E501

        ID of topology that needs to be updated. \\\\ The topology update only updates the addition or deletion \\\\ of node, port, link.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_topology(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Topology body: topology object that needs to be sent to the SDX LC (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_topology_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_topology_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_topology_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update an existing topology  # noqa: E501

        ID of topology that needs to be updated. \\\\ The topology update only updates the addition or deletion \\\\ of node, port, link.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_topology_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Topology body: topology object that needs to be sent to the SDX LC (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_topology" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `update_topology`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/topology",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def upload_file(self, topology_id, **kwargs):  # noqa: E501
        """uploads an topology image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_file(topology_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int topology_id: ID of topology to update (required)
        :param Object body:
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.upload_file_with_http_info(topology_id, **kwargs)  # noqa: E501
        else:
            (data) = self.upload_file_with_http_info(
                topology_id, **kwargs
            )  # noqa: E501
            return data

    def upload_file_with_http_info(self, topology_id, **kwargs):  # noqa: E501
        """uploads an topology image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_file_with_http_info(topology_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int topology_id: ID of topology to update (required)
        :param Object body:
        :return: ApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["topology_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'topology_id' is set
        if "topology_id" not in params or params["topology_id"] is None:
            raise ValueError(
                "Missing the required parameter `topology_id` when calling `upload_file`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "topology_id" in params:
            path_params["topology_id"] = params["topology_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/octet-stream"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/topology/{topology_id}/uploadImage",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ApiResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
