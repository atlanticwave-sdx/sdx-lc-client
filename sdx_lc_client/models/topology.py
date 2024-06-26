# coding: utf-8

"""
    SDX LC

    You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: yxin@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Topology(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "id": "str",
        "name": "str",
        "services": "Service",
        "version": "int",
        "model_version": "str",
        "timestamp": "datetime",
        "nodes": "list[Node]",
        "links": "list[Link]",
        "private_attributes": "list[str]",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "services": "services",
        "version": "version",
        "model_version": "model_version",
        "timestamp": "timestamp",
        "nodes": "nodes",
        "links": "links",
        "private_attributes": "private_attributes",
    }

    def __init__(
        self,
        id=None,
        name=None,
        services=None,
        version=None,
        model_version=None,
        timestamp=None,
        nodes=None,
        links=None,
        private_attributes=None,
    ):  # noqa: E501
        """Topology - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._services = None
        self._version = None
        self._model_version = None
        self._timestamp = None
        self._nodes = None
        self._links = None
        self._private_attributes = None
        self.discriminator = None
        self.id = id
        self.name = name
        if services is not None:
            self.services = services
        self.version = version
        if model_version is not None:
            self.model_version = model_version
        self.timestamp = timestamp
        self.nodes = nodes
        self.links = links
        if private_attributes is not None:
            self.private_attributes = private_attributes

    @property
    def id(self):
        """Gets the id of this Topology.  # noqa: E501


        :return: The id of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Topology.


        :param id: The id of this Topology.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Topology.  # noqa: E501


        :return: The name of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Topology.


        :param name: The name of this Topology.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def services(self):
        """Gets the services of this Topology.  # noqa: E501


        :return: The services of this Topology.  # noqa: E501
        :rtype: Service
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Topology.


        :param services: The services of this Topology.  # noqa: E501
        :type: Service
        """

        self._services = services

    @property
    def version(self):
        """Gets the version of this Topology.  # noqa: E501


        :return: The version of this Topology.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Topology.


        :param version: The version of this Topology.  # noqa: E501
        :type: int
        """
        if version is None:
            raise ValueError(
                "Invalid value for `version`, must not be `None`"
            )  # noqa: E501

        self._version = version

    @property
    def model_version(self):
        """Gets the model_version of this Topology.  # noqa: E501


        :return: The model_version of this Topology.  # noqa: E501
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """Sets the model_version of this Topology.


        :param model_version: The model_version of this Topology.  # noqa: E501
        :type: str
        """

        self._model_version = model_version

    @property
    def timestamp(self):
        """Gets the timestamp of this Topology.  # noqa: E501


        :return: The timestamp of this Topology.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Topology.


        :param timestamp: The timestamp of this Topology.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError(
                "Invalid value for `timestamp`, must not be `None`"
            )  # noqa: E501

        self._timestamp = timestamp

    @property
    def nodes(self):
        """Gets the nodes of this Topology.  # noqa: E501


        :return: The nodes of this Topology.  # noqa: E501
        :rtype: list[Node]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this Topology.


        :param nodes: The nodes of this Topology.  # noqa: E501
        :type: list[Node]
        """
        if nodes is None:
            raise ValueError(
                "Invalid value for `nodes`, must not be `None`"
            )  # noqa: E501

        self._nodes = nodes

    @property
    def links(self):
        """Gets the links of this Topology.  # noqa: E501


        :return: The links of this Topology.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Topology.


        :param links: The links of this Topology.  # noqa: E501
        :type: list[Link]
        """
        if links is None:
            raise ValueError(
                "Invalid value for `links`, must not be `None`"
            )  # noqa: E501

        self._links = links

    @property
    def private_attributes(self):
        """Gets the private_attributes of this Topology.  # noqa: E501


        :return: The private_attributes of this Topology.  # noqa: E501
        :rtype: list[str]
        """
        return self._private_attributes

    @private_attributes.setter
    def private_attributes(self, private_attributes):
        """Sets the private_attributes of this Topology.


        :param private_attributes: The private_attributes of this Topology.  # noqa: E501
        :type: list[str]
        """

        self._private_attributes = private_attributes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(Topology, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Topology):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
