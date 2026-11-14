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
- **Avisos.** Por Microsoft Teams o webhook, e integración con Home Assistant.
- **Datos personales.** Se borran solos a los 30 días, como recomienda la AEPD.
- **Configuración desde la web.** Cámaras, NVR, puertas, usuarios, integraciones y una guía de
  instalación.

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
