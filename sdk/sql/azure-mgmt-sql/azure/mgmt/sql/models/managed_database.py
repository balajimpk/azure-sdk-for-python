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

from .tracked_resource import TrackedResource


class ManagedDatabase(TrackedResource):
    """A managed database resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Required. Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param collation: Collation of the managed database.
    :type collation: str
    :ivar status: Status of the database. Possible values include: 'Online',
     'Offline', 'Shutdown', 'Creating', 'Inaccessible', 'Updating'
    :vartype status: str or ~azure.mgmt.sql.models.ManagedDatabaseStatus
    :ivar creation_date: Creation date of the database.
    :vartype creation_date: datetime
    :ivar earliest_restore_point: Earliest restore point in time for point in
     time restore.
    :vartype earliest_restore_point: datetime
    :param restore_point_in_time: Conditional. If createMode is
     PointInTimeRestore, this value is required. Specifies the point in time
     (ISO8601 format) of the source database that will be restored to create
     the new database.
    :type restore_point_in_time: datetime
    :ivar default_secondary_location: Geo paired region.
    :vartype default_secondary_location: str
    :param catalog_collation: Collation of the metadata catalog. Possible
     values include: 'DATABASE_DEFAULT', 'SQL_Latin1_General_CP1_CI_AS'
    :type catalog_collation: str or
     ~azure.mgmt.sql.models.CatalogCollationType
    :param create_mode: Managed database create mode. PointInTimeRestore:
     Create a database by restoring a point in time backup of an existing
     database. SourceDatabaseName, SourceManagedInstanceName and PointInTime
     must be specified. RestoreExternalBackup: Create a database by restoring
     from external backup files. Collation, StorageContainerUri and
     StorageContainerSasToken must be specified. Recovery: Creates a database
     by restoring a geo-replicated backup. RecoverableDatabaseId must be
     specified as the recoverable database resource ID to restore. Possible
     values include: 'Default', 'RestoreExternalBackup', 'PointInTimeRestore',
     'Recovery'
    :type create_mode: str or ~azure.mgmt.sql.models.ManagedDatabaseCreateMode
    :param storage_container_uri: Conditional. If createMode is
     RestoreExternalBackup, this value is required. Specifies the uri of the
     storage container where backups for this restore are stored.
    :type storage_container_uri: str
    :param source_database_id: The resource identifier of the source database
     associated with create operation of this database.
    :type source_database_id: str
    :param restorable_dropped_database_id: The restorable dropped database
     resource id to restore when creating this database.
    :type restorable_dropped_database_id: str
    :param storage_container_sas_token: Conditional. If createMode is
     RestoreExternalBackup, this value is required. Specifies the storage
     container sas token.
    :type storage_container_sas_token: str
    :ivar failover_group_id: Instance Failover Group resource identifier that
     this managed database belongs to.
    :vartype failover_group_id: str
    :param recoverable_database_id: The resource identifier of the recoverable
     database associated with create operation of this database.
    :type recoverable_database_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'status': {'readonly': True},
        'creation_date': {'readonly': True},
        'earliest_restore_point': {'readonly': True},
        'default_secondary_location': {'readonly': True},
        'failover_group_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'collation': {'key': 'properties.collation', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'earliest_restore_point': {'key': 'properties.earliestRestorePoint', 'type': 'iso-8601'},
        'restore_point_in_time': {'key': 'properties.restorePointInTime', 'type': 'iso-8601'},
        'default_secondary_location': {'key': 'properties.defaultSecondaryLocation', 'type': 'str'},
        'catalog_collation': {'key': 'properties.catalogCollation', 'type': 'str'},
        'create_mode': {'key': 'properties.createMode', 'type': 'str'},
        'storage_container_uri': {'key': 'properties.storageContainerUri', 'type': 'str'},
        'source_database_id': {'key': 'properties.sourceDatabaseId', 'type': 'str'},
        'restorable_dropped_database_id': {'key': 'properties.restorableDroppedDatabaseId', 'type': 'str'},
        'storage_container_sas_token': {'key': 'properties.storageContainerSasToken', 'type': 'str'},
        'failover_group_id': {'key': 'properties.failoverGroupId', 'type': 'str'},
        'recoverable_database_id': {'key': 'properties.recoverableDatabaseId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ManagedDatabase, self).__init__(**kwargs)
        self.collation = kwargs.get('collation', None)
        self.status = None
        self.creation_date = None
        self.earliest_restore_point = None
        self.restore_point_in_time = kwargs.get('restore_point_in_time', None)
        self.default_secondary_location = None
        self.catalog_collation = kwargs.get('catalog_collation', None)
        self.create_mode = kwargs.get('create_mode', None)
        self.storage_container_uri = kwargs.get('storage_container_uri', None)
        self.source_database_id = kwargs.get('source_database_id', None)
        self.restorable_dropped_database_id = kwargs.get('restorable_dropped_database_id', None)
        self.storage_container_sas_token = kwargs.get('storage_container_sas_token', None)
        self.failover_group_id = None
        self.recoverable_database_id = kwargs.get('recoverable_database_id', None)