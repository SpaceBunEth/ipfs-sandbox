import requests

#DOCS: http://docs.ipfs.tech.ipns.localhost:8080/reference/kubo/rpc/#api-v0-filestore-verify

# This is the baseurl for a local running ipfs daemon
# the default port is 5002 and api route /api/v0
BASE = "http://localhost:5002/api/v0"


"""
implement the following:
 - cat -- http://docs.ipfs.tech.ipns.localhost:8080/reference/kubo/rpc/#api-v0-cat
 - pin -- http://docs.ipfs.tech.ipns.localhost:8080/reference/kubo/rpc/#api-v0-pin-add
 - add -- http://docs.ipfs.tech.ipns.localhost:8080/reference/kubo/rpc/#api-v0-add
"""

def cat(ipfs_path, file_path):
    # cat gets a file from IPFS
    # add the cid (ipfs_path) to the http params
    route = add_params_to_route("/cat", { "arg": ipfs_path })
    # Make post request to cat route. Stream=true might not be necessary
    r = requests.post(BASE + route, data={}, stream=True)
    # open a file using file_path
    with open(file_path, 'wb') as fd:
        # write the raw response of the request to the file
        # you may not need the raw response. Maybe just response.content
        # do what works, refer to this: https://requests.readthedocs.io/en/latest/user/quickstart/#binary-response-content
        fd.write(r.raw.read())

def get_swarms():
    # swarm/peers returns the list of peers in your p2p swarm
    # here we're POSTING to the endpoint to get the peers
    # we call .json to turn the response into a python dictionary
    return requests.post(BASE + "/swarm/peers").json()

def add_params_to_route(route, params):
    # this takes a route (str) and params (dict)
    # it returns the route with the params as http query params
    # i.e. if you route is /myapp/endpoint and params is { "search": "pizza", "user": "jude" }
    # it creates /myapp/endpoint?search=pizza&user=jude
    # this is useful for adding params to IPFS endpoints
    route += "?"
    serialized_params = ""
    # we're iterating through keys and values of the dictionary
    for k, v in params.items():
        # constructing our params from each k and v pair
        serialized_params += serialized_params + f"{k}={v}&"

    # return our route and params without the last character which is a trailing &
    return route + serialized_params[:-1]

