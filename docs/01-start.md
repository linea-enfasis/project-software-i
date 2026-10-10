# Ficha de equipo y dominio — Sesión 1

Plantilla de la **actividad de cierre de la Clase 1**. Se diligencia en clase, en equipo, y se entrega al final de la sesión.

- **Equipos:** de 2 a 3 integrantes, fijos durante todo el curso.
- **Entrega:** una ficha por equipo.
- **Cada equipo elige un dominio distinto.**

---

## 1. Identificación del equipo

| Campo | Respuesta |
|---|---|
| Nombre del equipo | _(SISTEM INVENTARIOS Y GESTIÓN)_ |
| Fecha | _(25/09/2026)_ |

| # | Integrante | Correo | Rol / responsabilidad |
| --- | --- | --- | --- |
| 1 | _(JOHAN STIVEN HENAO MUÑOZ)_ | _(johanhenao932@gmail.com)_ | Coordinación _(lider)_ |
| 2 | _(JOSE FERNANDO SANCHEZ GARCIA)_ | _(312joselito@gmail.com)_ | _(desarrollador)_ |
| 3 | _(CRISTAN CAMILO CASTAÑO MONTES)_ | _(camilomontes11@gmail.com)_ | _(desarrollador)_ |

> El rol no es definitivo: se ajusta en la bitácora de gestión. Lo que sí queda fijo hoy es **JOHAN STIVEN HENAO MUÑOZ**.

---

## 2. Dominio propuesto

**Dominio:** _(GESTION Y CREACION DE SISTEMAS DE INVENTARIOS PARA UNA EMPRESA DE TELECOMUNICACIONES)_



**Problema que se quiere resolver** _(máximo tres líneas: qué pasa hoy, a quién le duele y por qué el proceso actual no alcanza)_:

_(¿Qué pasa hoy?
No se tiene una herramienta para gestionar los inventarios de los materiales asignados a los técnicos de telecomunicaciones

¿A quién le duele?
A la empresa prestadora de servicios, por la pérdida de materiales sin justificación por parte de los técnicos.

¿Por qué el proceso actual no alcanza?
•	Se evidencia mal manejo de materiales por parte de los técnicos.
•	Esto genera pérdidas injustificadas, incluso robos.
•	La empresa se queda sin materiales para asignar, afectando la operación.
•	Se produce un déficit financiero debido a la falta de control.)_

**Cómo se hace hoy sin software** _(o con qué herramienta improvisada: papel, WhatsApp, un Excel)_:

_(El proceso se realiza por medio de registros en papel, lo que dificulta la trazabilidad y el control.)_

---

## 3. Usuarios del sistema

| Tipo de usuario | Qué necesita hacer en el sistema | ¿Tenemos acceso para entrevistarlo? |
| --- | --- | --- |
| _(Administrador)_ | _(carga y visualizacion de inventario)_ | Sí / — _(JOHAN STIVN HENAO MUÑOZ)
| _(tecnicos)_ | _(carga de inventario)_ | Sí  — _(JOSE FERNANDO SANCHEZ GARCIA, CRISTIAN CAMILO CASTAÑO MONTES)_ |

> Al menos **un usuario real y accesible** es obligatorio: en la Clase 3 hay que hacerle una sesión de elicitación de verdad.
# No aplica porque no se cuenta con un usuario real para realizar la entrevista.
---

## 4. Capacidad del equipo

**¿Por qué este equipo puede levantar requisitos de este dominio?** _(acceso a usuarios reales, alguien trabaja o trabajó ahí, experiencia previa con el proceso, etc.)_

_(SI, ALGUEIN DE NUESTRO EQUIPO PRESENCIO ESTA PROBLEMATICA EN LA EMPRESA DONDE TRABAJA)_

---

## 5. Alcance tentativo

**Tres cosas que el sistema sí debe hacer**:

1. _(CARGA DE INVENTARIO)_
2. _(VISUALIZACION DEL INVENTARIO TOTAL)_
3. _(CARGA DE LOS ELEMENTOS EN EL INVENTARIO DE LOS GASTADO POR LOS TECNICOS )
4. _(HISTORIAL DE LAS MODIFICACIONES)

**Tres cosas que el sistema no va a hacer**:

1. _(NO REALIZA COMPRAS DE MATERIALES)_
2. _(NO REALIZA TRABAJOS TECNICOS)_
3. _(NO TIENE VISUALIZACION DEL ESTADO DE LOS MATERIALES)_

---

## 6. Autoverificación

- [ ] Hay **usuarios reales accesibles** para entrevistar en la Clase 3.
- [] El dominio da para **10 requisitos funcionales y 5 no funcionales** sin inventarlos.
- [X] Los **tres casos críticos** se ven implementables end-to-end en seis semanas.
- [ ] El proyecto **no fue desarrollado** en otra asignatura ni se está reciclando.
- [] No es demasiado grande _(una red social completa)_ ni demasiado pequeño _(una calculadora)_.
- [X] El sistema **maneja datos personales**: Sí / No. Si es Sí, aplica la Ley 1581 de 2012 en el numeral 10 de la Nota 1.

---

## Ejemplo diligenciado

Referencia de nivel de detalle esperado. **No se puede usar este dominio.**

- **Dominio:** control de turnos en una barbería de barrio con tres sillas.
- **Problema:** los turnos se anotan en un cuaderno; los clientes llegan sin saber la espera y se van, y el dueño no sabe cuánto factura cada barbero al mes.
- **Hoy:** cuaderno físico y llamadas telefónicas.
- **Usuarios:** cliente _(reserva y consulta su turno)_, barbero _(ve su agenda del día)_, administrador _(cierra caja y ve el reporte mensual)_. Acceso real: el tío de un integrante es dueño del local.
- **Sí hace:** reservar turno, ver agenda del día por barbero, cerrar caja con reporte de ingresos.
- **No hace:** pagos en línea, domicilios, inventario de productos.

---

## Flujo del Proyecto

```bash
UI → Controlador → ServicioIA «interfaz» → AdaptadorProveedor → API del modelo → AdaptadorSimulado → respuesta fija (pruebas)
```