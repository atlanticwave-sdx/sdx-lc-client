# coding: utf-8

"""
    SDX LC

    You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: yxin@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import sdx_lc_client
from sdx_lc_client.api.connection_api import ConnectionApi  # noqa: E501
from sdx_lc_client.rest import ApiException


class TestConnectionApi(unittest.TestCase):
    """ConnectionApi unit test stubs"""

    def setUp(self):
        self.api = ConnectionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_connection(self):
        """Test case for delete_connection

        Delete connection order by ID  # noqa: E501
        """
        pass

    def test_getconnection_by_id(self):
        """Test case for getconnection_by_id

        Find connection by ID  # noqa: E501
        """
        pass

    def test_place_connection(self):
        """Test case for place_connection

        Place an connection request from the SDX-Controller  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
