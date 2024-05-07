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
from sdx_lc_client.api.node_api import NodeApi  # noqa: E501
from sdx_lc_client.rest import ApiException


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
        p1 = sdx_lc_client.Port(
            id="n1:p1", name="p1", short_name="eth1", node="n1", status="UP"
        )
        p2 = sdx_lc_client.Port(
            id="n2:p1", name="p2", short_name="eth2", node="n2", status="UP"
        )
        ps = []
        ps.append(p1)
        # ps.append(p2)
        lt = sdx_lc_client.Location(
            address="miami", latitude=-28.51107891831147, longitude=-79.57947854792273
        )
        node_body = sdx_lc_client.Node(id="test1", name="test1", location=lt, ports=ps)
        try:
            # create a connection
            # logger.warning(connection_body)
            api_response = self.api.add_node(node_body)
            print(api_response)
            # logger.warning(api_response)
        except ApiException as e:
            print(e)
            # logger.warning("Exception when calling ConnectionApi->place_experiment: %s\n" % e)
            return False

        return True

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


if __name__ == "__main__":
    unittest.main()
