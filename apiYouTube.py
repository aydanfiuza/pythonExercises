import googleapiclient.discovery
from privateKey import *

api_service_name = "youtube"
api_version = "v3"
developer_key = apiKey

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=apiKey)

request_views = youtube.videos().list(
    part = 'snippet,contentDetails,statistics',
    id = 'vA7DyyWpvgk'
)

request_name = youtube.videos().list(
    part = 'snippet,contentDetails,statistics',
    id = 'vA7DyyWpvgk'
)

response_name = request_name.execute()
print("Título do vídeo:", response_name['items'][0]['snippet']['title'])

response_views = request_views.execute()
print("Número de views:", response_views['items'][0]['statistics']['viewCount'])