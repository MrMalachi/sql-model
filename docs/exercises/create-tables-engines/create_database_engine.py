from sqlmodel import Field, SQLModel, create_engine


class Mix(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    artist: str
    duration: int
    genre: str


sqlite_url = "sqlite:///weebtrax.db"
engine = create_engine(sqlite_url, echo=True)