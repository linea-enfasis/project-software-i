# Taller 3 · Elicitación cruzada de requerimientos

Enunciado del **Taller 3**. Se trabaja en clase, por parejas de equipos, y se entrega al final de la sesión.

- **Dinámica:** cada equipo entrevista a otro, que hace de **cliente** de su dominio, y luego se invierten los papeles.
- **Entrega:** en el **repositorio del equipo en GitHub**, diligenciando el enunciado con los puntos 1, 4, 5 y 6; las notas de la entrevista del punto 2 o 3 van como anexo en el mismo archivo.

---

## 1. Preparación

**Emparejamiento:** formar parejas de equipos con dominios distintos.

**Cómo funciona:** cada equipo pregunta **sobre su propio proyecto**. El otro equipo no responde sobre el suyo: se pone en el lugar del usuario del proyecto de quien pregunta. Si A hace inventario de materiales para técnicos, en la Ronda 1 B hace de almacenista de esa empresa y responde a las preguntas de A; en la Ronda 2, A hace de usuario del dominio de B.

- Que el cliente no conozca el dominio **es parte del ejercicio**: obliga a preguntar sin dar por sentado nada, y lo que el cliente improvisa se valida después con el cliente del proyecto.
- Lo que se evalúa hoy es la **técnica**: el guion, el sondeo, las notas y la conversión en requisitos con fuente. La verdad del dominio sale de la entrevista con el cliente del proyecto.
- **Este emparejamiento queda fijo:** el equipo que hace de cliente hoy es el **equipo cliente** para los proyectos que no tienen usuario real ni sustituto.

**Tarjeta de personaje:** el equipo entrevistador se la entrega al cliente al inicio, para que pueda responder con verosimilitud. Da el contexto, **no las respuestas**.

| Campo | Ejemplo *(barbería)* |
| --- | --- |
| Quién es | Dueño de la barbería, 15 años con el local |
| Qué hace en el día a día | Atiende una silla, contesta el teléfono y cierra caja |
| Cómo se hace hoy | Cuaderno de turnos y llamadas |
| Relación con la tecnología | Usa WhatsApp; nunca ha usado un computador para el negocio |

**Como cliente** *(del dominio del otro equipo)*:

- Leer la ficha de dominio y la tarjeta de personaje del equipo que va a entrevistar.
- Sostener el personaje toda la ronda *(e.g. "soy la dueña de la papelería, 12 años con el negocio, no uso computador")*.
- Responder con **problemas y situaciones del día a día**, no con soluciones técnicas. Si no sabe algo, puede inventarlo, siempre que sea verosímil con la tarjeta.

**Como entrevistador** *(del dominio propio)*:

- Ordenar las 10 preguntas. El banco de abajo sirve para completar tipos que falten.
- Asignar los roles de la entrevista.

**Banco de preguntas por tipo:** plantillas que sirven para cualquier dominio. Se reemplaza lo que va entre guillemets *(«proceso», «elemento»)* por el vocabulario del proyecto propio. **Copiarlas sin adaptar no cuenta**: una pregunta que podría hacerse en cualquier proyecto no saca requisitos de este.

| Tipo | Para qué | Plantillas |
| --- | --- | --- |
| **Contexto** | Entender el rol y el proceso completo | ¿Cuál es su papel en «el negocio / el área»? · ¿Cómo se hace hoy «el proceso», desde que empieza hasta que termina? · ¿Quién más participa? |
| **Abierta** | Encontrar el dolor | ¿Qué es lo que más le complica de «el proceso»? · ¿Qué le quita más tiempo en la semana? · Si pudiera cambiar una sola cosa, ¿cuál sería? |
| **Sondeo** | Profundizar en una respuesta | ¿Por qué? · ¿Me cuenta la última vez que pasó? · ¿Qué hizo en ese momento? · ¿Qué quiere decir con «término que usó el cliente»? |
| **Excepción** | Sacar flujos alternos | ¿Qué pasa cuando «el elemento» falta, llega tarde o viene mal? · ¿Y si la persona responsable no está? · ¿Qué hace cuando se equivoca al registrar algo? |
| **Cuantitativa** | Sacar RNF medibles | ¿Cuántos «registros» maneja al día o al mes? · ¿Cuántas personas lo hacen al mismo tiempo? · ¿Cuánto tiempo toma hoy? · ¿Cuánto es aceptable esperar? |
| **Datos y control** | Sacar permisos, auditoría y datos personales | ¿Quién puede ver o cambiar «la información»? · ¿Necesita saber quién hizo cada cambio y cuándo? · ¿Qué datos de personas se guardan? |
| **Cierre** | No dejar nada por fuera | ¿Hay algo que no le pregunté y debería saber? · ¿Con quién más debería hablar? · ¿Qué documentos o formatos usa hoy y me los puede mostrar? |

