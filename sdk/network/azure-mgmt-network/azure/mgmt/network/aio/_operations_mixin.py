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
from msrest import Serializer, Deserializer
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling


class NetworkManagementClientOperationsMixin(object):

    async def begin_delete_bastion_shareable_link(
        self,
        resource_group_name: str,
        bastion_host_name: str,
        bsl_request: "models.BastionShareableLinkListRequest",
        **kwargs
    ) -> AsyncLROPoller[None]:
        """Deletes the Bastion Shareable Links for all the VMs specified in the request.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param bastion_host_name: The name of the Bastion Host.
        :type bastion_host_name: str
        :param bsl_request: Post request for all the Bastion Shareable Link endpoints.
        :type bsl_request: ~azure.mgmt.network.v2020_06_01.models.BastionShareableLinkListRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_delete_bastion_shareable_link')
        if api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-11-01':
            from ..v2019_11_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-12-01':
            from ..v2019_12_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-04-01':
            from ..v2020_04_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-05-01':
            from ..v2020_05_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-06-01':
            from ..v2020_06_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_delete_bastion_shareable_link'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.begin_delete_bastion_shareable_link(resource_group_name, bastion_host_name, bsl_request, **kwargs)

    async def begin_generatevirtualwanvpnserverconfigurationvpnprofile(
        self,
        resource_group_name: str,
        virtual_wan_name: str,
        vpn_client_params: "models.VirtualWanVpnProfileParameters",
        **kwargs
    ) -> AsyncLROPoller["models.VpnProfileResponse"]:
        """Generates a unique VPN profile for P2S clients for VirtualWan and associated
        VpnServerConfiguration combination in the specified resource group.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param virtual_wan_name: The name of the VirtualWAN whose associated VpnServerConfigurations is
         needed.
        :type virtual_wan_name: str
        :param vpn_client_params: Parameters supplied to the generate VirtualWan VPN profile generation
         operation.
        :type vpn_client_params: ~azure.mgmt.network.v2020_06_01.models.VirtualWanVpnProfileParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VpnProfileResponse or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.network.v2020_06_01.models.VpnProfileResponse]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_generatevirtualwanvpnserverconfigurationvpnprofile')
        if api_version == '2019-08-01':
            from ..v2019_08_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-11-01':
            from ..v2019_11_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-12-01':
            from ..v2019_12_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-04-01':
            from ..v2020_04_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-05-01':
            from ..v2020_05_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-06-01':
            from ..v2020_06_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_generatevirtualwanvpnserverconfigurationvpnprofile'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.begin_generatevirtualwanvpnserverconfigurationvpnprofile(resource_group_name, virtual_wan_name, vpn_client_params, **kwargs)

    def begin_get_active_sessions(
        self,
        resource_group_name: str,
        bastion_host_name: str,
        **kwargs
    ) -> AsyncLROPoller[AsyncItemPaged["models.BastionActiveSessionListResult"]]:
        """Returns the list of currently active sessions on the Bastion.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param bastion_host_name: The name of the Bastion Host.
        :type bastion_host_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns an iterator like instance of either BastionActiveSessionListResult or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2020_06_01.models.BastionActiveSessionListResult]]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_get_active_sessions')
        if api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-11-01':
            from ..v2019_11_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-12-01':
            from ..v2019_12_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-04-01':
            from ..v2020_04_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-05-01':
            from ..v2020_05_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-06-01':
            from ..v2020_06_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_get_active_sessions'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_get_active_sessions(resource_group_name, bastion_host_name, **kwargs)

    def begin_put_bastion_shareable_link(
        self,
        resource_group_name: str,
        bastion_host_name: str,
        bsl_request: "models.BastionShareableLinkListRequest",
        **kwargs
    ) -> AsyncLROPoller[AsyncItemPaged["models.BastionShareableLinkListResult"]]:
        """Creates a Bastion Shareable Links for all the VMs specified in the request.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param bastion_host_name: The name of the Bastion Host.
        :type bastion_host_name: str
        :param bsl_request: Post request for all the Bastion Shareable Link endpoints.
        :type bsl_request: ~azure.mgmt.network.v2020_06_01.models.BastionShareableLinkListRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns an iterator like instance of either BastionShareableLinkListResult or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2020_06_01.models.BastionShareableLinkListResult]]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_put_bastion_shareable_link')
        if api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-11-01':
            from ..v2019_11_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-12-01':
            from ..v2019_12_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-04-01':
            from ..v2020_04_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-05-01':
            from ..v2020_05_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-06-01':
            from ..v2020_06_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_put_bastion_shareable_link'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.begin_put_bastion_shareable_link(resource_group_name, bastion_host_name, bsl_request, **kwargs)

    async def check_dns_name_availability(
        self,
        location: str,
        domain_name_label: str,
        **kwargs
    ) -> "models.DnsNameAvailabilityResult":
        """Checks whether a domain name in the cloudapp.azure.com zone is available for use.

        :param location: The location of the domain name.
        :type location: str
        :param domain_name_label: The domain name to be verified. It must conform to the following
         regular expression: ^[a-z][a-z0-9-]{1,61}[a-z0-9]$.
        :type domain_name_label: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DnsNameAvailabilityResult, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2020_06_01.models.DnsNameAvailabilityResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('check_dns_name_availability')
        if api_version == '2015-06-15':
            from ..v2015_06_15.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2016-09-01':
            from ..v2016_09_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2016-12-01':
            from ..v2016_12_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2017-03-01':
            from ..v2017_03_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2017-06-01':
            from ..v2017_06_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2017-08-01':
            from ..v2017_08_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2017-09-01':
            from ..v2017_09_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2017-10-01':
            from ..v2017_10_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2017-11-01':
            from ..v2017_11_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2018-01-01':
            from ..v2018_01_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2018-02-01':
            from ..v2018_02_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2018-04-01':
            from ..v2018_04_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2018-06-01':
            from ..v2018_06_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2018-07-01':
            from ..v2018_07_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2018-08-01':
            from ..v2018_08_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2018-10-01':
            from ..v2018_10_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2018-11-01':
            from ..v2018_11_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2018-12-01':
            from ..v2018_12_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-02-01':
            from ..v2019_02_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-04-01':
            from ..v2019_04_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-07-01':
            from ..v2019_07_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-08-01':
            from ..v2019_08_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-11-01':
            from ..v2019_11_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-12-01':
            from ..v2019_12_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-04-01':
            from ..v2020_04_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-05-01':
            from ..v2020_05_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-06-01':
            from ..v2020_06_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'check_dns_name_availability'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.check_dns_name_availability(location, domain_name_label, **kwargs)

    def disconnect_active_sessions(
        self,
        resource_group_name: str,
        bastion_host_name: str,
        session_ids: "models.SessionIds",
        **kwargs
    ) -> AsyncItemPaged["models.BastionSessionDeleteResult"]:
        """Returns the list of currently active sessions on the Bastion.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param bastion_host_name: The name of the Bastion Host.
        :type bastion_host_name: str
        :param session_ids: The list of sessionids to disconnect.
        :type session_ids: ~azure.mgmt.network.v2020_06_01.models.SessionIds
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BastionSessionDeleteResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2020_06_01.models.BastionSessionDeleteResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('disconnect_active_sessions')
        if api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-11-01':
            from ..v2019_11_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-12-01':
            from ..v2019_12_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-04-01':
            from ..v2020_04_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-05-01':
            from ..v2020_05_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-06-01':
            from ..v2020_06_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'disconnect_active_sessions'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.disconnect_active_sessions(resource_group_name, bastion_host_name, session_ids, **kwargs)

    def get_bastion_shareable_link(
        self,
        resource_group_name: str,
        bastion_host_name: str,
        bsl_request: "models.BastionShareableLinkListRequest",
        **kwargs
    ) -> AsyncItemPaged["models.BastionShareableLinkListResult"]:
        """Return the Bastion Shareable Links for all the VMs specified in the request.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param bastion_host_name: The name of the Bastion Host.
        :type bastion_host_name: str
        :param bsl_request: Post request for all the Bastion Shareable Link endpoints.
        :type bsl_request: ~azure.mgmt.network.v2020_06_01.models.BastionShareableLinkListRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either BastionShareableLinkListResult or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.network.v2020_06_01.models.BastionShareableLinkListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('get_bastion_shareable_link')
        if api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-11-01':
            from ..v2019_11_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-12-01':
            from ..v2019_12_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-04-01':
            from ..v2020_04_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-05-01':
            from ..v2020_05_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-06-01':
            from ..v2020_06_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'get_bastion_shareable_link'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.get_bastion_shareable_link(resource_group_name, bastion_host_name, bsl_request, **kwargs)

    async def supported_security_providers(
        self,
        resource_group_name: str,
        virtual_wan_name: str,
        **kwargs
    ) -> "models.VirtualWanSecurityProviders":
        """Gives the supported security providers for the virtual wan.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param virtual_wan_name: The name of the VirtualWAN for which supported security providers are
         needed.
        :type virtual_wan_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualWanSecurityProviders, or the result of cls(response)
        :rtype: ~azure.mgmt.network.v2020_06_01.models.VirtualWanSecurityProviders
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('supported_security_providers')
        if api_version == '2018-08-01':
            from ..v2018_08_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2018-10-01':
            from ..v2018_10_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2018-11-01':
            from ..v2018_11_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2018-12-01':
            from ..v2018_12_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-02-01':
            from ..v2019_02_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-04-01':
            from ..v2019_04_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-06-01':
            from ..v2019_06_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-07-01':
            from ..v2019_07_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-08-01':
            from ..v2019_08_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-09-01':
            from ..v2019_09_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-11-01':
            from ..v2019_11_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2019-12-01':
            from ..v2019_12_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-03-01':
            from ..v2020_03_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-04-01':
            from ..v2020_04_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-05-01':
            from ..v2020_05_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        elif api_version == '2020-06-01':
            from ..v2020_06_01.aio.operations import NetworkManagementClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'supported_security_providers'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.supported_security_providers(resource_group_name, virtual_wan_name, **kwargs)
