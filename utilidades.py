"""Utilidades transversales del servicio."""
import functools


def con_registro(func):
    """Registra el paso por la función. Si hay excepción, la deja propagar."""
    @functools.wraps(func)
    def envoltura(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            print(f"[registro] {func.__name__} falló: {exc}")
            raise
    return envoltura
