# Documentación

Gestión documental de la empresa dentro de Hub365: **estanterías, libros, capítulos y páginas**, con un
editor completo y los **documentos** de cada tema (PDF, Word, Excel, imágenes…) en el mismo sitio.

## Qué hace

- **Estanterías y libros.** Ordena la documentación como en una biblioteca: estanterías con su portada y
  color, libros con capítulos y páginas, y páginas sueltas dentro de un libro. Todo se reordena arrastrando.
- **Editor completo.** Títulos, listas, listas de tareas, tablas, recuadros de aviso (información, éxito,
  cuidado y peligro), bloques de código con resaltado, desplegables, resaltado de texto, imágenes pegadas o arrastradas,
  PDF incrustados, tarjetas de fichero y enlaces entre páginas (escribe `[[`). Con atajos de teclado y su ayuda.
- **Documentos.** Cada página tiene sus **adjuntos** (subida múltiple arrastrando) y cada libro una pestaña
  **Documentos** con todos sus ficheros, filtro por tipo y vista previa de PDF, imágenes y texto.
- **Subir documentos.** Sube varios ficheros a la vez a un libro o capítulo y cada uno se convierte en una
  página: Word, Markdown, HTML y texto pasan a contenido editable; los PDF quedan incrustados y se pueden
  buscar por su texto; el resto queda como fichero descargable.
- **Revisiones.** Cada guardado es una revisión: compara dos versiones (palabras y código), vuelve a una
  anterior y ve quién cambió qué.
- **Borradores y edición a la vez.** El editor guarda un borrador solo mientras escribes y avisa si otra
  persona está editando la misma página. Si dos guardan a la vez, nadie pisa el trabajo de otro.
- **Plantillas.** Acta de reunión, procedimiento, política, guía paso a paso, informe, preguntas frecuentes,
  registro de decisiones, proyecto… y las tuyas propias, con variables como la fecha, el autor o el libro.
- **Importar y exportar.** Importa Markdown, HTML, texto, Word, PDF o un ZIP con un libro entero. Exporta
  páginas, capítulos y libros a HTML, Markdown, texto o ZIP, e imprímelos (o guárdalos como PDF) desde el
  navegador.
- **Búsqueda.** Busca en títulos, contenido, etiquetas y en el texto de los PDF y documentos de Word
  adjuntos, sin importar los acentos.
- **Favoritos, recientes y papelera.** Lo que borras va a la papelera y se puede recuperar; se vacía sola
  pasados los días que elijas.
- **Quién ve qué.** Cada libro puede verlo todo el mundo, solo ciertos **departamentos** de Hub365 (o los de
  su estantería) o solo los gestores.
- **Auditoría y copias.** Registro de cambios para los administradores, copia de seguridad descargable y
  copias automáticas cada noche.
- **Tema claro u oscuro**, en español o inglés, y adaptada al móvil, con el mismo aspecto que Hub365.

## Permisos

El rol de cada persona se elige en Hub365 › *Aplicaciones* › **Documentación** › **Acceso** y se aplica al
momento:

| Hub365 | En Documentación | Puede |
|---|---|---|
| Lector | **Consulta** | leer, descargar, exportar e imprimir lo que ve; favoritos |
| Editor | **Gestor** | además, crear y editar estanterías, libros y páginas, subir documentos, importar, plantillas y papelera |
| Administrador | **Administrador** | todo: ajustes, vaciar la papelera, auditoría, usuarios y copias de seguridad |

Cada persona va por su cuenta de Hub365: no hay usuarios ni contraseñas aparte.

## Requisitos

- Hub365 **2.3** o posterior (Windows o Linux).
- **Docker** para el contenedor de la app.
- Una licencia de Hub365 que incluya **Documentación** (`app:documentacion`).

## Instalación desde Hub365

1. *Catálogo de apps* › **Documentación** › **Instalar**.
   - Si Hub365 controla Docker, arranca él mismo el contenedor y lo publica en `/apps/documentacion/`.
   - Si no, copia el `compose` que te enseña, ponlo en marcha en tu servidor de Docker (en la misma red que
     Hub365) y Hub365 lo publica por su proxy.
2. Abre la app desde el portal. La primera vez está vacía: crea una estantería y un libro, o importa lo que
   ya tengas (*Importar*).

## Datos y copias de seguridad

La base de datos y los ficheros van en el volumen de Docker `documentacion-data`. Se conservan al actualizar
y al desinstalar, salvo que elijas borrarlos. **Las copias de Hub365 no incluyen los volúmenes de Docker**:

- La app hace una copia cada noche dentro del propio volumen (carpeta `backups`, se guardan los días que
  elijas en *Ajustes*).
- En *Ajustes* › **Copia de seguridad** puedes descargar una copia completa (base de datos y ficheros) en ZIP.
- Para copiar el volumen entero desde el servidor:
  `docker run --rm -v hub365-documentacion_documentacion-data:/data -v "$PWD":/copia alpine tar czf /copia/documentacion.tgz -C /data .`

## Novedades de la 1.0.0

Primera versión.
