def post():

SOLAR = "http://localhost/api/solar/" #Get IP adress

# Post data to the webserver
def post_data(params):
    r = requests.post(SOLAR, params)
    if r.status_code is not 200:
        print ("Error:", r.status_code)
        return False
    return True


