from .logf import logf

_registry = {'testcase': {}, 'prepare': {}}


def register(folder, fn):
    logf.debug("adding {} {}: {}", folder, fn.__name__, fn.__doc__)
    _registry[folder][fn.__name__] = fn


def foreach(folder, do):
    for fn in _registry[folder].keys():
        do(_registry[folder][fn])


def walk(folder, *arg, **kwarg):
    for fn in _registry[folder].keys():
        _registry[folder][fn](*arg, **kwarg)
