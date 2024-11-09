# Python project to generate yaml configuration files for Home Assistant

## Setup

```
$ python3 -m venv ./venv
$ source ./venv/bin/activate
$ pip install -e .
```

### Add your devices as follows:

```
{
	"suggested_area": "<your-area>",
	"devices": [
		{
			"template": "<Template>.jinja",
			"state_topic": "zigbee2mqtt/<topic>",
			"identifier": "<id of device>",
			"model": "<model of device>",
			"manufacturer": "<manufacturer of device>",
			"device_name": "<your name for the device>"
		}
	]
}

```