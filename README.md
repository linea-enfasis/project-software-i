# Ficha de equipo y dominio — Sesión 1

Plantilla de la **actividad de cierre de la Clase 1**. Se diligencia en clase, en equipo, y se entrega al final de la sesión.

- **Equipos:** de 2 a 3 integrantes, fijos durante todo el curso.
- **Entrega:** una ficha por equipo.
- **Cada equipo elige un dominio distinto.**

---

## 1. Identificación del equipo

| Campo | Respuesta |
|---|---|
| Nombre del equipo | _(completar)_ |
| Fecha | _(completar)_ |

| # | Integrante | Correo | Rol / responsabilidad |
| --- | --- | --- | --- |
| 1 | _(completar)_ | _(completar)_ | Coordinación _(obligatorio)_ |
| 2 | _(completar)_ | _(completar)_ | _(completar)_ |
| 3 | _(completar)_ | _(completar)_ | _(completar)_ |

> El rol no es definitivo: se ajusta en la bitácora de gestión. Lo que sí queda fijo hoy es **quién coordina**.

---

## 2. Dominio propuesto

**Dominio:** _(una línea — el sector o la actividad; e.g. "gestión de inventario para una tienda de barrio")_

**Problema que se quiere resolver** _(máximo tres líneas: qué pasa hoy, a quién le duele y por qué el proceso actual no alcanza)_:

_(completar)_

**Cómo se hace hoy sin software** _(o con qué herramienta improvisada: papel, WhatsApp, un Excel)_:

_(completar)_

---

## 3. Usuarios del sistema

| Tipo de usuario | Qué necesita hacer en el sistema | ¿Tenemos acceso para entrevistarlo? |
| --- | --- | --- |
| _(completar)_ | _(completar)_ | Sí / No — _(quién es)_ |
| _(completar)_ | _(completar)_ | Sí / No — _(quién es)_ |

> Al menos **un usuario real y accesible** es obligatorio: en la Clase 3 hay que hacerle una sesión de elicitación de verdad.

---

## 4. Capacidad del equipo

**¿Por qué este equipo puede levantar requisitos de este dominio?** _(acceso a usuarios reales, alguien trabaja o trabajó ahí, experiencia previa con el proceso, etc.)_

_(completar)_

---

## 5. Alcance tentativo

**Tres cosas que el sistema sí debe hacer**:

1. _(completar)_
2. _(completar)_
3. _(completar)_

**Tres cosas que el sistema no va a hacer**:

1. _(completar)_
2. _(completar)_
3. _(completar)_

---

## 6. Autoverificación

- [ ] Hay **usuarios reales accesibles** para entrevistar en la Clase 3.
- [ ] El dominio da para **10 requisitos funcionales y 5 no funcionales** sin inventarlos.
- [ ] Los **tres casos críticos** se ven implementables end-to-end en seis semanas.
- [ ] El proyecto **no fue desarrollado** en otra asignatura ni se está reciclando.
- [ ] No es demasiado grande _(una red social completa)_ ni demasiado pequeño _(una calculadora)_.
- [ ] El sistema **maneja datos personales**: Sí / No. Si es Sí, aplica la Ley 1581 de 2012 en el numeral 10 de la Nota 1.

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