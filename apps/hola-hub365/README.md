# Hola Hub365

App de ejemplo del catálogo de Hub365. Saluda al usuario que la abre y cuenta las visitas.

Sirve para comprobar que el catálogo funciona de punta a punta:

- **Identidad firmada.** La app sabe quién la abre gracias a las cabeceras `X-Hub365-*` firmadas por
  Hub365 (firma `v2`).
- **Licencia.** Comprueba que tu licencia de Hub365 incluye `app:hola-hub365`. Si no, muestra
  «Necesita licencia».
- **Datos.** El contador de visitas se guarda en la carpeta de datos de la app y se conserva al
  actualizarla o desinstalarla.

No necesita dependencias: solo el Python que ya trae Hub365.
