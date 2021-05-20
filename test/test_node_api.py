# coding: utf-8

"""
    SDX LC

    You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: yxin@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.node_api import NodeApi  # noqa: E501
from swagger_client.rest import ApiException


class TestNodeApi(unittest.TestCase):
    """NodeApi unit test stubs"""

    def setUp(self):
        self.api = NodeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_node(self):
        """Test case for add_node

        add a new node to the topology  # noqa: E501
        """
        pass

    def test_delete_node(self):
        """Test case for delete_node

        Deletes a node  # noqa: E501
        """
        pass

    def test_get_node(self):
        """Test case for get_node

        get an existing node  # noqa: E501
        """
        pass

    def test_update_node(self):
        """Test case for update_node

        Update an existing node  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
