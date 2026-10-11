from .usuario import Usuario
from .tecnico import Tecnico


class Administrador(Usuario):
    rol = "administrador"

    def gestionar_cuenta_tecnico(self, tecnico: Tecnico, activo: bool) -> None:
        tecnico.activo = activo
        if not activo:
            tecnico.cerrar_session()
