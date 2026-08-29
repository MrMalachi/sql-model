from sqlmodel import Field, Session, SQLModel, create_engine, select


class Mix(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    artist: str
    duration: int
    genre: str


sqlite_url = "sqlite:///weebtrax.db"
connect_args = {"check_same_thread": False, "timeout": 30}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_tables_and_database():
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        mix_1 = Mix(
            title="Neon Tokyo",
            artist="WeebTrax",
            duration=4100,
            genre="Lo-Fi House"
        )

        mix_2 = Mix(
            title="Midnight Drive",
            artist="Kiffen Beats",
            duration=3800,
            genre="Lo-Fi House"
        )

        mixes = [mix_1, mix_2]

        for mix in mixes:
            session.add(mix)

        session.commit()

def select_mixes():
    with Session(engine) as session:
        mixes = session.exec(select(Mix)).all()

        for mix in mixes:
            print(f"{mix.id} - {mix.title} - {mix.artist} - {mix.duration} - {mix.genre}")

def main():
    create_tables_and_database()
    select_mixes()

if __name__ == "__main__":
    main()