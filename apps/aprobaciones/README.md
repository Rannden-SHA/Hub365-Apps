# Aprobaciones

Flujos de aprobación dentro de Hub365: **tipos de solicitud** con su formulario, **etapas** con quién aprueba y
en qué orden, **plazos** en horas laborables y un **justificante PDF** que se puede verificar.

## Qué hace

- **Tipos de solicitud.** Cada tipo tiene su formulario, su flujo, su numeración (por ejemplo `COMP-2026-0007`) y
  quién puede pedirlo. Los tipos tienen **versiones**: una solicitud sigue con la versión con la que se envió,
  aunque se publique otra.
- **Plantillas de serie.** Compra / pedido, nota de gastos, vacaciones y ausencias, viaje de trabajo, horas extra,
  contrato o documento, alta o acceso a sistemas, cambio de TI, préstamo de material y aprobación general. Se
  instalan y se cambian como cualquier otro tipo.
- **Formularios.** 25 tipos de campo: texto, números e importes, fechas y rangos, listas, personas,
  departamento, ficheros, tablas de líneas con totales y campos calculados. Un campo puede salir u obligarse
  solo si se cumple una condición.
- **Etapas y aprobadores.** Una persona, un grupo, el responsable del solicitante (o uno de más arriba, hasta 10
  niveles), el responsable del departamento, alguien elegido en el formulario o una **matriz de límites** (por
  importe, departamento…). Cada etapa puede pedir a todos, al primero, un **quórum** (con veto) o ir uno tras
  otro. Las etapas pueden ir en paralelo y saltarse si no se cumple su condición. Un **simulador** dice quién
  aprobaría y con qué plazos.
- **Decidir.** Aprobar, rechazar, devolver para cambios o respuestas propias del tipo. También reasignar, añadir
  un aprobador o **consultar** a alguien sin que vote. Una etapa puede exigir comentario o **firma** (escribir tu
  nombre). Se pueden aprobar varias a la vez.
- **Devolver y reenviar.** Al reenviar se guarda una revisión nueva con las diferencias campo a campo y una nota.
- **Plazos.** En horas laborables o naturales, con **calendarios** (horario por día y festivos). Recordatorios y,
  si sigue sin decidir pasadas las horas que elijas, escalado: avisar, reasignar, añadir a alguien o aprobar o
  rechazar sola. Las urgentes tienen la mitad de plazo.
- **Ausencias y delegaciones.** En *Mi ausencia* eliges un suplente y unas fechas: las tareas nuevas van al
  suplente o las ven los dos (vale la primera decisión).
- **Bandejas y búsqueda.** Pendientes de mí, mis solicitudes (con quién falta), donde participo, todas y
  borradores. Filtros guardados, búsqueda y atajos de teclado.
- **Confidenciales.** Los datos solo los ve quien participa; los administradores y los gestores del tipo ven
  solo la cabecera.
- **Línea de tiempo con cadena de huellas.** Cada paso queda anotado con su huella SHA-256, encadenada a la
  anterior. El **justificante PDF** lleva los datos, las decisiones, las firmas, los adjuntos con su huella y la
  cadena. En *Verificar justificante* compruebas con el número y la huella si coincide o si se ha alterado.
- **Avisos.** Campana de la app, correo con el botón «Revisar y decidir», resumen diario, **Microsoft Teams**
  (tarjeta en un canal, general o por tipo) y **webhooks** firmados con HMAC, con reintentos y registro.
- **Informes.** Volumen, tasa de aprobación, tiempo de ciclo (mediana y p90) por tipo, etapa y aprobador,
  cumplimiento de plazos, cuellos de botella, motivos de rechazo, carga e importes, en horas de reloj o
  laborables. Informes y bandejas se exportan a CSV y Excel.
- **API propia.** Tokens creados en *Ajustes › API* para crear y consultar solicitudes y decidir tareas desde
  otros programas. La petición pasa igualmente por Hub365: sin sesión de Hub365 solo llega si el portal público
  está activo y la app se puede ver sin iniciar sesión.
- **Auditoría, retención y copias.** Registro de cambios para los administradores, borrado de las solicitudes
  cerradas pasados los días que elijas en cada tipo y copias de seguridad.
- **Tema claro u oscuro**, en español o inglés, y adaptada al móvil, con el mismo aspecto que Hub365.

## Permisos

El rol de cada persona se elige en Hub365 › *Aplicaciones* › **Aprobaciones** › **Acceso** y se aplica al
momento:

| Hub365 | En Aprobaciones | Puede |
|---|---|---|
| Lector | **Usuario** | pedir los tipos que le dejen, decidir lo que le asignen, comentar, ver lo suyo y en lo que participa, su ausencia y sus avisos |
| Editor | **Gestor de procesos** | además, crear tipos y gestionar los suyos (formulario, flujo, versiones y sus solicitudes), grupos, calendarios e informes de sus tipos |
| Administrador | **Administrador** | todo: todas las solicitudes, personas y departamentos, delegaciones de otros, ajustes, Teams, API, webhooks, auditoría y copias |

Cada persona va por su cuenta de Hub365: no hay usuarios ni contraseñas aparte.

## Requisitos

- Hub365 **2.3** o posterior (Windows o Linux).
- **Docker** para el contenedor de la app.
- Una licencia de Hub365 que incluya **Aprobaciones** (`app:aprobaciones`).

**Con Hub365 2.4** la app usa la API de apps de Hub365. Pide tres permisos, que se conceden al instalar y se
pueden retirar en *Aplicaciones* › **Aprobaciones** › **Integración con Hub365**:

- **Directorio de personas** (`directory`): lee las personas y los departamentos de Hub365, con su cargo y su
  responsable, para elegir aprobadores que aún no han abierto la app.
- **Avisos en Hub365** (`notify`): avisa también en la campana de Hub365.
- **Correo** (`mail`): envía los correos con el SMTP de Hub365, solo a usuarios de Hub365.

**Con Hub365 2.3** (o sin esos permisos) la app funciona igual: conoce a las personas cuando entran por primera
vez y puedes importarlas desde un CSV (con cargo y responsable). Los correos salen por el SMTP propio de la app
(*Ajustes › Correo*) y los avisos se ven en la campana de la app.

## Instalación desde Hub365

1. *Catálogo de apps* › **Aprobaciones** › **Instalar**.
   - Si Hub365 controla Docker, arranca él mismo el contenedor y lo publica en `/apps/aprobaciones/`.
   - Si no, copia el `compose` que te enseña, ponlo en marcha en tu servidor de Docker (en la misma red que
     Hub365) y Hub365 lo publica por su proxy.
2. Abre la app desde el portal como administrador. Revisa el calendario y los ajustes, e instala los tipos que
   necesites desde *Plantillas*.

## Datos y copias de seguridad

La base de datos y los adjuntos van en el volumen de Docker `aprobaciones-data`. Se conservan al actualizar y
al desinstalar, salvo que elijas borrarlos. **Las copias de Hub365 no incluyen los volúmenes de Docker**:

- La app hace una copia cada noche dentro del propio volumen (carpeta `backups`, se guardan los días que
  elijas).
- En **Copias de seguridad** puedes descargar una copia completa (base de datos y ficheros) en ZIP.
- Para copiar el volumen entero desde el servidor:
  `docker run --rm -v hub365-aprobaciones_aprobaciones-data:/data -v "$PWD":/copia alpine tar czf /copia/aprobaciones.tgz -C /data .`

## Novedades de la 1.0.0

Primera versión.
