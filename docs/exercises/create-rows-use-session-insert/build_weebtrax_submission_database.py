from sqlmodel import Field, Session, SQLModel, create_engine


class TrackSubmission(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    artist: str
    title: str
    genre: str
    bpm: int


sqlite_url = "sqlite:///weebtrax_submissions.db"
engine = create_engine(sqlite_url, echo=True)


def create_tables_and_database():
    SQLModel.metadata.create_all(engine)

def main():
    create_tables_and_database()

    with Session(engine) as session:

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
            bpm=124
        )

        submission_4 = TrackSubmission(
            artist="Sora",
            title="Neon City",
            genre="House",
            bpm=124
        )

        session.add(submission_1)
        session.add(submission_2)
        session.add(submission_3)
        session.add(submission_4)

        session.commit()

        session.refresh(submission_1)
        session.refresh(submission_2)
        session.refresh(submission_3)
        session.refresh(submission_4)

        print("Display each submission's generated ID:")
        print(f"Submission 1: {submission_1.id}")
        print(f"Submission 2: {submission_2.id}")
        print(f"Submission 3: {submission_3.id}")
        print(f"Submission 4: {submission_4.id}")


if __name__ == "__main__":
    main()