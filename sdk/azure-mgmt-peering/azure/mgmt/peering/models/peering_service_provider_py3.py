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

from .resource_py3 import Resource


class PeeringServiceProvider(Resource):
    """PeeringService provider.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: The name of the resource.
    :vartype name: str
    :ivar id: The ID of the resource.
    :vartype id: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param service_provider_name: The name of the service provider.
    :type service_provider_name: str
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'service_provider_name': {'key': 'properties.serviceProviderName', 'type': 'str'},
    }

    def __init__(self, *, service_provider_name: str=None, **kwargs) -> None:
        super(PeeringServiceProvider, self).__init__(**kwargs)
        self.service_provider_name = service_provider_name