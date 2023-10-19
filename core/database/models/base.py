from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
import inflect

plur = inflect.engine()


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return plur.plural(cls.__name__.lower())

    id: Mapped[int] = mapped_column(primary_key=True)
