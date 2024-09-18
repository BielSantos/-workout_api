
from workout_api.contrib.models import BaseModel
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import mapped_column, Mapped, relationship

class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column((String), unique=True, nullable= False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='categoria')