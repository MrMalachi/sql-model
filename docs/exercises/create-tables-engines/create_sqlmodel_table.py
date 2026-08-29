from sqlmodel import Field, SQLModel


class Mix(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    artist: str
    duration: int
    genre: str


