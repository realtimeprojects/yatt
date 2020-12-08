from uuid import uuid4

from .logf import logf
from . import registry


class Suite:
    @staticmethod
    def run():
        trid = str(uuid4())
        logf.info("---- preparing testrun {}", trid)
        registry.walk('prepare', trid)

        def run_it(testcase):
            logf.info("---- testcase START: {}", testcase)
            testcase()
            logf.info("---- testcase PASS: {}", testcase)

        registry.foreach('testcase', run_it)