- **Evitar:** preguntas sobre la solución *("¿quiere una app móvil?")*, inductoras *("¿no le parece que sería mejor…?")* y las que se responden con sí o no sin dar información.

**Guion de entrevista**

| # | Pregunta | Tipo |
| --- | --- | --- |
| P1 | ¿Por qué cree que se debe automatizar el proceso actual? | Abierta |
| P2 | ¿Qué funciones considera indispensables en el sistema? | Abierta |
| P3 | ¿Qué información o datos necesita gestionar su sistema? | Contexto |
| P4 | ¿Cuántos usuarios van a usar el sistema? | Contexto |
| P5 | ¿Qué nivel de seguridad quiere que cuente su sistema?| Datos y Control |
| P6 | ¿que otra herramienta cree que debe tener el software? | Cierre |


- **Mínimo:** dos preguntas de **excepción** y dos **cuantitativas**. De ellas salen los flujos alternos y los RNF.

**Roles**

| Rol | Integrante |
| --- | --- |
| Entrevistador | *(Johan Stiven Henao Muñoz)* |
| Anotador | *(Cristian Cristian Camilo Castaño)* |
| Observador | *(Jose Fernando Sanchez)* |

> **Equipo de 2:** el anotador asume también la observación. **Equipo de 4:** el cuarto integrante lleva el tiempo y anota las preguntas de sondeo que surjan.

---

## 2. Ronda 1

El **equipo A** entrevista al **equipo B**, que hace de cliente del dominio de A.

- 12 minutos exactos: el docente marca el tiempo.
- El anotador registra las respuestas **textuales**, numeradas con la pregunta que las originó *(P1, P2…)*. Si una respuesta abre un tema nuevo, la pregunta de sondeo se anota como *P4a, P4b*.
- El observador anota contradicciones, jerga del dominio y lo que el cliente evita responder.

---

## 3. Ronda 2

Se invierten los papeles: el **equipo B** entrevista al **equipo A**. Mismas reglas.

---

## 4. Análisis

Convertir las notas propias en requisitos candidatos. Todavía no es el catálogo final: es lo que se va a confirmar con el cliente del proyecto.

**Requisitos funcionales candidatos** *(mínimo 8)*:
**Requisitos no funcionales candidatos** *(mínimo 3, con métrica)*:

