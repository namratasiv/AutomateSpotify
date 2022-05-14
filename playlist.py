import json
import requests
from secrets import spotify_user_id as user_id, spotify_token as token
class Playlist:
    def __init__(self):
        pass
    def createPlaylist(self):
        request_body = json.dumps({
            "name": "My liked Videos",
            "description": "From YouTube",
            "public": False
                })
        query = "https://api.spotify.com/v1/users/{user_id}/playlists".format(user_id=user_id)
        response = requests.post(
            query,
            data=request_body,
            headers={"Content-Type": "application/json",
            "Authorization": "Bearer {}".format(token)}
        )
        response_json = response.json()
        
        return response_json["id"]
    
    def getYPlaylist(self):
        pass
    def findSongs(self,song,artist):
        
        
    def addtoSpotify(self):
        pass
    def getYClient(self):
        pass