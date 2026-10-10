# Taller 5 · Diagrama de clases

- **Entrega:** en el **repositorio del equipo en GitHub**, diligenciando el enunciado con los puntos 2, 3 y 4 y subiendo el diagrama al repositorio *(imagen exportada o fuente PlantUML/draw.io)*.
- **Requisito previo:** diagrama de casos de uso del Taller 4.
- Herramienta: draw.io, PlantUML, StarUML o Visual Paradigm.

---

## 1. Guía mínima

**Diagrama de clases:** vista estructural del sistema. Muestra qué cosas existen en el dominio, qué datos guardan, qué saben hacer y cómo se relacionan. No muestra orden ni tiempo: eso es de los diagramas de secuencia.

### Clase

```bash
┌──────────────────────┐
│       Turno          │  ← nombre: sustantivo singular, del vocabulario del dominio
├──────────────────────┤
│ - fecha: Fecha       │  ← atributos: visibilidad nombre: tipo
│ - estado: EstadoTurno│
├──────────────────────┤
│ + cancelar(): void   │  ← métodos: visibilidad nombre(parámetros): retorno
└──────────────────────┘
```

- **Visibilidad:** `+` pública, `-` privada, `#` protegida, `~` de paquete. Los atributos van privados por defecto.
- En el **modelo de dominio** se pueden omitir los métodos: importan los conceptos, sus datos y sus relaciones.
- Una clase **no es una pantalla, una tabla ni un botón**. `PantallaLogin` o `BotonGuardar` no son conceptos del dominio.

### Relaciones

| Relación        | Notación                                  | Se lee                           | Ejemplo                  |
| --------------- | ----------------------------------------- | -------------------------------- | ------------------------ |
| **Asociación**  | línea simple                              | "A se relaciona con B"           | Cliente — Turno          |
| **Agregación**  | rombo vacío en el todo                    | "A tiene B, pero B existe sin A" | Barbería ◇— Barbero      |
| **Composición** | rombo lleno en el todo                    | "B es parte de A y muere con A"  | Factura ◆— LíneaFactura  |
| **Herencia**    | flecha con triángulo vacío hacia el padre | "B es un tipo de A"              | Usuario ◁— Administrador |
| **Dependencia** | flecha punteada                           | "A usa a B de paso"              | Reporte ⇢ Turno          |

- Ante la duda entre agregación y composición: si al borrar el todo **las partes no tienen sentido solas**, es composición.
- Herencia solo si el hijo **es un** padre y comparte su comportamiento. Si solo comparten un campo, no es herencia.

### Multiplicidad

Se escribe en cada extremo de la relación: cuántos objetos de ese lado se relacionan con **uno** del otro.

| Notación | Significa |
| --- | --- |
| `1` | exactamente uno |
| `0..1` | cero o uno |
| `*` o `0..*` | cero o muchos |
| `1..*` | uno o muchos |

- `Cliente 1 —— 0..* Turno`: un cliente tiene cero o muchos turnos; cada turno es de exactamente un cliente.
- Una relación sin multiplicidad está incompleta.

### Navegabilidad

- Flecha abierta en un extremo: desde A se llega a B, pero no al revés.
- En el modelo de dominio se puede dejar sin flecha *(bidireccional)*; se decide en el diseño.

### Cómo encontrar las clases

1. Subrayar los **sustantivos** del catálogo de requisitos y de las descripciones de los casos de uso.
2. Descartar sinónimos, atributos disfrazados *(el "nombre" no es una clase)*, actores que no guardan datos y cosas fuera del alcance.
3. Lo que queda son **clases candidatas**. Los **verbos** entre ellas sugieren relaciones.

---

