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
from sdx_lc_client.api.topology_api import TopologyApi  # noqa: E501
from sdx_lc_client.rest import ApiException


class TestTopologyApi(unittest.TestCase):
    """TopologyApi unit test stubs"""

    def setUp(self):
        self.api = TopologyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_topology(self):
        """Test case for add_topology
        Send a new topology to SDX-LC  # noqa: E501
        """
        p1 = sdx_lc_client.Port(
            id="n1:p1", name="p1", short_name="eth1", node="n1", status="UP"
        )
        p2 = sdx_lc_client.Port(
            id="n2:p1", name="p2", short_name="eth2", node="n2", status="UP"
        )
        ps = []
        ps.append(p1)
        ps.append(p2)
        lt = sdx_lc_client.Location(address="miami")
        node = sdx_lc_client.Node(id="node1", name="node1", location=lt, ports=ps)
        ns = []
        ns.append(node)

        link = sdx_lc_client.Link(id="link1", name="link1", ports=ps)
        ls = []
        ls.append(link)

        timestmp = "2021-06-24T04:56:07+00:00"
        topology_body = sdx_lc_client.Topology(
            id="topology1",
            name="topology1",
            nodes=ns,
            links=ls,
            version=1,
            timestamp=timestmp,
        )

        try:
            # create a connection
            # logger.warning(connection_body)
            api_response = self.api.add_topology(topology_body)
            print(api_response)
            # logger.warning(api_response)
        except ApiException as e:
            print(e)
            # logger.warning("Exception when calling ConnectionApi->place_experiment: %s\n" % e)

    def test_delete_topology(self):
        """Test case for delete_topology

        Deletes a topology  # noqa: E501
        """
        pass

    def test_delete_topology_version(self):
        """Test case for delete_topology_version

        Deletes a topology version  # noqa: E501
        """
        pass

    def test_get_topology(self):
        """Test case for get_topology

        get an existing topology  # noqa: E501
        """
        pass

    def test_get_topologyby_version(self):
        """Test case for get_topologyby_version

        Find topology by version  # noqa: E501
        """
        pass

    def test_topology_version(self):
        """Test case for topology_version

        Finds topology version  # noqa: E501
        """
        pass

    def test_update_topology(self):
        """Test case for update_topology

        Update an existing topology  # noqa: E501
        """
        pass

    def test_upload_file(self):
        """Test case for upload_file

        uploads an topology image  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
