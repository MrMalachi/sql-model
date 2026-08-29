from sqlmodel import Field, SQLModel, create_engine


class Mix(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    artist: str
    duration: int
    genre: str


class TrackSubmission(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    artist: str
    title: str
    bpm: int
    file_name: str


sqlite_url = "sqlite:///weebtrax.db"
engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def main():
    create_db_and_tables()


if __name__ == "__main__":
    main()