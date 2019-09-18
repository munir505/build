"""Creates the virtual machine."""

COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(unused_context):
    """Creates the first virtual machine."""

    resources = [{
        'name': 'the-first-vm',
        'type': 'compute.v1.instance',
        'properties': {
            'zone': 'europe-west2-c',
            'machineType': ''.join([COMPUTE_URL_BASE, 'projects/ops-munir-kakar', '/zones/europe-west2-c/', 'machineTypes/n1-standard-1']),
            'disks': [{
                'deviceName': 'boot',
                'type': 'PERSISTENT',
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/', 'centos-cloud/global/', 'images/centos-7-v20190619'])
                }
            }],
            'networkInterfaces': [{
                'network': 'global/networks/default',
                'accessConfigs': [{
                    'name': 'External NAT',
                    'type': 'ONE_TO_ONE_NAT'
                }]
            }]
        }
    }]
    return {'resources': resources}
