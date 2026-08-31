# Bitácora de uso de IA

**Grupo:** <número> · **Integrantes:** Brayan Barreto, Edwing Navarrete
**Herramientas usadas:** Claude (Sonnet 4.6)

> Las tres secciones son obligatorias. **`## Rechazado` es la que se califica.**
> Una bitácora que solo lista prompts aceptados vale la mitad.

## Prompts

| # | Parte | Quién | Prompt (resumido si es largo) |
|---|-------|-------|-------------------------------|
| 1 | A/B (H2) | Brayan | Fijar versiones en `requirements.txt` con `pip freeze` en venv limpio |
| 2 | A/B (H3) | Brayan | Sacar los secretos hardcodeados de `config.py` cumpliendo B1 |

## Aceptado

| # | Qué propuso la IA | Por qué lo aceptamos | Qué cambiamos antes de usarlo |
|---|-------------------|----------------------|-------------------------------|
| 1 | Correr `pip install` de las 7 dependencias sin versión y capturar con `pip freeze` las versiones exactas para pinnearlas con `==` | Es exactamente lo que exige la restricción B1: reproducibilidad. Sin `==`, el calificador puede instalar versiones distintas y el entorno no se reproduce | Nada — se aceptó tal cual |
| 2 | Eliminar las constantes `API_KEY` y `CLAVE_FIRMA` de `config.py` porque un `grep` demostró que no se usan en ningún módulo del proyecto | Es el arreglo mínimo suficiente para B1 y se justifica con evidencia (grep). Reemplazarlas por lectura de `os.environ` sin código que las consuma habría añadido complejidad no pedida | Nada |

## Rechazado

| # | Qué propuso la IA | Por qué lo rechazamos | Qué hicimos en su lugar |
|---|-------------------|-----------------------|-------------------------|
| 1 | Añadir `aiofiles` y `python-dotenv` al `requirements.txt` mientras se fijaban las versiones (útiles para arreglar `/consulta-archivo` en Parte C y para sacar secretos de `config.py` en H1) | El enunciado dice explícitamente que "cualquier cosa que añadan más allá de lo pedido no suma puntos y sí ocupa el tiempo de la defensa". Cada dependencia nueva se debe defender en la sustentación, así que solo se añaden cuando sean estrictamente necesarias | Se pinneó **solo** las 7 dependencias que ya venían en el archivo original |
| 2 | Reescribir la historia de git con `git filter-repo` para borrar los secretos del commit `v0-semilla` y forzar push | El comando de evidencia declarado en HALLAZGOS.md apunta a `v0-semilla`; el calificador hace `checkout` de ese commit para reproducir el defecto. Si borramos los secretos del historial, la fila queda sin evidencia y no cuenta. La corrección vive en HEAD, no en la historia | Se dejaron los secretos en `v0-semilla` (donde el calificador los verifica) y se eliminaron solo en HEAD |
