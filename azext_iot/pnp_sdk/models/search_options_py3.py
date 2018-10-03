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


class SearchOptions(Model):
    """SearchOptions.

    :param search_keyword:
    :type search_keyword: str
    :param model_filter_type: Possible values include: 'interface',
     'capabilityModel'
    :type model_filter_type: str or
     ~digitaltwinmodelrepositoryservice.models.enum
    :param continuation_token:
    :type continuation_token: str
    :param page_size:
    :type page_size: int
    """

    _attribute_map = {
        'search_keyword': {'key': 'searchKeyword', 'type': 'str'},
        'model_filter_type': {'key': 'modelFilterType', 'type': 'str'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'page_size': {'key': 'pageSize', 'type': 'int'},
    }

    def __init__(self, *, search_keyword: str=None, model_filter_type=None, continuation_token: str=None, page_size: int=None, **kwargs) -> None:
        super(SearchOptions, self).__init__(**kwargs)
        self.search_keyword = search_keyword
        self.model_filter_type = model_filter_type
        self.continuation_token = continuation_token
        self.page_size = page_size
