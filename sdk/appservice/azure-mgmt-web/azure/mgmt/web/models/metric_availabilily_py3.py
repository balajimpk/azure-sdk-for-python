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

from msrest.serialization import Model


class MetricAvailabilily(Model):
    """Metric availability and retention.

    :param time_grain: Time grain.
    :type time_grain: str
    :param retention: Retention period for the current time grain.
    :type retention: str
    """

    _attribute_map = {
        'time_grain': {'key': 'timeGrain', 'type': 'str'},
        'retention': {'key': 'retention', 'type': 'str'},
    }

    def __init__(self, *, time_grain: str=None, retention: str=None, **kwargs) -> None:
        super(MetricAvailabilily, self).__init__(**kwargs)
        self.time_grain = time_grain
        self.retention = retention