from sqlmodel import Field, Session, SQLModel, create_engine


class Mix(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    artist: str
    duration: int
    genre: str


sqlite_url = "sqlite:///weebtrax.db"
engine = create_engine(sqlite_url, echo=True)


def create_tables_and_database():
    SQLModel.metadata.create_all(engine)

def main():
    create_tables_and_database()

    with Session(engine) as session:
        mix_1 = Mix(
            title="Midnight Tokyo",
            artist="DJ Neko",
            duration=2520,
            genre="Lo-Fi House"
        )

        mix_2 = Mix(
            title="Neon Dreams",
            artist="Yume",
            duration=3300,
            genre="Lo-Fi House"
        )

        mix_3 = Mix(
            title="Digital Rain",
            artist="DJ Kuro",
            duration=2280,
            genre="Ambient House"
        )

        session.add(mix_1)
        session.add(mix_2)
        session.add(mix_3)

        session.commit()

        session.refresh(mix_1)
        session.refresh(mix_2)
        session.refresh(mix_3)

        print("Display each mix's generated ID:")
        print(f"Mix 1: {mix_1.id}")
        print(f"Mix 2: {mix_2.id}")
        print(f"Mix 3: {mix_3.id}")


if __name__ == "__main__":
    main()