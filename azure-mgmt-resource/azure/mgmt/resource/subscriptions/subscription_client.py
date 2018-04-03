# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration

from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from ..version import VERSION


class SubscriptionClientConfiguration(AzureConfiguration):
    """Configuration for SubscriptionClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(SubscriptionClientConfiguration, self).__init__(base_url)

        self.add_user_agent('subscriptionclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class SubscriptionClient(MultiApiClientMixin):
    """All resource groups and resources exist within subscriptions. These operation enable you get information about your subscriptions and tenants. A tenant is a dedicated instance of Azure Active Directory (Azure AD) for your organization.

    :ivar config: Configuration for client.
    :vartype config: SubscriptionClientConfiguration

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str api_version: API version to use if no profile is provided, or if
     missing in profile.
    :param str base_url: Service URL
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    """

    DEFAULT_API_VERSION='2016-06-01'
    _PROFILE_TAG = "azure.mgmt.resource.subscriptions.SubscriptionClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(self, credentials, api_version=None, base_url=None, profile=KnownProfiles.default):
        super(SubscriptionClient, self).__init__(
            credentials=credentials,
            api_version=api_version,
            base_url=base_url,
            profile=profile
        )

        self.config = SubscriptionClientConfiguration(credentials, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

############ Generated from here ############

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2016-06-01: :mod:`v2016_06_01.models<azure.mgmt.resource.subscriptions.v2016_06_01.models>`
        """
        if api_version == '2016-06-01':
            from .v2016_06_01 import models
            return models
        raise NotImplementedError("APIVersion {} is not available".format(api_version))
    
    @property
    def subscriptions(self):
        """Instance depends on the API version:

           * 2016-06-01: :class:`SubscriptionsOperations<azure.mgmt.resource.subscriptions.v2016_06_01.operations.SubscriptionsOperations>`
        """
        api_version = self._get_api_version('subscriptions')
        if api_version == '2016-06-01':
            from .v2016_06_01.operations import SubscriptionsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def tenants(self):
        """Instance depends on the API version:

           * 2016-06-01: :class:`TenantsOperations<azure.mgmt.resource.subscriptions.v2016_06_01.operations.TenantsOperations>`
        """
        api_version = self._get_api_version('tenants')
        if api_version == '2016-06-01':
            from .v2016_06_01.operations import TenantsOperations as OperationClass
        else:
            raise NotImplementedError("APIVersion {} is not available".format(api_version))
        return OperationClass(self._client, self.config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))
