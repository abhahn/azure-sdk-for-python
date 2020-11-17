# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import MySQLManagementClientConfiguration
from .operations import ServersOperations
from .operations import ReplicasOperations
from .operations import FirewallRulesOperations
from .operations import VirtualNetworkRulesOperations
from .operations import DatabasesOperations
from .operations import ConfigurationsOperations
from .operations import LogFilesOperations
from .operations import ServerAdministratorsOperations
from .operations import LocationBasedPerformanceTierOperations
from .operations import CheckNameAvailabilityOperations
from .operations import Operations
from .operations import ServerSecurityAlertPoliciesOperations
from .operations import QueryTextsOperations
from .operations import TopQueryStatisticsOperations
from .operations import WaitStatisticsOperations
from .operations import AdvisorsOperations
from .operations import MySQLManagementClientOperationsMixin
from .operations import RecommendedActionsOperations
from .operations import LocationBasedRecommendedActionSessionsOperationStatusOperations
from .operations import LocationBasedRecommendedActionSessionsResultOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from .operations import ServerKeysOperations
from . import models


class MySQLManagementClient(MySQLManagementClientOperationsMixin):
    """The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, log files and configurations with new business model.

    :ivar servers: ServersOperations operations
    :vartype servers: azure.mgmt.rdbms.mysql.v2020_01_01.operations.ServersOperations
    :ivar replicas: ReplicasOperations operations
    :vartype replicas: azure.mgmt.rdbms.mysql.v2020_01_01.operations.ReplicasOperations
    :ivar firewall_rules: FirewallRulesOperations operations
    :vartype firewall_rules: azure.mgmt.rdbms.mysql.v2020_01_01.operations.FirewallRulesOperations
    :ivar virtual_network_rules: VirtualNetworkRulesOperations operations
    :vartype virtual_network_rules: azure.mgmt.rdbms.mysql.v2020_01_01.operations.VirtualNetworkRulesOperations
    :ivar databases: DatabasesOperations operations
    :vartype databases: azure.mgmt.rdbms.mysql.v2020_01_01.operations.DatabasesOperations
    :ivar configurations: ConfigurationsOperations operations
    :vartype configurations: azure.mgmt.rdbms.mysql.v2020_01_01.operations.ConfigurationsOperations
    :ivar log_files: LogFilesOperations operations
    :vartype log_files: azure.mgmt.rdbms.mysql.v2020_01_01.operations.LogFilesOperations
    :ivar server_administrators: ServerAdministratorsOperations operations
    :vartype server_administrators: azure.mgmt.rdbms.mysql.v2020_01_01.operations.ServerAdministratorsOperations
    :ivar location_based_performance_tier: LocationBasedPerformanceTierOperations operations
    :vartype location_based_performance_tier: azure.mgmt.rdbms.mysql.v2020_01_01.operations.LocationBasedPerformanceTierOperations
    :ivar check_name_availability: CheckNameAvailabilityOperations operations
    :vartype check_name_availability: azure.mgmt.rdbms.mysql.v2020_01_01.operations.CheckNameAvailabilityOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.rdbms.mysql.v2020_01_01.operations.Operations
    :ivar server_security_alert_policies: ServerSecurityAlertPoliciesOperations operations
    :vartype server_security_alert_policies: azure.mgmt.rdbms.mysql.v2020_01_01.operations.ServerSecurityAlertPoliciesOperations
    :ivar query_texts: QueryTextsOperations operations
    :vartype query_texts: azure.mgmt.rdbms.mysql.v2020_01_01.operations.QueryTextsOperations
    :ivar top_query_statistics: TopQueryStatisticsOperations operations
    :vartype top_query_statistics: azure.mgmt.rdbms.mysql.v2020_01_01.operations.TopQueryStatisticsOperations
    :ivar wait_statistics: WaitStatisticsOperations operations
    :vartype wait_statistics: azure.mgmt.rdbms.mysql.v2020_01_01.operations.WaitStatisticsOperations
    :ivar advisors: AdvisorsOperations operations
    :vartype advisors: azure.mgmt.rdbms.mysql.v2020_01_01.operations.AdvisorsOperations
    :ivar recommended_actions: RecommendedActionsOperations operations
    :vartype recommended_actions: azure.mgmt.rdbms.mysql.v2020_01_01.operations.RecommendedActionsOperations
    :ivar location_based_recommended_action_sessions_operation_status: LocationBasedRecommendedActionSessionsOperationStatusOperations operations
    :vartype location_based_recommended_action_sessions_operation_status: azure.mgmt.rdbms.mysql.v2020_01_01.operations.LocationBasedRecommendedActionSessionsOperationStatusOperations
    :ivar location_based_recommended_action_sessions_result: LocationBasedRecommendedActionSessionsResultOperations operations
    :vartype location_based_recommended_action_sessions_result: azure.mgmt.rdbms.mysql.v2020_01_01.operations.LocationBasedRecommendedActionSessionsResultOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections: azure.mgmt.rdbms.mysql.v2020_01_01.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources: azure.mgmt.rdbms.mysql.v2020_01_01.operations.PrivateLinkResourcesOperations
    :ivar server_keys: ServerKeysOperations operations
    :vartype server_keys: azure.mgmt.rdbms.mysql.v2020_01_01.operations.ServerKeysOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MySQLManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.servers = ServersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replicas = ReplicasOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.firewall_rules = FirewallRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_network_rules = VirtualNetworkRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.configurations = ConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.log_files = LogFilesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.server_administrators = ServerAdministratorsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.location_based_performance_tier = LocationBasedPerformanceTierOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.check_name_availability = CheckNameAvailabilityOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.server_security_alert_policies = ServerSecurityAlertPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.query_texts = QueryTextsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.top_query_statistics = TopQueryStatisticsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.wait_statistics = WaitStatisticsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.advisors = AdvisorsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.recommended_actions = RecommendedActionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.location_based_recommended_action_sessions_operation_status = LocationBasedRecommendedActionSessionsOperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.location_based_recommended_action_sessions_result = LocationBasedRecommendedActionSessionsResultOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.server_keys = ServerKeysOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MySQLManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