| ID | Descripción | Prioridad | Fuente |
| --- | --- | --- | --- |
| RF-01 | El sistema debe permitir el ingreso del administrador y el tecnico  |  Must | P1, P3 |
| RF-02 | El sistema debe permitir el ingreso de material al administrador | Must | P6 |
| RF-03 | El sistema debe permitir la asignacion del material a los tecnicos por parte del administrador | Must | P7 |
| RF-04 | El sistema debe permitir la visualizacion del material gastado por parte de los tecnicos | Must | P7 |
| RF-05 | El sistema debe permitir la devolucion de los materiales por parte de los tecnicos | Must | P7 |
| RF-06 | El sistema debe permitir la visualizacion del material a nivel general al administrador | Must | P7 |
| RF-07 | El sistema debe permitir que el tecnico visualice su material gastado en el momento | Must | P7 |
|RF-08  | El sistema debe permitir que el técnico ingrese en el sistema elementos entregados defectuosos	|Should	|P7|
|RF-09  | El sistema debe permitir al administrador visualizar el historial de movimientos de material	|Should|P7|
|RF-10  | El sistema debe permitir al administrador registrar, editar y desactivar cuentas de técnicos	|Should	|P1|
|RF-11  | El sistema debe notificar al administrador cuando un material esté defectuoso según el estado del material	|Should| P7|
|RF-12  | El sistema debe enviar una notificación al momento de presentarse una falla	|should	|P7|
|RF-13  | El sistema debe permitir al administrador revisar y aprobar o rechazar los elementos defectuosos reportados por los técnicos	|Should|P7|
|RF-14  | El sistema debe permitir al técnico consultar el material que tiene asignado actualmente	|Should	|P7|
|RF-15  | El sistema debe permitir al administrador confirmar la recepción de los materiales devueltos por los técnicos	|Should|P7|
|RF-16  | El sistema debe registrar la fecha, hora y usuario responsable de cada movimiento de material |Should|P7|
| RNF-01 | *(Eficiencia de desempeño)* El sistema soporta ingreso simultaneo de cualquier cantidad de usuarios, respondiendo en menos de 10 s | Should | P9 |
| RNF-02 | *(Usabilidad)* El sistema esta activo 24/7 | Must | P3, P10 |
| RNF-03 | *(Usabilidad)* El sistema al momento de cargar los datos se demora 15s | Should | P3, P10 |
| RNF-04 | *(Seguridad)* El sistema debe restringir el acceso por roles: el técnico solo puede ver su material asignado y el administrador tiene acceso a la gestión completa | Must | P1, P7 |
| RNF-05 | *(Fiabilidad)* El sistema debe garantizar la integridad del inventario: ningún movimiento de material debe dejar el stock en valores negativos | Should | P3, P10 |
| RNF-06 | *(Fiabilidad)* El sistema debe recuperarse de una falla en un máximo de 1 hora | Should | P3, P10 |
| RNF-07 | *(Usabilidad)* El sistema debe mostrar mensajes de error claros| Should | P3 |
| RNF-08 | *(Eficiencia de desempeño)* El sistema debe soportar al menos 50 usuarios concurrentes sin degradar el tiempo de respuesta|Should | P9 |
| RNF-09 | *(Eficiencia de desempeño)* El historial de movimientos debe cargar en menos de 5 s con hasta 10.000 registros | Should | P7, P9 |



**Ambigüedades y conflictos detectados** *(lo que hay que aclarar con el cliente del proyecto)*:

- *(Se necesita registrar nuevos usurios o modificar los ya exixtentes?)* Se le pregunta al dueño directo

- *(Se pueden sacar los historicos o historial de las modificaciones del inventario?)* Se le pregunta al dueño y coordinador 

- *(Los usuarios deben ser unicos, tener un diferenciador?)* Se le pregunta al dueño y coordinador 

> Todo requisito lleva **fuente**. Un requisito sin pregunta que lo respalde es un requisito inventado por el equipo.

---

## 5. Validación cruzada

El equipo cliente lee la lista del punto 4 y marca cada requisito:

| Marca | Significado |
| --- | --- |
| ✅ | Lo dije y está bien entendido |
| ✏️ | Lo dije, pero no así *(se anota la corrección)* |
| ❌ | No lo dije: el equipo lo supuso |

**Resultado de la validación:**

| Requisito | Marca | Corrección del cliente |
|---|---|---|
| *(RF 1)* | *(✏️)* | *(Cliente propone que se ingrese con un usuario y contraseña)* |
| *(RF 2)* | *(✅ )* | *(Aprobado)* |
| *(RF 3)* | *(✅)* | *(Aprobado)* |
| *(RF 4)* | *(✅)* | *(Aprobado)* |
| *(RF 5)* | *(✏️)* | *(Cliente solicita subir el estado del material (defectuoso,bueno,malo))* |
| *(RF 6)* | *(✅)* | *(Aprobado)* |
| *(RF 7)* | *(✅)* | *(Aprobado)* |
| *(RF 8)* | *(✅)* | *(Aprobado)* |
| *(RNF 1)* | *(✅)* | *(Aprobado)* |
| *(RNF 2)* |*(✅)* | *(Aprobado)* |
| *(RNF 3)* | *(❌)* | *(El equipo supuso el tiempo de gestion)* |


- Los ❌ no se borran: pasan a **preguntas para el cliente del proyecto**. Pueden ser requisitos válidos que el cliente no mencionó, o suposiciones del equipo.

---

## 6. Plan con el cliente del proyecto

La entrevista de hoy es un ensayo. La elicitación que cuenta para la Nota 1 es con el **cliente del proyecto**, siempre **externo al equipo**. Se usa el primer nivel posible:

