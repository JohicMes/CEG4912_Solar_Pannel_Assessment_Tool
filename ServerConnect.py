import requests

SOLAR = "http://localhost/api/solar/"


# Post data to the webserver
def post_data(params):
    r = requests.post(SOLAR, params)

    if r.status_code is not 200:
        print ("Error:", r.status_code)
        return False
    return True


def delete_data(resourceId):
    r = requests.delete("{url}{rid}".format(url=SOLAR, rid=resourceId))
    if r.status_code is not 204:
        print ("Error:", r.status_code)
        return False
    return True