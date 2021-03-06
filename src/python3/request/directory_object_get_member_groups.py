# -*- coding: utf-8 -*- 
"""
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
"""

from ..collection_base import CollectionRequestBase
from ..request_builder_base import RequestBuilderBase
from ..options import *
import json
import asyncio
from ..request import drive_item_collection 


class DirectoryObjectGetMemberGroupsRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options, security_enabled_only=None):
        super(DirectoryObjectGetMemberGroupsRequest, self).__init__(request_url, client, options)
        self.method = "POST"
        self.body_options={}

        if security_enabled_only:
            self.body_options["securityEnabledOnly"] = security_enabled_only

    @property
    def body_options(self):
        return self._body_options

    @body_options.setter
    def body_options(self, value):
        self._body_options=value

    def post(self):
        """Sends the POST request
        
        Returns: 
            :class:`DriveItemCollectionResponse<msgraph.request.drive_item_collection.DriveItemCollectionResponse>`:
                The resulting collection page from the operation
        """
        self.content_type = "application/json"
        collection_response = drive_item_collection.DriveItemCollectionResponse(json.loads(self.send(self.body_options).content))
        return self._page_from_response(collection_response)

    @asyncio.coroutine
    def post_async(self):
        """Sends the POST request using an asyncio coroutine

        Yields:
            :class:`DriveItemCollectionResponse<msgraph.request.drive_item_collection.DriveItemCollectionResponse>`:
                The resulting collection page from the operation
        """
        future = self._client._loop.run_in_executor(None,
                                                    self.post)
        collection_response = yield from future
        return collection_response


class DirectoryObjectGetMemberGroupsRequestBuilder(RequestBuilderBase):

    def __init__(self, request_url, client, security_enabled_only=None):
        super(DirectoryObjectGetMemberGroupsRequestBuilder, self).__init__(request_url, client)
        self._method_options = {}

        self._method_options["securityEnabledOnly"] = security_enabled_only

    def request(self,select=None, filter=None, top=None, skip=None, order_by=None, options=None):
        """Builds the request for the DirectoryObjectGetMemberGroups
        
        Args:
            expand (str): Default None, comma-separated list of relationships
                to expand in the response.
            select (str): Default None, comma-separated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-separated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<msgraph.options.Option>`):
                Default to None, list of options to include in the request

        Returns: 
            :class:`DirectoryObjectGetMemberGroupsRequest<msgraph.request.directory_object_get_member_groups.DirectoryObjectGetMemberGroupsRequest>`:
                The request
        """
        req = DirectoryObjectGetMemberGroupsRequest(self._request_url, self._client, options, security_enabled_only=self._method_options["securityEnabledOnly"])
        req._set_query_options(select=select, filter=filter, top=top, skip=skip, order_by=order_by, )
        return req

    def post(self):
        """Sends the POST request
        
        Returns:
            :class:`DriveItemCollectionResponse<msgraph.request.drive_item_collection.DriveItemCollectionResponse>`:
            The resulting DriveItemCollectionResponse from the operation
        """
        return self.request().post()

    @asyncio.coroutine
    def post_async(self):
        """Sends the POST request using an asyncio coroutine
        
        Yields:
            :class:`DriveItemCollectionResponse<msgraph.request.drive_item_collection.DriveItemCollectionResponse>`:
                The resulting DriveItemCollectionResponse from the operation
        """
        collection_page = yield from self.request().post_async()
        return collection_page

