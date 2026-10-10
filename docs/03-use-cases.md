# Taller 4 · Casos de uso

Se trabaja en clase, por equipo.

- **Entrega:** en el **repositorio del equipo en GitHub**, diligenciando el enunciado con los puntos 1 a 5 y subiendo el diagrama al repositorio *(imagen exportada o fuente PlantUML/draw.io)*.
- Herramienta: draw.io, PlantUML, StarUML o Visual Paradigm.

---

## 1. Actores y casos

| Actor | Tipo | Principal o secundario | Objetivo |
| Administrador | Humano | Principal | Administrar usuarios de tecnico y recursos del inventario |
| Tecnico | Humano | Principal | Manejo de material asignado  |
| Proveedor de IA | Sistema externo | Secundario | Ayudar con sugerencias cuando el material este desgastado |

- Roles, no personas. La base de datos y el servidor **no** son actores.
- Si el proyecto tiene componente de IA, el **proveedor del modelo** es un actor secundario.

**Casos de uso**

| ID    | Nombre *(verbo en infinitivo + objeto)* | Actor principal | RF que cubre |
| ----- | --------------------------------------- | --------------- | ------------ |
| CU-01 | *(Visualización de material gastado)*      |*(Administrador)*| *(RF-04)*    |
| CU-02 | *(Ingreso del materiales)*              |*(Administrador)*| *(RF-02)*    |
| CU-03 | *(Devolucion de materiales)*            |*(Tecnicos)*     | *(RF-05)*    |
| CU-04 | *(Devolucion de materiales defectuosos)*|*(Tecnicos)*     | *(RF-08)*    |
| CU-05 | *(Ingreso y revision del historial)*    |*(Administrador)*| *(RF-09)*    |
| CU-06 | *(Manejo de las cuentas de tecnicos)*   |*(Administrador)*| *(RF-10)*    |
| CU-07 | *(Visualización del material gastado)*     |*(Tecnico)*      | *(RF-07)*    |
| CU-08 | *(la asignacion del material a los tecnicos )* |*(Administrador)* | *(RF-3)*   |


- **Mínimo 6 casos**, todos con al menos un RF.

---

## 2. Diagrama de casos de uso

Un solo diagrama con:

- **Límite del sistema** CU-01 `«include»` CU-02,CU-03, esto ya que en la visulacion del material aparecen los devueltos. CU-08 `«include»` CU-03, CU-04, CU-07, esto ya que para consultar el material se debe tener en cuenta lo devuelto ya sea por no uso o defectuoso
CU-05 `«include»` CU-02,CU-03,CU-04,CU-07 ya que todo movimiento queda registrado.

**Imagen o enlace al diagrama:** <<link>>

![img](/docs/diagramas/caso_uso_ingreso.jpeg)
![img](/docs/diagramas/caso_uso_administrador.jpeg)
![img](/docs/diagramas/caso_uso_tecnico.jpeg)

## 3. Casos críticos

Los tres casos que el prototipo implementa **de punta a punta** *(de la interfaz a la persistencia)*.

