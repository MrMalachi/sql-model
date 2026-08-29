from sqlmodel import Field, Session, SQLModel, create_engine


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
    genre: str
    bpm: int


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


        submission_1 = TrackSubmission(
            artist="Aiko",
            title="Plastic Moon",
            genre="House",
            bpm=122
        )

        submission_2 = TrackSubmission(
            artist="Kaito",
            title="Tokyo Drive",
            genre="Lo-Fi House",
            bpm=120
        )

        submission_3 = TrackSubmission(
            artist="Rei",
            title="After Midnight",
            genre="Deep House",
            bpm=118
        )

        submission_4 = TrackSubmission(
            artist="Sora",
            title="Neon City",
            genre="House",
            bpm=124
        )

        session.add(mix_1)
        session.add(mix_2)
        session.add(mix_3)

        session.add(submission_1)
        session.add(submission_2)
        session.add(submission_3)
        session.add(submission_4)

        session.commit()

        session.refresh(mix_1)
        session.refresh(mix_2)
        session.refresh(mix_3)

        session.refresh(submission_1)
        session.refresh(submission_2)
        session.refresh(submission_3)
        session.refresh(submission_4)

        print("Display each mix:")
        print(f"Mix created: {mix_1.id} - {mix_1.title}")
        print(f"Mix created: {mix_2.id} - {mix_2.title}")
        print(f"Mix created: {mix_3.id} - {mix_3.title}")

        print("Display each submission's generated ID:")
        print(f"Submission created: {submission_1.id} - {submission_1.title}")
        print(f"Submission created: {submission_2.id} - {submission_2.title}")
        print(f"Submission created: {submission_3.id} - {submission_3.title}")
        print(f"Submission created: {submission_4.id} - {submission_4.title}")


if __name__ == "__main__":
    main()