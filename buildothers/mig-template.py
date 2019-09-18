"""Creates the virtual machine."""

COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(unused_context):
	"""Creates the first virtual machine."""

	resources = [{
		'type': 'compute.v1.regionInstanceGroupManager',
		'name': 'mig-test',
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