| Caso      | Por qué es crítico *(valor / frecuencia / riesgo técnico)* |
| --------- | ---------------------------------------------------------- |
| *(CU-1#)* | *(Visualización del material general gastado /no existe limite para visualización/No asigna lugar de almacenamiento del material, solo se sabe que hay x candidad.)*                                              |
| *(CU-4#)* | *(Devolucion de materiales defectuosos/limite de tiempo/Despues de 2 dias de asignado material no es valida devolucion, ya que el tecnico debe revisar material cuando lo recibe)*                                              |
| *(CU-8#)* | *(Asignacion de material por parte del administrador/1 vez al dia/El tecnico tiene un limite de espacio para asignacion de material. Y para recibir nuevo material, debe de haber gastado mas del 80% o debe realizar devolucion del mismo para nueva asignacion)*                                              |

- **Máximo uno** puede ser el caso de IA; los otros dos son funcionalidad con persistencia propia.
- No valen iniciar sesión.

---

## 4. Descripción detallada de los casos críticos

Una tabla por caso crítico.
| Campo | Contenido |
| --- | --- |
| **Actor principal** | Administrador |
| **Actores secundarios** | Tecnicos|
| **Requisitos** | RF-01, RF-16 *(Asignacion del material, debe registar fecha, hora y usuario responsable)* |
| **Precondiciones** | Si tecnico no le han asignado material en el dia y haya gastado mas del 80% del mismo |
| **Disparador** | El sistema muestra los tecnicos disponible para asignacion de material |
| **Frecuencia** | Una vez al día |

1. El administrador asigna material a los tecnicos
2. El sistema solo deja asignar material si hay suficiente en bodega, debe haber el tecnico consumido el 80% del asignado la ultima vez, no haya recibido material ese dia.
3. El sistema solo le muestra al administrador los tecnicos que cumplan con la condicion del punto 2, para poder asignar material
4. El administrador intenta seleccinar manualmente el tecnico para asignar material, pero si no cumple 1 de cualquiera de las condiciones del punto 2, genera error, le aparece(no es posible ejecutar la accion, no cumple con las condiciones establecidas y luego lo retorna al menu principal)
5. El sistema muestra una tabla de los tecnicos prontos a solicitar material y los que tienen el almacen más lleno de menor a mayor 
6. El administrador para asignar material, selecciona el tecnico, ademas debe poner fecha y hora de asignacion, tipo de material y cantidad.
7. El sistema guarda los datos y devuelve mensaje "material asignado correctamente".

- **2a.** si el sistema no cuenta con material suficiente material cargado en bodega, no deja asignar material.
- **3a.** si el sistema identifica que el tecnico no ha consumido el 80%  del material asignado la ultima vez o haya recibido material ese dia, el sistema no muestra al administrador ese tecnico para asignar material
- **4a.** *(excepción)* si el administrador ingresa datos incorrectos o asigna material a tecnico que no cumple las condiciones del punto 2, devuelve HTTP 400: el sistema informa que no es posible ejecutar la accion y retorna al menu principal nuevamente

**Postcondiciones.** Éxito: cada tecnico solo puede solicitar material 1 solo vez al dia

---

## 5. Trazabilidad

//pregunta al profesor  

**Columna de caso de uso de la matriz** *()*:

**Columna de caso de uso de la matriz (la que se abrió en la Clase 3):

Requisito	Fuente	Caso de uso
RF-01	(P# o documento)	(CU-0#)
…		
Huecos detectados:

Hueco	Cuál	Qué se hace
RF sin caso de uso	(completar o "ninguno")	(se crea el caso / el RF sale del catálogo)
Caso de uso sin RF	(completar o "ninguno")	(se agrega el RF / el caso sale del alcance)
Todo lo que cambie el catálogo va al registro de control de cambios de la bitácora.

---

## Ejemplo diligenciado

Referencia de nivel de detalle. Mismo dominio de los talleres anteriores: **no se puede usar.**

**1. Actores** *(barbería; extracto)*

| Actor | Tipo | Principal o secundario | Objetivo |
| --- | --- | --- | --- |
| Cliente | Humano | Principal | Conseguir un turno sin llamar |
| Barbero | Humano | Principal | Saber a quién atiende y registrar quién no llegó |
| Dueño | Humano *(hereda de Barbero)* | Principal | Cerrar caja y mantener la clientela |
| Proveedor de IA | Sistema externo | Secundario | Redactar el texto del recordatorio |

**1. Casos** *(extracto)*

| ID | Nombre | Actor principal | RF |
| --- | --- | --- | --- |
| CU-01 | Reservar turno | Cliente | RF-01 |
| CU-02 | Consultar franjas libres | Cliente | RF-01 |
| CU-03 | Cancelar turno | Cliente | RF-04 |
| CU-05 | Marcar turno no asistido | Barbero | RF-02 |
| CU-06 | Cerrar caja del día | Dueño | RF-05 |
| CU-07 | Redactar recordatorio con IA | Dueño | RF-08 |

**2. Relaciones:** CU-01 `«include»` CU-02, porque toda reserva pasa por consultar las franjas y el cliente también las consulta sin reservar. Dueño hereda de Barbero, porque el dueño también atiende una silla.

**3. Críticos**

| Caso                               | Por qué                                                                                                                |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| CU-01 Reservar turno               | Es el problema que se tiene es: el teléfono no para los sábados; ~40 al día; riesgo de dos reservas en la misma franja |
| CU-06 Cerrar caja del día          | Todos los días; cálculo sobre los turnos atendidos                                                                     |
| CU-07 Redactar recordatorio con IA | El caso de IA; reduce los no asistidos *(P6)*                                                                          |

**4. Descripción** *(CU-07; CU-01 está completo en la Sesión 5)*

| Campo | Contenido |
| --- | --- |
| **Actor principal** | Dueño |
| **Actores secundarios** | Proveedor de IA |
| **Requisitos** | RF-08, RNF-04 *(respuesta en menos de 10 s)* |
| **Precondiciones** | Hay turnos *Reservados* para el día siguiente |
| **Disparador** | El administrador programa recordatorio cuando el tecnico haya gastado 80% |
| **Frecuencia** | Una vez al día |

1. El dueño pide los recordatorios del día siguiente.
2. El sistema lista los turnos *Reservados* de mañana.
3. El sistema envía al proveedor de IA la franja, el barbero y el nombre de pila de cada cliente, **sin teléfono**.
4. El proveedor devuelve un borrador de mensaje por turno.
5. El sistema valida que cada borrador traiga fecha y franja, y los muestra marcados como *texto generado*.
6. El dueño revisa, edita si quiere y aprueba.
7. El sistema guarda los mensajes aprobados listos para enviar.

- **5a.** Un borrador no trae fecha o franja: se descarta y se usa la plantilla fija para ese turno. Vuelve al paso 6.
- **6a.** El dueño descarta un borrador: el sistema usa la plantilla fija para ese turno. Vuelve al paso 6.
- **4a.** *(excepción)* El proveedor no responde en 10 s o devuelve HTTP 429: el sistema informa que la IA no está disponible, registra el evento y ofrece la plantilla fija para todos. El caso termina sin texto generado.

**Postcondiciones.** Éxito: cada turno de mañana tiene un mensaje aprobado. Garantía mínima: ningún dato de contacto sale hacia el proveedor.

**5. Huecos:** RF-06 *(reporte mensual de ingresos)* sin caso → se crea CU-09 Consultar reporte mensual. CU-04 Avisar a la lista de espera sin RF → se agrega RF-11 y se registra en el control de cambios.
