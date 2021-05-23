# pip install pyyaml

import yaml

filename1 = "00-modules/external_modules/yaml/example.yaml"

data = {
    'hi': [
        1, 
        2, 
        3.141, 
        "1337", 
        'help', 
        '€'
    ],
    'hello': 'bla',
    'another dict': {
        'foo': 'bar',
        'key': 'value',
        'the answer': 42
    },
    "code": "import os\nprint(os.listdir())",
    "unsecure_code": "import os\nexec(print(os.listdir()))"
}

# Write YAML file
with open(filename1, 'w', encoding='utf8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

# Read YAML file
with open(filename1, 'r', encoding='utf8') as stream:
    try:
        data_loaded = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc) 


print(data_loaded)


# can run code
exec(data_loaded['code'])


# safe_load wont runs unsecure code
# yaml.load(stream)
# data_loaded['unsecure_code']
