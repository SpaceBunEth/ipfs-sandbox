import requests

#DOCS: http://docs.ipfs.tech.ipns.localhost:8080/reference/kubo/rpc/#api-v0-filestore-verify

BASE = "http://localhost:5002/api/v0"


"""
notes:
implement the following:
 - cat -- http://docs.ipfs.tech.ipns.localhost:8080/reference/kubo/rpc/#api-v0-cat
 - pin -- http://docs.ipfs.tech.ipns.localhost:8080/reference/kubo/rpc/#api-v0-pin-add
 - add -- http://docs.ipfs.tech.ipns.localhost:8080/reference/kubo/rpc/#api-v0-add
"""

def cat(ipfs_path, file_path):
    route = add_params_to_route("/cat", { "arg": ipfs_path })
    r = requests.post(BASE + route, data={}, stream=True)
    with open(file_path, 'wb') as fd:
        fd.write(r.raw.read())

def get_swarms():
    return http_post("/swarm/peers").json()

def http_get(route):
    return requests.get(BASE + route)

def http_post(route, params={}, payload={}):
    route = add_params_to_route(route, params)
    return requests.post(BASE + route, data=payload)

def add_params_to_route(route, params):
    route += "?"
    serialized_params = ""
    for k, v in params.items():
        serialized_params += serialized_params + f"{k}={v}&"

    return route + serialized_params[:-1]

