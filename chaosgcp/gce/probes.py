# -*- coding: utf-8 -*-

from chaoslib.types import Configuration, Secrets

from chaosgcp import get_context, get_service

__all__ = ["list_instances"]


def list_instances(
        zone: str,
        configuration: Configuration = None,
        secrets: Secrets = None,
        ):
    """
    Lists existing compute engine instances

    See: https://cloud.google.com/compute/docs/reference/rest/v1/instances/list

    :param zone: zone of the instances
    :param configuration:
    :param secrets:

    :return:
    """  # noqa: E501
    ctx = get_context(configuration=configuration, secrets=secrets)
    service = get_service('compute', version='v1',
                          configuration=configuration, secrets=secrets)

    request = service.projects().list(project=ctx.project_id, zone=zone)
    response = request.execute()
    return response

def get_instance(
        zone: str,
        name: str,
        configuration: Configuration = None,
        secrets: Secrets = None,
        ):
    """
    Returns information about a Compute Engine instance.

    See: https://cloud.google.com/compute/docs/reference/rest/v1/instances/get

    :param zone: zone of the instance
    :param name: name of the instance
    :param configuration:
    :param secrets:
    :return:
    """  # noqa: E501
    ctx = get_context(configuration=configuration, secrets=secrets)
    service = get_service('compute', version='v1',
                          configuration=configuration, secrets=secrets)

    request = service.projects().get(
        projectId=ctx.project_id, zone=zone, instance=name)
    response = request.execute()
    return response
