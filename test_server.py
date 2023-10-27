#test_server.py
import requests

# URL of HTTP request to web API.
url = "http://127.0.0.1:8000/"

#Test the query if status = 200 and results are correct
def testgetAlbum():
    query = requests.get(url + "albums/?artistId=3")

    assert query.status_code == 200
    assert query.json() == [{"albumId": 5,"title": "Big Ones","artistId": 3}]

#Test the query if status = 200 and results are correct
def testgetArtist():
    query = requests.get(url + "artists/?name=kiss")

    assert query.status_code == 200
    assert query.json() == [{"artistId": 52,"name": "Kiss"}]

#Test the query if status = 200 and results are correct
def testgetTracks():
    query = requests.get(url + "tracks/?albumId=3")

    assert query.status_code == 200
    assert query.json() == [{"name":"Fast As a Shark","trackId":3,"albumId":3},{"name":"Restless and Wild","trackId":4,"albumId":3},{"name":"Princess of the Dawn","trackId":5,"albumId":3}]