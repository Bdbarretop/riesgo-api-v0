# Hallazgos — Parte A

**Grupo:** <número> · **Integrantes:** Brayan Barreto, Edwing Navarrete

> No borren la fila de ejemplo hasta haber comprobado que su tabla se parsea.
> El formato es rígido: siete columnas, en este orden. Una tabla torcida se
> rechaza indicando la línea, no se «entiende igual».
>
> **Tuberías dentro de una celda:** si su comando lleva `|` —y varios lo llevarán,
> por `grep`, `head` o `jq`— escríbanlo `\|`. Sin escapar, Markdown lo lee como
> separador de columna y su fila pasa a tener ocho.

| ID | Síntoma observable | Causa | Módulo · Sección | SHA donde se observa | Comando de evidencia | Salida obtenida | Corrección aplicada |
|----|--------------------|-------|------------------|----------------------|----------------------|-----------------|---------------------|
| H1 | *(ejemplo de FORMATO, no un defecto de este repositorio)* `GET /ping` responde sin cabecera `Cache-Control` | El handler no declara política de caché | M2 · 2. El protocolo HTTP y la autenticación | `v0-semilla` | `curl -sI localhost:8000/ping \| grep -ci cache-control` | `0` | Se añade la cabecera en la respuesta |
| H2 | `requirements.txt` no fija versiones de sus dependencias | Las 7 dependencias se declaran sin `==`, por lo que un `pip install` en máquina nueva puede traer versiones distintas y romper la reproducibilidad | M2 · 5. requirements.txt y la reproducibilidad | `v0-semilla` | `grep -c "==" requirements.txt` | `0` | Se fijan las 7 dependencias con `==` a las versiones instaladas en un venv limpio |
| H3 | `config.py` contiene credenciales en texto plano (`API_KEY` y `CLAVE_FIRMA`) versionadas en el repositorio | Los secretos se declararon como constantes hardcodeadas en un archivo que forma parte del historial de Git, expuestos a cualquiera con acceso al repo | M1 · 5. Git y GitHub para investigadores | `v0-semilla` | `grep -cE "^(API_KEY\|CLAVE_FIRMA) *=" config.py` | `2` | Se eliminan las dos constantes (nunca se usan en el código) |
| H4 | El `.gitignore` solo excluye `*.pyc` — no ignora `__pycache__/`, entornos virtuales (`.venv/`, `venv/`), archivos de entorno (`.env`) ni artefactos comunes de Python | El `.gitignore` es un stub mínimo que no protege el repositorio de commits accidentales de bytecode, dependencias locales o secretos en `.env` | M1 · 5. Git y GitHub para investigadores | `v0-semilla` | `cat .gitignore` | `*.pyc` | Se amplía `.gitignore` con las entradas estándar para un proyecto Python + FastAPI |
| H5 | El decorador `con_registro` reemplaza la identidad de la función envuelta: `EvaluadorRiesgo.puntuar.__name__` es `envoltura` en vez de `puntuar` | `utilidades.py` define `con_registro` sin `@functools.wraps(func)`, por lo que la envoltura no copia los metadatos (`__name__`, `__doc__`, `__wrapped__`) de la función original | M1 · 6. Decoradores como guardianes | `v0-semilla` | `python -c "from dominio import EvaluadorRiesgo; print(EvaluadorRiesgo.puntuar.__name__)"` | `envoltura` | Se añade `@functools.wraps(func)` a la envoltura interna del decorador |
| H6 | El decorador `con_registro` traga cualquier excepción y devuelve `None`: un fallo en `puntuar()` se convierte en un `puntaje: null` que el servicio responde con 200 en vez de propagar el error | El bloque `except Exception` de `con_registro` imprime un log y hace `return None`; la excepción nunca llega al handler ni se convierte en un código HTTP correcto | M1 · 6. Decoradores como guardianes | `v0-semilla` | `python -c "from utilidades import con_registro; print(con_registro(lambda: 1/0)() is None)"` | `True` | Se elimina el `return None` silencioso: el decorador registra la excepción y la re-lanza con `raise` |
| H7 | | | | | | | |


**Reglas que se verifican automáticamente:**

- `Módulo · Sección` debe citar una lección que exista en los módulos 1 a 5, con el
  título tal como aparece en el menú lateral del material.
- **`SHA donde se observa`** es el commit donde el defecto todavía está: normalmente
  `v0-semilla`, la etiqueta del repositorio tal como se lo entregamos. El calificador hace
  *checkout* de ese commit para reproducir la evidencia. Si lo dejan en el commit final —donde
  ya está corregido— el comando no reproducirá nada y la fila no cuenta.
- `Comando de evidencia` se ejecuta ahí. Escríbanlo contra `localhost:8000`; el calificador
  sustituye el puerto por el que use.
- `Salida obtenida` es literal, copiada de su terminal. **Se compara con lo que salga de
  verdad**, así que una salida inventada se detecta.
- Entre 6 y 12 hallazgos. Una fila que no corresponda a un defecto real resta la mitad de lo
  que suma una correcta: el máximo se alcanza con precisión, no con volumen.

---

# Parte C — Interpretación de las mediciones

> Un párrafo por endpoint. Expliquen **los tiempos que ustedes obtuvieron**, no la
> teoría general. Si un resultado los sorprendió, dígan­lo: eso se premia.

## `/ping`

## `/consulta-archivo`

## `/servicio-externo`

## `/calculo-pesado`
