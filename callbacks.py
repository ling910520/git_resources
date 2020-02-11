class CallbackCallWrapper(object):
    def __init__(self, handler, name):
        self.name = name
        self.handler = handler
        print(self.handler)

    def __call__(self, *args, **kwargs):
        return self.handler._call(self.name, *args, **kwargs)  # noqa

class CallbackHandler(object):
    def __init__(self):
        self._callbacks = {}
        self.target = None
        self._object_intitialized = True

    def __setattr__(self, name, value):
        if '_object_intitialized' not in self.__dict__ or name in self.__dict__:
            print(f"{name} and {value}")
            return dict.__setattr__(self, name, value)
        else:
            if value is None:
                if name in self._callbacks:
                    del self._callbacks[name]
            else:
                self._callbacks[name] = value

    def __getattr__(self, name):
        return CallbackCallWrapper(self, name)
    def sample(self):
        return 1,2

_callbacks = CallbackHandler()
_callbacks
_callbacks.a=4
# for k in _callbacks.__dict__:
#     print(f"{k}")
class x(object):
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        print(dict.__setattr__(self, name, value))
        return dict.__setattr__(self, name, value)
    def sample(self):
        return 1,2
c = x()
c.a = 4
print(c.sample())

class basefunction(object):
    def __init__(self):
        self.target = self
    def print_member(self,*args,**kwargs):
        handler = getattr(self.target,"_on_print",None)
        if callable(handler):
            print("before call")
            return handler(*args,**kwargs)

class inheritedfunction(basefunction):
    def __init__(self):
        basefunction.__init__(self)
    def _on_print(self,*args,**kwargs):
        print('printed')
        return "from on printe"


a = inheritedfunction()
handler = a.print_member()

