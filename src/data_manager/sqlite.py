from typing import Any, Generator, Optional, Type
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from data_manager.storage import DataStorageInterface
from models.assets import reg, Asset


class SQLAlchemyDataStorage(DataStorageInterface):
    def __init__(self, db_url: str = "sqlite+pysqlite:///:memory:"):
        self.engine = create_engine(db_url, echo=True)
        self.session_factory = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def create_tables(self):
        reg.metadata.create_all(self.engine)

    @contextmanager
    def get_db(self) -> Generator[Session, None, None]:
        db = self.session_factory()
        try:
            yield db
        finally:
            db.close()

    def store_data(self, model_instance: Any) -> None:
        with self.get_db() as db:
            db.add(model_instance)
            try:
                db.commit()
            except Exception as e:
                db.rollback()
                raise e

    def retrieve_data(
        self, model_class: Type[Asset], identifier: Any
    ) -> Optional[Asset]:
        with self.get_db() as db:
            result = db.query(model_class).filter_by(id=identifier).first()
            return result

    def add(self, db: Session, obj: Any) -> Any:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def query(self, db: Session, model, *criteria) -> list:
        return db.query(model).filter(*criteria).all()

    def update(self, db: Session, obj: Any, **kwargs) -> Any:
        for key, value in kwargs.items():
            setattr(obj, key, value)
        db.commit()
        return obj

    def delete(self, db: Session, obj: Any) -> None:
        db.delete(obj)
        db.commit()
