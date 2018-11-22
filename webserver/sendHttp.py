import requests
import datetime

SOLAR = "http://localhost/api/solar/"

#Post data to the webserver
#INPUT : params (dictionnary)
#ex dict = ['intensity':'150', etc]
#OUTPUT : TRUE if successful, else FALSE
def postData(params):
    r = requests.post(SOLAR, params)

    if r.status_code is not 200:
        print ("Error:", r.status_code)
        return False
    return True

def deleteData(resourceId):
    r = requests.delete("{url}{rid}".format(url=SOLAR, rid=resourceId))
    if r.status_code is not 204:
        print ("Error:", r.status_code)
        return False
    return True



def main():
    time = datetime.datetime.now()
    for i in range(115,225):
        postData(params={'intensity':'10','time':time})

if __name__ == "__main__":
    main()
