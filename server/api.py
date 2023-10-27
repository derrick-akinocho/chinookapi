#api.py
import sqlalchemy

from fastapi import FastAPI
from sqlalchemy import select, func, update
from models import Artists, Albums, Tracks
from database import session

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World"}

# To display album names corresponding to an artist
@app.get("/albums/")
async def getAlbum(artistId: int):

    statement = select(Albums).join(Albums.artists).where(Artists.artistId == artistId)
    res = tuple(session.scalars(statement).all())

    return res


# To display artists with the same name
@app.get("/artists/")
async def getArtist(name: str):

    artistName = f"%{name}%"
    res = tuple(session.query(Artists).filter(func.lower(Artists.name).like(artistName.lower())).all())

    return res

#To display track names corresponding to an album
@app.get("/tracks/")
async def getTracks(albumId: int):

    statement = select(Tracks).join(Tracks.albums).where(Albums.albumId == albumId)
    res = tuple(session.scalars(statement).all())

    return res

# Close session
session.close()