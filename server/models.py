#models.py 
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String, DateTime, Boolean, Numeric
from typing import List
from datetime import datetime

# Declaring Base
class Base(DeclarativeBase):
	pass

#Declaring Mapped Table Artists
class Artists(Base):
	__tablename__ = "artists"

	artistId = mapped_column(Integer, primary_key = True)
	name = mapped_column(String(120))
	albums:Mapped[List["Albums"]] = relationship(back_populates = "artists")

#Declaring Mapped Table Albums
class Albums (Base):
	__tablename__ = "albums"

	albumId = mapped_column(Integer, primary_key = True)
	title = mapped_column(String(160), nullable = False)
	artistId = mapped_column(Integer, ForeignKey("artists.artistId"), nullable = False)
	artists:Mapped["Artists"] = relationship(back_populates = "albums")
	tracks:Mapped["Tracks"] = relationship(back_populates = "albums")

#Declaring Mapped Table Tracks
class Tracks(Base):
	__tablename__ = "tracks"

	trackId = mapped_column(Integer, primary_key = True)
	name = mapped_column(String(200), nullable = False)
	albumId = mapped_column(Integer, ForeignKey("albums.albumId"), nullable = False)
	albums:Mapped[List["Albums"]] = relationship(back_populates = "tracks")
