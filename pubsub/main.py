import base64
import json
import os
from googleapiclient import discovery
PROJECT_ID = os.getenv('GCP_PROJECT')
PROJECT_NAME = f'projects/{PROJECT_ID}'
ZONE = 'us-west1-b'


def limit_use(data, context):
    pubsub_data = base64.b64decode(data['data']).decode('utf-8')
    pubsub_json = json.loads(pubsub_data)
    cost_amount = pubsub_json['costAmount']
    budget_amount = pubsub_json['budgetAmount']
    if cost_amount <= budget_amount:
        print(f'No action necessary. (Current cost: {cost_amount})')
        return

    compute = discovery.build(
        'compute',
        'v1',
        cache_discovery=False,
    )
    instances = compute.instances()

    instance_names = __list_running_instances(PROJECT_ID, ZONE, instances)
    __stop_instances(PROJECT_ID, ZONE, instance_names, instances)


def __list_running_instances(project_id, zone, instances):
    """
    @param {string} project_id ID of project that contains instances to stop
    @param {string} zone Zone that contains instances to stop
    @return {Promise} Array of names of running instances
    """
    res = instances.list(project=project_id, zone=zone).execute()

    if 'items' not in res:
        return []

    items = res['items']
    running_names = [i['name'] for i in items if i['status'] == 'RUNNING']
    return running_names


def __stop_instances(project_id, zone, instance_names, instances):
    """
    @param {string} project_id ID of project that contains instances to stop
    @param {string} zone Zone that contains instances to stop
    @param {Array} instance_names Names of instance to stop
    @return {Promise} Response from stopping instances
    """
    if not len(instance_names):
        print('No running instances were found.')
        return

    for name in instance_names:
        instances.stop(
          project=project_id,
          zone=zone,
          instance=name).execute()
        print(f'Instance stopped successfully: {name}')