1. **Usuario real** del dominio. Si un integrante trabaja en el lugar, su papel es conseguir la cita con quien vive el proceso *(jefe, almacenista, cliente)*, no ser el entrevistado.
2. **Usuario sustituto**: alguien que hace esa actividad en otro lugar, aunque no vaya a usar el sistema.
3. **Equipo cliente**: el equipo que hizo de cliente hoy. En este caso la técnica complementaria es obligatoria: **análisis de documentos o de sistemas similares** *(formatos, planillas, aplicaciones parecidas)*, para que los requisitos no dependan solo de lo que el otro equipo imagine.

| Campo | Respuesta |
| --- | --- |
| Cliente del proyecto  | *(nivel 3, equipo cliente)* |
| Técnica principal y técnica complementaria | *( entrevista + análisis de documentos)* |
| Fecha y lugar | *(21/09/2026)* |*(Universidad Uniremintong)* | *(desde las 8:00 pm a 9:00 pm)* | 
| Responsables | *(Johan, Entrevistador)* |  *(Cristian, Anotador)* | *(José, Observador)* |
| Evidencia que se va a recoger | *( notas y grabación con consentimiento)* |
| Preguntas que se añaden al guion tras el taller | *(¿actualmente usa algún método o herramientas para esta tarea?)* | *(¿Qué nivel de experiencia técnica tienen los usuarios en las nuevas tecnologías?)* | *(¿con que presupuesto cuentan y cuanto tiempo están dispuestos a esperar?)* | *(¿Este sistema lo usa solamente el personal de la empresa  o también sus clientes?)* |

- Añadir la tarjeta de la entrevista real al tablero, dentro del **Sprint 1**, con responsable y fecha.

---

## Ejemplo diligenciado

Referencia de nivel de detalle. Mismo dominio de los Talleres 1 y 2: **no se puede usar.**

**1. Guion** *(barbería de barrio; extracto)*

| # | Pregunta | Tipo |
| --- | --- | --- |
| P1 | ¿Cómo se agenda hoy un turno, desde que el cliente llama hasta que se sienta en la silla? | Contexto |
| P3 | ¿Qué es lo que más le complica del día a día con los turnos? | Abierta |
| P4 | ¿Por qué? ¿Me cuenta la última vez que pasó? | Sondeo |
| P6 | ¿Qué pasa cuando un cliente no llega? | Excepción |
| P7 | ¿Y cuando un barbero falta sin avisar? | Excepción |
| P9 | ¿Cuántos turnos atienden en un sábado? ¿Cuántos clientes llaman al tiempo? | Cuantitativa |
| P10 | ¿Cuánto tiempo está dispuesto a dedicarle al sistema al día? | Cuantitativa |
| P12 | ¿Hay algo que no le pregunté y debería saber? | Cierre |

**2. Notas** *(extracto)*

- **P3:** "Los sábados el teléfono no para y mientras contesto no corto."
- **P6:** "Unos dos o tres por semana no llegan y ese turno se pierde."
- **P9:** "Unos 40 turnos el sábado, entre los tres."
- **Observador:** el "cliente" dice *"agenda"* para el cuaderno y *"turno"* para cada cita; usar esos términos en el catálogo.

**4. Requisitos candidatos** *(extracto)*

| ID | Descripción | Prioridad | Fuente |
| --- | --- | --- | --- |
| RF-01 | El sistema debe permitir al cliente reservar un turno eligiendo barbero, fecha y franja libre | Must | P1, P3 |
| RF-02 | El sistema debe permitir al barbero marcar un turno como no asistido | Should | P6 |
| RF-03 | El sistema debe reasignar los turnos de un barbero ausente o notificar a sus clientes | Should | P7 |
| RNF-01 | *(Eficiencia de desempeño)* El sistema soporta 40 reservas en un día y 10 consultas simultáneas, respondiendo en menos de 2 s | Must | P9 |
| RNF-02 | *(Usabilidad)* El dueño registra un turno telefónico en menos de 30 s | Should | P3, P10 |

**Ambigüedad:** ¿el cliente reserva con un barbero concreto o con el primero libre? Se pregunta al dueño real.

**5. Validación:** RF-01 ✅, RF-02 ✅, RF-03 ✏️ *("no reasigno, los llamo yo")* → pasa a "notificar a los clientes"; RNF-02 ❌ *("no dije tiempo")* → pregunta para el cliente del proyecto.

**6. Plan:** entrevista al dueño el lunes a las 8:00 en la barbería, antes de abrir, + fotos de dos páginas del cuaderno de turnos *(análisis de documentos)*. Responsables: entrevistador y anotador del taller. Tarjeta creada en el tablero.