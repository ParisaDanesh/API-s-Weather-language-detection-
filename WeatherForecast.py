import requests
import json

def map(adres,proxies):
    address = adres
    accessKey = "AIzaSyBUpbYmXN4bBZC7NqBPVM8x7_mftAWUuD4"
    URL = "https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key="+accessKey
    connect = requests.post(URL,proxies=proxies)
    # return connect.text
    output = connect.text
    result = json.loads(output)
    # print json.dumps(result, indent=4, sort_keys=True)
    try:
        print result['results1'][0]['place_id']
    except:
        pass
    exit(0)
    # newRes= result.get('results')
    # print newRes
    # print newRes[0].get('place_id')
    #return newRes[0].get('place_id')

def weather(city,proxies):
    APIkey = "55ff3c0e47d54e378e366a0becf697b5"
    URL = "https://api.weatherbit.io/v2.0/forecast/daily?city="+ city +"&key="+APIkey

    connect = requests.post(URL,proxies=proxies)
    return connect.text
def Main():
    proxies = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'https://162.223.91.18:3128'
    }
    adres = raw_input("enter city: ")
    AddressID = map(adres,proxies)
    weatherInfo = weather(adres,proxies)
    print ("WEATHER info :\n"+ weatherInfo)
    print ("GEO info :\n"+ AddressID)

if __name__ == '__main__':
    Main()