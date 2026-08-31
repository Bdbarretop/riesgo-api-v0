# Bitácora de uso de IA

**Grupo:** <número> · **Integrantes:** Brayan Barreto, Edwing Navarrete
**Herramientas usadas:** Claude (Sonnet 4.6)

> Las tres secciones son obligatorias. **`## Rechazado` es la que se califica.**
> Una bitácora que solo lista prompts aceptados vale la mitad.

## Prompts

| # | Parte | Quién | Prompt (resumido si es largo) |
|---|-------|-------|-------------------------------|
| 1 | A/B (H2) | Brayan | Fijar versiones en `requirements.txt` con `pip freeze` en venv limpio |

## Aceptado

| # | Qué propuso la IA | Por qué lo aceptamos | Qué cambiamos antes de usarlo |
|---|-------------------|----------------------|-------------------------------|
| 1 | Correr `pip install` de las 7 dependencias sin versión y capturar con `pip freeze` las versiones exactas para pinnearlas con `==` | Es exactamente lo que exige la restricción B1: reproducibilidad. Sin `==`, el calificador puede instalar versiones distintas y el entorno no se reproduce | Nada — se aceptó tal cual |

## Rechazado

| # | Qué propuso la IA | Por qué lo rechazamos | Qué hicimos en su lugar |
|---|-------------------|-----------------------|-------------------------|
| 1 | Añadir `aiofiles` y `python-dotenv` al `requirements.txt` mientras se fijaban las versiones (útiles para arreglar `/consulta-archivo` en Parte C y para sacar secretos de `config.py` en H1) | El enunciado dice explícitamente que "cualquier cosa que añadan más allá de lo pedido no suma puntos y sí ocupa el tiempo de la defensa". Cada dependencia nueva se debe defender en la sustentación, así que solo se añaden cuando sean estrictamente necesarias | Se pinneó **solo** las 7 dependencias que ya venían en el archivo original |
