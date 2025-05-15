import json
from typing import Any



def json_merge(json1, json2):
    for j in json2:
        if j in json1 and isinstance(json1[j],dict):
            json_merge(json1[j],json2[j])
        else:
            json1[j] = json2[j]
    return json1       


def json_configs_merge(*json_paths: str) -> dict[str, Any]:
    data = None

    if not json_paths or json_paths == "":
        return {}

    with open(json_paths[0], 'r') as js:
        data = json.load(js)

    for i in range(1,len(json_paths)):
        with open(json_paths[i], 'r') as js:
            js_data = json.load(js)
            data = json_merge(data,js_data)

    return data


if __name__ == '__main__':
    # Example usage; make sure the files exist for this to run.
    config = json_configs_merge('default.json','production.json','us-east-1-production.json')
    print(config)
