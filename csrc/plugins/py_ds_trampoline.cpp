#include <pybind11/pybind11.h>
#include "trampoline.h"

namespace py = pybind11;

PYBIND11_MODULE(py_ds_trampoline, m) {
    py::class_<Trampoline>(m, "Trampoline")
        .def(py::init<const std::string&>())
        .def("load_device", &Trampoline::load_device)
        .def("do_something", &Trampoline::do_something);
}
