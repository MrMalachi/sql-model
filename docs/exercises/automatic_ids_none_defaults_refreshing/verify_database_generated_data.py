from sqlmodel import Field, Session, SQLModel, create_engine


class Mix(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    artist: str
    duration: int
    genre: str


sqlite_url = "sqlite:///weebtrax_archive.db"
engine = create_engine(sqlite_url, echo=True)


def create_tables_and_database():
    SQLModel.metadata.create_all(engine)

def main():
    create_tables_and_database()

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

        print("Before session:")
        print(f"ID: {mix_1.id}")

        session.add(mix_1)

        print("After add:")
        print(f"ID: {mix_1.id}")

        session.commit()

        print("After commit:")
        print(f"ID: {mix_1.id}")

        session.refresh(mix_1)

        print("After refresh:")
        print(f"ID: {mix_1.id}")



if __name__ == "__main__":
    main()