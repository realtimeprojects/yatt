import logging


logging.basicConfig(level=logging.DEBUG)


class proxy:
    def __getattr__(self, name):
        def logit(msg, *arg, **kwarg):
            return getattr(logging, name)(msg.format(*arg, **kwarg))

        return logit


logf = proxy()