## 2. Clases candidatas
| Clase candidata | Fuente *(RF o caso de uso)* | ¿Se queda? | Por qué |
| --- | --- | --- | --- |
| Usuario | RF-01, RF-10, RF-16, CU-01 | Sí | Es quien ingresa con contraseña; es el padre común de administrador y técnico |
| Administrador | RF-02, RF-03, RF-13, RF-15, CU-03, CU-04 | Sí | Crea asignaciones, confirma devoluciones y revisa defectos; guarda datos en el sistema |
| Técnico | RF-04, RF-05, RF-08, RF-14, CU-05, CU-06 | Sí | Recibe material, lo consume, lo devuelve y reporta defectos |
| Material | RF-02, RF-06, RF-11, CU-03 | Sí | Concepto central del dominio: tiene código, stock y estado |
| Asignación | RF-03, RF-14, CU-04 | Sí | Registra la entrega de material a un técnico |
| DetalleAsignación | RF-03, CU-04 | Sí | Cada material y cantidad dentro de una asignación |
| Consumo | RF-04, RF-07, CU-05 | Sí | Es el "material gastado"; tiene fecha y cantidad |
| Devolución | RF-05, RF-15, CU-06, CU-07 | Sí | Tiene estado (pendiente/confirmada) y fecha |
| DetalleDevolución | RF-05, CU-06 | Sí | Cada material y cantidad devuelta; no existe sin la devolución |
| ReporteDefecto | RF-08, RF-13, CU-08, CU-09 | Sí | Son los "elementos defectuosos"; tiene descripción y estado de revisión |
| Notificación | RF-11, RF-12, CU-11 | Sí | Alerta al administrador; guarda mensaje y tipo |
| MovimientoMaterial | RF-09, RF-16, CU-10 | Sí | Es el historial: fecha, hora, tipo, cantidad y responsable |
| Material gastado | RF-04, RF-07 | No | Sinónimo de Consumo |
| Elementos defectuosos | RF-08, RF-13 | No | Es el nombre usado en el RF; la clase es ReporteDefecto |
| Fecha, hora | RF-16 | No | Son atributos de MovimientoMaterial |
| Recepción | RF-15 | No | Es el estado "confirmada" de Devolución |
| Historial de movimientos | RF-09 | No | Es la lista de MovimientoMaterial: una consulta, no una clase |
| Inventario | RF-06 | No | Es una consulta sobre Material, no un concepto con datos propios |

- **Mínimo 6 clases** que se quedan.
- Toda clase lleva fuente. Una clase que no sale de ningún requisito o caso de uso no está en el alcance.


## 3. Diagrama de clases del dominio

Un solo diagrama con:

- **Mínimo 6 clases**, con atributos y tipos.
- **Mínimo 5 relaciones**, cada una con multiplicidad en los dos extremos.
- Al menos **una composición o agregación** y, si el dominio lo justifica, una **herencia**.
- Nombres en el vocabulario del dominio *(el que salió de la elicitación del Taller 3)*.
- Si el proyecto tiene componente de IA, la **entidad que guarda el resultado** del modelo *(e.g. `SugerenciaIA` con fecha, entrada, salida y estado)*. El servicio que llama a la API **no** va en este taller.

**Imagen o enlace al diagrama:** *(completar)*

@startuml
title Diagrama de clases - Gestion de material

skinparam classAttributeIconSize 0
skinparam linetype ortho
skinparam nodesep 90
skinparam ranksep 110
skinparam shadowing false
skinparam ArrowColor #333333
skinparam ArrowThickness 1.5
skinparam class {
  BackgroundColor #DAE3F3
  BorderColor #4A86C5
  FontSize 14
  AttributeFontSize 12
}
skinparam class<<ia>> {
  BackgroundColor #E2F0D9
  BorderColor #70AD47
}

' ===== FILA 1: clase padre =====
class Usuario {
  - id : int
  - nombre : String
  - contrasena : String
  - activo : boolean
  + iniciarSesion() : boolean
  + cerrarSesion() : void
  + verMaterialGastado() : List<Asignacion>
}

' ===== FILA 2: actores =====
class Administrador {
  + ingresarMaterial(material : Material) : void
  + asignarMaterial(tecnico : Tecnico, material : Material, cantidad : int) : Asignacion
  + verMaterialGeneral() : List<Material>
  + verHistorial() : List<Asignacion>
  + gestionarCuentaTecnico(tecnico : Tecnico, activo : boolean) : void
  + recibirNotificacion() : void
}

class Tecnico {
  + consultarMaterialAsignado() : List<Asignacion>
  + recibirMaterial(asignacion : Asignacion) : void
  + devolverMaterial(material : Material, cantidad : int) : Devolucion
  + devolverMaterialDefectuoso(material : Material, descripcion : String) : ReporteDefecto
}

class AgenteIA <<ia>> {
  - nombre : String
  + predecirAgotamiento(material : Material) : boolean
  + notificarMaterialPorAgotarse(material : Material) : Notificacion
  + consultarHistorial(material : Material) : List<Asignacion>
  + analizarReporte(reporte : ReporteDefecto) : String
  + notificarDictamen(reporte : ReporteDefecto) : Notificacion
}

' ===== FILA 3: clases de datos =====
class Material {
  - codigo : String
  - nombre : String
  - stock : int
  - stockMinimo : int
  - estado : String
}

class Asignacion {
  - fecha : Date
  - fechaLimiteDevolucion : Date
  - cantidadAsignada : int
  - cantidadGastada : int
}

class Devolucion {
  - fecha : Date
  - cantidad : int
  - estado : String
}

class Notificacion <<ia>> {
  - id : int
  - tipo : String
  - mensaje : String
  - fecha : Date
  - leida : boolean
}

' ===== FILA 4 =====
class ReporteDefecto {
  - fecha : Date
  - descripcion : String
  - fotos : List<String>
  - dictamen : String
  - estado : String
}

