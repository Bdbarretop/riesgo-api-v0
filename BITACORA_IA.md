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
| 3 | A/B (H4) | Brayan | Ampliar `.gitignore` a las entradas estándar de un proyecto Python + FastAPI |
| 4 | A/B (H5) | Brayan | Preservar la identidad de la función envuelta en `con_registro` |
| 5 | A/B (H6) | Brayan | Que `con_registro` deje propagar las excepciones en vez de tragárselas |
| 6 | A/B (H7) | Brayan | Sacar `historial` del atributo de clase para que dos instancias no lo compartan |

## Aceptado

| # | Qué propuso la IA | Por qué lo aceptamos | Qué cambiamos antes de usarlo |
|---|-------------------|----------------------|-------------------------------|
| 1 | Correr `pip install` de las 7 dependencias sin versión y capturar con `pip freeze` las versiones exactas para pinnearlas con `==` | Es exactamente lo que exige la restricción B1: reproducibilidad. Sin `==`, el calificador puede instalar versiones distintas y el entorno no se reproduce | Nada — se aceptó tal cual |
| 2 | Eliminar las constantes `API_KEY` y `CLAVE_FIRMA` de `config.py` porque un `grep` demostró que no se usan en ningún módulo del proyecto | Es el arreglo mínimo suficiente para B1 y se justifica con evidencia (grep). Reemplazarlas por lectura de `os.environ` sin código que las consuma habría añadido complejidad no pedida | Nada |
| 3 | Ampliar `.gitignore` con secciones para Python (`__pycache__/`, `*.pyo`, `*.egg-info/`, `.pytest_cache/`), entornos virtuales (`.venv/`, `venv/`, `env/`), variables de entorno (`.env`, `.env.*` con excepción para `.env.example`) e IDE (`.vscode/`, `.idea/`) | Son las entradas estándar de un proyecto Python; sin ellas cualquier `pip install` en el directorio del proyecto contamina el diff y un `.env` local se puede commitear por error | Nada — se aceptó tal cual |
| 4 | Añadir `import functools` y decorar la envoltura interna con `@functools.wraps(func)` | Es el patrón estándar de la stdlib para preservar `__name__`, `__doc__` y `__wrapped__`. El test `test_el_decorador_conserva_la_identidad_de_la_funcion` lo verifica explícitamente | Nada |
| 5 | Reemplazar `return None` del `except` por `raise` después de imprimir el log, manteniendo el `print` original | Cumple B9 sin cambiar el propósito del decorador (auditar llamadas). Dejar que la excepción propague permite que capas superiores respondan con el código HTTP correcto | Nada |
| 6 | Mover `historial = []` de nivel de clase a `self.historial = []` dentro de `__init__`, y crear una clase `RepositorioEvaluaciones` como colaborador opcional para conservar el historial entre peticiones | Cumple el test de aislamiento entre instancias, la restricción B4 (dominio en clases sin estado global), el contrato del constructor (póliza única + colaboradores opcionales) y suma en C5 (POO con responsabilidad clara) | Nada — se aceptó tal cual |

## Rechazado

| # | Qué propuso la IA | Por qué lo rechazamos | Qué hicimos en su lugar |
|---|-------------------|-----------------------|-------------------------|
| 1 | Añadir `aiofiles` y `python-dotenv` al `requirements.txt` mientras se fijaban las versiones (útiles para arreglar `/consulta-archivo` en Parte C y para sacar secretos de `config.py` en H1) | El enunciado dice explícitamente que "cualquier cosa que añadan más allá de lo pedido no suma puntos y sí ocupa el tiempo de la defensa". Cada dependencia nueva se debe defender en la sustentación, así que solo se añaden cuando sean estrictamente necesarias | Se pinneó **solo** las 7 dependencias que ya venían en el archivo original |
| 2 | Reescribir la historia de git con `git filter-repo` para borrar los secretos del commit `v0-semilla` y forzar push | El comando de evidencia declarado en HALLAZGOS.md apunta a `v0-semilla`; el calificador hace `checkout` de ese commit para reproducir el defecto. Si borramos los secretos del historial, la fila queda sin evidencia y no cuenta. La corrección vive en HEAD, no en la historia | Se dejaron los secretos en `v0-semilla` (donde el calificador los verifica) y se eliminaron solo en HEAD |
| 3 | Añadir `modelo.pkl` y `datos/siniestros.csv` al `.gitignore` como "buenas prácticas para no versionar binarios ni datasets" | El README del propio semilla dice que `modelo.pkl` viene con el repositorio y el servicio lo carga al arrancar. Ignorarlo lo sacaría del repo y rompería `/score`. El CSV es dataset sintético del artefacto, no datos sensibles | Se dejaron ambos archivos versionados |
| 4 | Eliminar el decorador `con_registro` de `puntuar` completamente ("si ya no traga excepciones, ¿para qué el decorador?") | El decorador sigue teniendo sentido como punto de auditoría: deja rastro de qué falló. Eliminarlo cambiaría el modelado del dominio (que sí se califica en C5) sin ganar nada. B9 exige que el decorador cumpla ciertas reglas, no que se elimine | Se mantuvo el decorador aplicado a `puntuar`, corregido |
| 5 | Reemplazar el `print` por `logging.error(...)` con un logger configurado a nivel del módulo | Añadir el módulo `logging` implica configurar handlers, niveles y formato — es superficie de código y complejidad no pedida. El enunciado dice "hacer lo pedido y saber por qué" | Se mantuvo el `print` original, único cambio: `raise` después |
| 6 | Usar una lista de módulo `_HISTORIAL_GLOBAL = []` en `dominio.py` como almacén compartido, sin envolverla en una clase | B4 prohíbe explícitamente "funciones sueltas con estado global"; una lista de módulo es exactamente eso. Además pierde la responsabilidad clara que una clase Repositorio expone (`registrar`, `listar`) | Se creó `RepositorioEvaluaciones` como clase con responsabilidad de almacenamiento |
