# Accesos Parking

Registro automático de **entradas y salidas del parking por matrícula**, a partir de las cámaras y
de **Frigate** (NVR con detección por IA).

## Qué hace

- **Registro de pasos.** Anota cada entrada y salida con la matrícula, la foto y la confianza de la
  lectura. Los pasos dudosos quedan para revisar.
- **Segunda lectura.** Si Frigate no lee la matrícula, la app la lee en el vídeo con su propio
  detector YOLOv9 y OCR (con licencia MIT).
- **Vehículos.** Lista de vehículos con su tipo (empleado, visita, proveedor…). Las puertas se pueden
  abrir solas para los tipos y el horario que elijas (iSmartGate / Gogogate2, Home Assistant,
  Tasmota o webhook).
- **Búsqueda rápida.** Escribe una matrícula arriba (atajo `/`) y ves al momento si está dentro,
  de quién es y sus últimos pasos.
- **Lista negra.** Matrículas a vigilar: salen en rojo en toda la app, avisan al entrar y la puerta
  nunca se abre sola para ellas.
- **Visitas.** Prerregistra a quien va a venir: al leer su matrícula ves quién es y a quién viene a
  ver, y no salta el aviso de matrícula desconocida.
- **Estadísticas.** Horas punta, ocupación por hora, tiempo de estancia, vehículos más frecuentes y
  calidad de la lectura de matrículas.
- **Pantalla de recepción.** Vista a pantalla completa para un monitor de recepción o garita, que se
  actualiza sola.
- **Avisos.** Por Microsoft Teams o webhook, e integración con Home Assistant.
- **Datos personales.** Se borran solos a los 30 días, como recomienda la AEPD.
- **Configuración desde la web.** Cámaras, NVR, puertas, usuarios, integraciones y una guía de
  instalación.
- **Tema claro u oscuro.** Sigue el del sistema o el que elijas en el menú de tu cuenta. Se usa
  también desde el móvil.

## Requisitos

- Hub365 2.2 o posterior, **en Linux con Docker**. La app es un contenedor y necesita unos 2 GB de RAM
  para la segunda lectura.
- Frigate 0.14 o posterior con la detección de matrículas (LPR) y su MQTT. El de Home Assistant sirve.
- Una licencia de Hub365 que incluya **Accesos Parking** (`app:accesos-parking`).

## Instalación desde Hub365

1. *Catálogo de apps* › **Accesos Parking** › **Instalar**.
   - Si Hub365 controla Docker, arranca él mismo el contenedor y lo publica en `/apps/accesos-parking/`.
   - Si no, copia el `compose` que te enseña, ponlo en marcha en tu servidor de Docker (en la misma
     red que Hub365) y Hub365 lo publica por su proxy.
2. Abre la app y sigue su **guía** (*Configuración › Guía*): Frigate, MQTT, cámaras y puertas.

Los datos (base de datos y fotos) van en el volumen `accesos-parking-data`. Se conservan al actualizar
y al desinstalar, salvo que elijas borrarlos.

## Novedades de la 1.2.0

- **Copias de seguridad**: copias manuales y automáticas (con o sin fotos, cifradas si quieres), descarga,
  restauración comprobada antes de aplicarse e importación/exportación de personas y vehículos (CSV) y de
  la configuración sin secretos.
- **Grabación extra para vehículos desconocidos**: si la matrícula no es de nadie, pide a Frigate unos
  segundos más de vídeo; se corta antes si al final resulta conocida.
- **Ajustes de grabación y detección de Frigate** desde la app (días que se guardan, segundos antes y
  después, umbrales), con copia previa y vuelta atrás si Frigate no los acepta.
- Mejor lectura: coches aparcados que ya no se confunden con el que pasa, menos llegadas partidas en dos y
  menos falsos «desconocidos».
- Menú lateral en acordeón: al abrir un grupo se cierran los demás.

## Novedades de la 1.1.0

- Interfaz nueva, igual que la de Hub365: menú lateral por grupos con tu cuenta dentro, tema claro u
  oscuro y mejor en el móvil.
- Búsqueda rápida, lista negra, visitas prerregistradas, estadísticas de ocupación y pantalla de
  recepción.
- Al actualizar desde la 1.0.0 se conservan todos los datos.
