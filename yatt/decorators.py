from yatt import logf
from yatt.registry import register


def testcase(fn):
    logf.debug("adding testcase {}: {}".format(fn.__name__, fn.__doc__))
    register('testcase', fn)


def prepare(fn):
    logf.debug("adding prepare{}: {}".format(fn.__name__, fn.__doc__))
    register('prepare', fn)
