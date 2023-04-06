import googleapiclient.discovery
from privateKey import *

api_service_name = "youtube"
api_version = "v3"
developer_key = apiKey

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=apiKey)

def breakLine():
    print("\n")

request_gema = youtube.videos().list(
    part = 'snippet,contentDetails,statistics',
    id = 'vA7DyyWpvgk'
)

request_estrogenio = youtube.videos().list(
    part ='snippet,contentDetails,statistics',
    id = 'JUVXsS8k5qs'
)

def gemaRequest():
    response_views = request_gema.execute()
    return response_views['items'][0]['statistics']['likeCount']

response_estrogenio = request_estrogenio.execute()
print("Título do vídeo:", response_estrogenio['items'][0]['snippet']['title'])
response_estrogenio = request_estrogenio.execute()
print("Número de views:", response_estrogenio['items'][0]['statistics']['viewCount'])
response_estrogenio = request_estrogenio.execute()
print("Número de likes:", response_estrogenio['items'][0]['statistics']['likeCount'])
breakLine()
response_name = request_gema.execute()
print("Título do vídeo:", response_name['items'][0]['snippet']['title'])
response_views = request_gema.execute()
print("Número de views:", response_views['items'][0]['statistics']['viewCount'])
print(gemaRequest())