"""Creates the virtual machine."""

COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'

names = ["mig1", "mig2"]

def GenerateConfig(name):
       	resources = [{
               	'type': 'compute.v1.regionInstanceGroupManager',
               	'name': names[0],
               	'properties': {
                       	'instanceTemplate': 'projects/ops-munir-kakar/global/instanceTemplates/build-template',
                       	'region': 'europe-west2',
                       	'targetSize': 1,
                       	'namedPorts': [{
                               	'name': 'http',
                               	'port': 80
                       	}],
                       	'autoHealingPolicies': [{
                               	'healthCheck': 'projects/ops-munir-kakar/global/healthChecks/health-check'
                       	}]
               	}
        },
	{
		'type': 'compute.v1.regionInstanceGroupManager',
                'name': names[1],
                'properties': {
                        'instanceTemplate': 'projects/ops-munir-kakar/global/instanceTemplates/build-template',
                        'region': 'europe-west2',
                        'targetSize': 1,
                        'namedPorts': [{
                                'name': 'http',
                                'port': 80
                        }],
                        'autoHealingPolicies': [{
                                'healthCheck': 'projects/ops-munir-kakar/global/healthChecks/health-check'
                        }]
                }
	}]

        return {'resources': resources}

