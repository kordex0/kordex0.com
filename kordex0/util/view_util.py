from functools import wraps
from inspect import signature


def params(fn):
    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        fn_params = signature(fn).parameters
        # move positional args to key args
        for key, arg in zip(args, fn_params):
            kwargs[key] = arg
        for key in fn_params:
            if key in self.request.matchdict:
                kwargs[key] = self.request.matchdict[key]
            if key in self.request.params:
                kwargs[key] = self.request.params[key]
        return fn(self, **kwargs)
    return wrapper
