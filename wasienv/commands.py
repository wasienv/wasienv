from .tools import execute
from .wasiar import run as wasiar_run
from .wasicc import run as wasicc_run
from .wasiconfigure import run as wasiconfigure_run
from .wasienv import run as wasienv_run
from .wasild import run as wasild_run
from .wasimake import run as wasimake_run
from .wasinm import run as wasinm_run
from .wasiranlib import run as wasiranlib_run
from .wasirun import run as wasirun_run


def wasiar():
    return execute(wasiar_run)


def wasicc():
    return execute(wasicc_run)


def wasiconfigure():
    return execute(wasiconfigure_run)


def wasienv():
    return execute(wasienv_run)


def wasild():
    return execute(wasild_run)


def wasimake():
    return execute(wasimake_run)


def wasinm():
    return execute(wasinm_run)


def wasiranlib():
    return execute(wasiranlib_run)


def wasirun():
    return execute(wasirun)
