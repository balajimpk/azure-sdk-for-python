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


class JobCreateParameters(Model):
    """Parameters supplied to the Create operation.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The region in which to create the job.
    :type location: str
    :param tags: The user specified tags associated with the job.
    :type tags: dict[str, str]
    :param experiment_name: Describe the experiment information of the job
    :type experiment_name: str
    :param priority: Priority associated with the job. Priority associated
     with the job. Priority values can range from -1000 to 1000, with -1000
     being the lowest priority and 1000 being the highest priority. The default
     value is 0. Default value: 0 .
    :type priority: int
    :param cluster: Required. Specifies the Id of the cluster on which this
     job will run.
    :type cluster: ~azure.mgmt.batchai.models.ResourceId
    :param mount_volumes: Information on mount volumes to be used by the job.
     These volumes will be mounted before the job execution and will be
     unmouted after the job completion. The volumes will be mounted at location
     specified by $AZ_BATCHAI_JOB_MOUNT_ROOT environment variable.
    :type mount_volumes: ~azure.mgmt.batchai.models.MountVolumes
    :param node_count: Required. Number of compute nodes to run the job on.
     The job will be gang scheduled on that many compute nodes
    :type node_count: int
    :param container_settings: If provided the job will run in the specified
     container. If the container was downloaded as part of cluster setup then
     the same container image will be used. If not provided, the job will run
     on the VM.
    :type container_settings: ~azure.mgmt.batchai.models.ContainerSettings
    :param cntk_settings: Specifies the settings for CNTK (aka Microsoft
     Cognitive Toolkit) job.
    :type cntk_settings: ~azure.mgmt.batchai.models.CNTKsettings
    :param py_torch_settings: Specifies the settings for pyTorch job.
    :type py_torch_settings: ~azure.mgmt.batchai.models.PyTorchSettings
    :param tensor_flow_settings: Specifies the settings for Tensor Flow job.
    :type tensor_flow_settings: ~azure.mgmt.batchai.models.TensorFlowSettings
    :param caffe_settings: Specifies the settings for Caffe job.
    :type caffe_settings: ~azure.mgmt.batchai.models.CaffeSettings
    :param caffe2_settings: Specifies the settings for Caffe2 job.
    :type caffe2_settings: ~azure.mgmt.batchai.models.Caffe2Settings
    :param chainer_settings: Specifies the settings for Chainer job.
    :type chainer_settings: ~azure.mgmt.batchai.models.ChainerSettings
    :param custom_toolkit_settings: Specifies the settings for custom tool kit
     job.
    :type custom_toolkit_settings:
     ~azure.mgmt.batchai.models.CustomToolkitSettings
    :param job_preparation: Specifies the command line to be executed before
     tool kit is launched. The specified actions will run on all the nodes that
     are part of the job
    :type job_preparation: ~azure.mgmt.batchai.models.JobPreparation
    :param std_out_err_path_prefix: Required. The path where the Batch AI
     service will upload stdout and stderror of the job.
    :type std_out_err_path_prefix: str
    :param input_directories: Specifies the list of input directories for the
     Job.
    :type input_directories: list[~azure.mgmt.batchai.models.InputDirectory]
    :param output_directories: Specifies the list of output directories.
    :type output_directories: list[~azure.mgmt.batchai.models.OutputDirectory]
    :param environment_variables: Additional environment variables to set on
     the job. Batch AI will setup these additional environment variables for
     the job.
    :type environment_variables:
     list[~azure.mgmt.batchai.models.EnvironmentVariable]
    :param secrets: Additional environment variables with secret values to set
     on the job. Batch AI will setup these additional environment variables for
     the job. Server will never report values of these variables back.
    :type secrets:
     list[~azure.mgmt.batchai.models.EnvironmentVariableWithSecretValue]
    :param constraints: Constraints associated with the Job.
    :type constraints: ~azure.mgmt.batchai.models.JobBasePropertiesConstraints
    """

    _validation = {
        'location': {'required': True},
        'cluster': {'required': True},
        'node_count': {'required': True},
        'std_out_err_path_prefix': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'experiment_name': {'key': 'properties.experimentName', 'type': 'str'},
        'priority': {'key': 'properties.priority', 'type': 'int'},
        'cluster': {'key': 'properties.cluster', 'type': 'ResourceId'},
        'mount_volumes': {'key': 'properties.mountVolumes', 'type': 'MountVolumes'},
        'node_count': {'key': 'properties.nodeCount', 'type': 'int'},
        'container_settings': {'key': 'properties.containerSettings', 'type': 'ContainerSettings'},
        'cntk_settings': {'key': 'properties.cntkSettings', 'type': 'CNTKsettings'},
        'py_torch_settings': {'key': 'properties.pyTorchSettings', 'type': 'PyTorchSettings'},
        'tensor_flow_settings': {'key': 'properties.tensorFlowSettings', 'type': 'TensorFlowSettings'},
        'caffe_settings': {'key': 'properties.caffeSettings', 'type': 'CaffeSettings'},
        'caffe2_settings': {'key': 'properties.caffe2Settings', 'type': 'Caffe2Settings'},
        'chainer_settings': {'key': 'properties.chainerSettings', 'type': 'ChainerSettings'},
        'custom_toolkit_settings': {'key': 'properties.customToolkitSettings', 'type': 'CustomToolkitSettings'},
        'job_preparation': {'key': 'properties.jobPreparation', 'type': 'JobPreparation'},
        'std_out_err_path_prefix': {'key': 'properties.stdOutErrPathPrefix', 'type': 'str'},
        'input_directories': {'key': 'properties.inputDirectories', 'type': '[InputDirectory]'},
        'output_directories': {'key': 'properties.outputDirectories', 'type': '[OutputDirectory]'},
        'environment_variables': {'key': 'properties.environmentVariables', 'type': '[EnvironmentVariable]'},
        'secrets': {'key': 'properties.secrets', 'type': '[EnvironmentVariableWithSecretValue]'},
        'constraints': {'key': 'properties.constraints', 'type': 'JobBasePropertiesConstraints'},
    }

    def __init__(self, *, location: str, cluster, node_count: int, std_out_err_path_prefix: str, tags=None, experiment_name: str=None, priority: int=0, mount_volumes=None, container_settings=None, cntk_settings=None, py_torch_settings=None, tensor_flow_settings=None, caffe_settings=None, caffe2_settings=None, chainer_settings=None, custom_toolkit_settings=None, job_preparation=None, input_directories=None, output_directories=None, environment_variables=None, secrets=None, constraints=None, **kwargs) -> None:
        super(JobCreateParameters, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.experiment_name = experiment_name
        self.priority = priority
        self.cluster = cluster
        self.mount_volumes = mount_volumes
        self.node_count = node_count
        self.container_settings = container_settings
        self.cntk_settings = cntk_settings
        self.py_torch_settings = py_torch_settings
        self.tensor_flow_settings = tensor_flow_settings
        self.caffe_settings = caffe_settings
        self.caffe2_settings = caffe2_settings
        self.chainer_settings = chainer_settings
        self.custom_toolkit_settings = custom_toolkit_settings
        self.job_preparation = job_preparation
        self.std_out_err_path_prefix = std_out_err_path_prefix
        self.input_directories = input_directories
        self.output_directories = output_directories
        self.environment_variables = environment_variables
        self.secrets = secrets
        self.constraints = constraints