' ===== Herencia =====
Usuario <|-down- Administrador
Usuario <|-down- Tecnico

' ===== Administrador (lado izquierdo) =====
Administrador "1" -down-> "0..*" Material
Administrador "1" -down-> "0..*" Asignacion

' ===== Tecnico (lado derecho) =====
Asignacion "0..*" -up-> "1" Tecnico
Tecnico "1" -down-> "0..*" Devolucion
Tecnico "1" -down-> "0..*" ReporteDefecto

' ===== Relaciones entre clases de datos =====
Material "1" -right- "0..*" Asignacion
Asignacion "1" -right- "0..*" Devolucion
Material "1" -down- "0..*" ReporteDefecto

' ===== Agente de IA (segundo actor) =====
AgenteIA "1" -right-> "1" Administrador : notifica
AgenteIA "1" -down-> "0..*" Notificacion : genera
AgenteIA ..> Asignacion : consulta
AgenteIA ..> ReporteDefecto : analiza

' ===== Ayudas de orden =====
Material -[hidden]right- Asignacion
Asignacion -[hidden]right- Devolucion
Asignacion -[hidden]down- ReporteDefecto
Administrador -[hidden]right- Tecnico
AgenteIA -[hidden]right- Administrador
Notificacion -[hidden]right- Material
@enduml


## 4. Trazabilidad y dudas

**Columna de clase de la matriz**

| Requisito | Caso de uso | Clase(s) |
| --------- | ----------- | -------- |
| RF-01 | CU-01 Iniciar sesión | Usuario, Administrador, Técnico |
| RF-02 | CU-03 Registrar ingreso de material | Administrador, Material, MovimientoMaterial |
| RF-03 | CU-04 Asignar material a técnico | Administrador, Técnico, Asignación, DetalleAsignación, Material |
| RF-04 | CU-05 Consultar material consumido | Técnico, Consumo, Material |
| RF-05 | CU-06 Devolver material | Técnico, Devolución, DetalleDevolución, Material |
| RF-06 | CU-12 Consultar inventario general | Administrador, Material |
| RF-07 | CU-05 Consultar material consumido | Técnico, Consumo, Material |
| RF-08 | CU-08 Reportar material defectuoso | Técnico, ReporteDefecto, Material |
| RF-09 | CU-10 Consultar historial de movimientos | Administrador, MovimientoMaterial |
| RF-10 | CU-02 Gestionar cuentas de técnicos | Administrador, Usuario, Técnico |
| RF-11 | CU-11 Recibir notificaciones | Administrador, Notificación, Material, ReporteDefecto |
| RF-12 | CU-11 Recibir notificaciones | Administrador, Notificación |
| RF-13 | CU-09 Revisar reporte de defecto | Administrador, ReporteDefecto |
| RF-14 | CU-05 Consultar material asignado | Técnico, Asignación, DetalleAsignación, Material |
| RF-15 | CU-07 Confirmar recepción de devolución | Administrador, Devolución, DetalleDevolución |
| RF-16 | CU-10 Consultar historial de movimientos | MovimientoMaterial, Usuario |

- Cada caso crítico se apoya en al menos una clase del diagrama:
  - CU-01 Iniciar sesión → Usuario, Administrador, Técnico.
  - CU-04 Asignar material → Asignación, DetalleAsignación, Material.
  - CU-06 Devolver material → Devolución, DetalleDevolución, Material.
  - CU-08 Reportar material defectuoso → ReporteDefecto, Material, Notificación.


**Dudas para la siguiente clase** *(lo que el equipo no pudo resolver solo)*:
  - pregunta del punto 3 diagrama 

## Ejemplo diligenciado

**2. Candidatas**

| Clase candidata | Fuente            | ¿Se queda? | Por qué                                                                   |
| --------------- | ----------------- | ---------- | ------------------------------------------------------------------------- |
| Cliente         | RF-01             | Sí         | Reserva y tiene turnos                                                    |
| Turno           | RF-01, CU-01      | Sí         | Concepto central del dominio                                              |
| Barbero         | RF-02             | Sí         | Atiende turnos; tiene agenda                                              |
| Agenda          | P1 *(entrevista)* | No         | Es la lista de turnos de un barbero en un día: una consulta, no una clase |
| CierreCaja      | RF-05             | Sí         | Guarda el total del día                                                   |
| Teléfono        | RF-01             | No         | Es un atributo de Cliente                                                 |

**3. Diagrama** *(extracto en PlantUML)*

![img](/docs/diagramas/diagrama-gestion-material.png)

**4. Trazabilidad:** RF-01 → CU-01 Reservar turno → Cliente, Turno, Barbero. RF-02 → CU-02 Marcar no asistido → Turno *(estado)*.
