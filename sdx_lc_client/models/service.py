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


class Service(object):
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
        "l2vpn_ptp": "object",
        "l2vpn_ptmp": "object",
        "monitoring_capability": "str",
        "owner": "str",
        "private_attributes": "list[str]",
        "provisioning_system": "str",
        "provisioning_url": "str",
        "vendor": "list[str]",
    }

    attribute_map = {
        "l2vpn_ptp": "l2vpn-ptp",
        "l2vpn_ptmp": "l2vpn-ptmp",
        "monitoring_capability": "monitoring_capability",
        "owner": "owner",
        "private_attributes": "private_attributes",
        "provisioning_system": "provisioning_system",
        "provisioning_url": "provisioning_url",
        "vendor": "vendor",
    }

    def __init__(
        self,
        l2vpn_ptp=None,
        l2vpn_ptmp=None,
        monitoring_capability=None,
        owner=None,
        private_attributes=None,
        provisioning_system=None,
        provisioning_url=None,
        vendor=None,
    ):  # noqa: E501
        """Service - a model defined in Swagger"""  # noqa: E501
        self._l2vpn_ptp = None
        self._l2vpn_ptmp = None
        self._monitoring_capability = None
        self._owner = None
        self._private_attributes = None
        self._provisioning_system = None
        self._provisioning_url = None
        self._vendor = None
        self.discriminator = None
        if l2vpn_ptp is not None:
            self.l2vpn_ptp = l2vpn_ptp
        if l2vpn_ptmp is not None:
            self.l2vpn_ptmp = l2vpn_ptmp
        if monitoring_capability is not None:
            self.monitoring_capability = monitoring_capability
        if owner is not None:
            self.owner = owner
        if private_attributes is not None:
            self.private_attributes = private_attributes
        if provisioning_system is not None:
            self.provisioning_system = provisioning_system
        if provisioning_url is not None:
            self.provisioning_url = provisioning_url
        if vendor is not None:
            self.vendor = vendor

    @property
    def l2vpn_ptp(self):
        """Gets the l2vpn_ptp of this Service.  # noqa: E501


        :return: The l2vpn_ptp of this Service.  # noqa: E501
        :rtype: object
        """
        return self._l2vpn_ptp

    @l2vpn_ptp.setter
    def l2vpn_ptp(self, l2vpn_ptp):
        """Sets the l2vpn_ptp of this Service.


        :param l2vpn_ptp: The l2vpn_ptp of this Service.  # noqa: E501
        :type: object
        """

        self._l2vpn_ptp = l2vpn_ptp

    @property
    def l2vpn_ptmp(self):
        """Gets the l2vpn_ptmp of this Service.  # noqa: E501


        :return: The l2vpn_ptmp of this Service.  # noqa: E501
        :rtype: object
        """
        return self._l2vpn_ptmp

    @l2vpn_ptmp.setter
    def l2vpn_ptmp(self, l2vpn_ptmp):
        """Sets the l2vpn_ptmp of this Service.


        :param l2vpn_ptmp: The l2vpn_ptmp of this Service.  # noqa: E501
        :type: object
        """

        self._l2vpn_ptmp = l2vpn_ptmp

    @property
    def monitoring_capability(self):
        """Gets the monitoring_capability of this Service.  # noqa: E501


        :return: The monitoring_capability of this Service.  # noqa: E501
        :rtype: str
        """
        return self._monitoring_capability

    @monitoring_capability.setter
    def monitoring_capability(self, monitoring_capability):
        """Sets the monitoring_capability of this Service.


        :param monitoring_capability: The monitoring_capability of this Service.  # noqa: E501
        :type: str
        """

        self._monitoring_capability = monitoring_capability

    @property
    def owner(self):
        """Gets the owner of this Service.  # noqa: E501


        :return: The owner of this Service.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Service.


        :param owner: The owner of this Service.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def private_attributes(self):
        """Gets the private_attributes of this Service.  # noqa: E501


        :return: The private_attributes of this Service.  # noqa: E501
        :rtype: list[str]
        """
        return self._private_attributes

    @private_attributes.setter
    def private_attributes(self, private_attributes):
        """Sets the private_attributes of this Service.


        :param private_attributes: The private_attributes of this Service.  # noqa: E501
        :type: list[str]
        """

        self._private_attributes = private_attributes

    @property
    def provisioning_system(self):
        """Gets the provisioning_system of this Service.  # noqa: E501


        :return: The provisioning_system of this Service.  # noqa: E501
        :rtype: str
        """
        return self._provisioning_system

    @provisioning_system.setter
    def provisioning_system(self, provisioning_system):
        """Sets the provisioning_system of this Service.


        :param provisioning_system: The provisioning_system of this Service.  # noqa: E501
        :type: str
        """

        self._provisioning_system = provisioning_system

    @property
    def provisioning_url(self):
        """Gets the provisioning_url of this Service.  # noqa: E501


        :return: The provisioning_url of this Service.  # noqa: E501
        :rtype: str
        """
        return self._provisioning_url

    @provisioning_url.setter
    def provisioning_url(self, provisioning_url):
        """Sets the provisioning_url of this Service.


        :param provisioning_url: The provisioning_url of this Service.  # noqa: E501
        :type: str
        """

        self._provisioning_url = provisioning_url

    @property
    def vendor(self):
        """Gets the vendor of this Service.  # noqa: E501


        :return: The vendor of this Service.  # noqa: E501
        :rtype: list[str]
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this Service.


        :param vendor: The vendor of this Service.  # noqa: E501
        :type: list[str]
        """

        self._vendor = vendor

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
        if issubclass(Service, dict):
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
        if not isinstance(other, Service):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
