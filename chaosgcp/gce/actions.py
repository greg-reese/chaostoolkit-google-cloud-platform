# -*- coding: utf-8 -*-
from typing import Any, Dict

from chaoslib.types import Configuration, Secrets

from chaosgcp import get_context, get_service

__all__ = ["delete_instance"]

def delete_instance(
        zone: str,
        name: str,
        configuration: Configuration = None,
        secrets: Secrets = None,
        ):
    """
    Deletes a Compute Engine instance.

    NB: The instance must exist in the targeted project.

    See: https://cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.instances.InstancesClient#google_cloud_compute_v1_services_instances_InstancesClient_delete_unary

    :param name: name of the instance
    :param zone: zone of the instance
    :param configuration:
    :param secrets:

    :return:
    """
    ctx = get_context(configuration=configuration, secrets=secrets)
    service = get_service('compute', version='v1',
                          configuration=configuration, secrets=secrets)

    request = service.projects().delete_unary(
        project=ctx.project_id, zone=zone, instance=name)
    response = request.execute()
    return response
