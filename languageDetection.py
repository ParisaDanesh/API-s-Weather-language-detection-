import requests

access_key = "67144a8028f243a4ab736acaf1c53ba0"
URL = "http://apilayer.net/api/detect?access_key="+access_key

query = "english"


data = {
    # 'access_key' : access_key,
    'query' : query
    # 'show_query' : 1
    # 'format' : 1
}
proxies = {
    'http' : 'socks5://127.0.0.1:9050',
    'https' : 'https://162.223.91.18:3128'
}
connect = requests.post(URL,data=data,proxies=proxies)

print connect.text
