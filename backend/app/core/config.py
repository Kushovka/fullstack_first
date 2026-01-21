import os


class Settings:
    DB_USER = os.getenv("POSTGRES_USER", "dev")
    DB_PASS = os.getenv("POSTGRES_PASSWORD", "dev")
    DB_HOST = os.getenv("POSTGRES_HOST", "db")
    DB_PORT = os.getenv("POSTGRES_PORT", "5432")
    DB_NAME = os.getenv("POSTGRES_DB", "testdb")

    @property
    def DB_URL(self) -> str:
        return (
            f"postgresql+psycopg://{self.DB_USER}:"
            f"{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
