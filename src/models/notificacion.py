from datetime import datetime
from enum import Enum

from .administrador import Administrador


class TipoNotificacion(str, Enum):
    DEFECTO = "defecto"
    FALLA = "falla"
    AGOTAMIENTO = "agotamiento"


class Notificacion:
    def __init__(
        self,
        id: int,
        tipo: TipoNotificacion,
        mensaje: str,
        destinatario: Administrador,
        fecha: datetime | None = None,
        leida: bool = False,
    ) -> None:
        self.id = id
        self.tipo = tipo
        self.mensaje = mensaje
        self.destinatario = destinatario
        self.fecha = fecha or datetime.now()
        self.leida = leida

    def marcar_leida(self) -> None:
        self.leida = True
