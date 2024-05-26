import py_ds_trampoline

class AsyncIOBuilder:
    def load(self):
        trampoline = py_ds_trampoline.Trampoline("plugin1")
        return trampoline

aio=AsyncIOBuilder().load().do_something()

