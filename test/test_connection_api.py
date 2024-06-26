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
        p1 = sdx_lc_client.Port(
            id="n1:p1", name="p1", short_name="eth1", node="n1", status="UP"
        )
        p2 = sdx_lc_client.Port(
            id="n2:p1", name="p2", short_name="eth2", node="n2", status="UP"
        )
        timestmp = "2021-06-24T00:05:23+04:00"
        connection_body = sdx_lc_client.Connection(
            id="test1",
            name="test1",
            ingress_port=p1,
            egress_port=p2,
            start_time=timestmp,
            end_time=timestmp,
        )
        try:
            # create a connection
            # logger.warning(connection_body)
            api_response = self.api.place_connection(connection_body)
            print(api_response)
            # logger.warning(api_response)
        except ApiException as e:
            print(e)
            # logger.warning("Exception when calling ConnectionApi->place_experiment: %s\n" % e)


if __name__ == "__main__":
    unittest.main()
