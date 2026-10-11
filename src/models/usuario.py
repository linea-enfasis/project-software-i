import hashlib
import hmac
import secrets


class Usuario:
    rol = "usuario"

    def __init__(
        self, id: int, nombre: str, contrasena: str, activo: bool = True
    ) -> None:
        self.id = id
        self.nombre = nombre
        self.activo = activo
        self._contrasena = self._cifrar(contrasena)
        self._sesion_iniciada = False

    @property
    def sesion_iniciada(self) -> bool:
        return self._sesion_iniciada

    def iniciar_sesion(self, contrasena: str) -> bool:
        if not self.activo or not self._verificar(contrasena):
            return False
        self._sesion_iniciada = True
        return True

    def cerrar_sesion(self) -> None:
        self._sesion_iniciada = False

    @staticmethod
    def _cifrar(contrasena: str, sal: str | None = None) -> str:
        sal = sal or secrets.token_hex(16)
        resumen = hashlib.scrypt(
            contrasena.encode(), salt=bytes.fromhex(sal), n=2**14, r=8, p=1
        )
        return f"{sal}${resumen.hex()}"

    def _verificar(self, contrasena: str) -> bool:
        sal = self._contrasena.split("$")[0]
        return hmac.compare_digest(self._contrasena, self._cifrar(contrasena, sal))
