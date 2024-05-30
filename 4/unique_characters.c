#include <Python.h>

// Function to check if a string has unique characters
static PyObject* has_unique_characters(PyObject* self, PyObject* args) {
    const char* input_str;
    if (!PyArg_ParseTuple(args, "s", &input_str)) {
        PyErr_SetString(PyExc_TypeError, "Parameter must be a string.");
        return NULL;
    }
    
    int char_set[256] = {0};
    for (int i = 0; input_str[i] != '\0'; ++i) {
        if (char_set[(unsigned char)input_str[i]]) {
            PyErr_SetString(PyExc_ValueError, "String contains duplicate characters.");
            return NULL;
        }
        char_set[(unsigned char)input_str[i]] = 1;
    }
    Py_RETURN_TRUE;
}

// Custom data type
typedef struct {
    PyObject_HEAD
    char* str;
    Py_ssize_t length;
} UniqueStringObject;

// Deallocate
static void UniqueString_dealloc(UniqueStringObject* self) {
    Py_XDECREF(self->str);
    Py_TYPE(self)->tp_free((PyObject*)self);
}

// New
static PyObject* UniqueString_new(PyTypeObject* type, PyObject* args, PyObject* kwds) {
    UniqueStringObject* self;
    self = (UniqueStringObject*)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->str = NULL;
        self->length = 0;
    }
    return (PyObject*)self;
}

// Init
static int UniqueString_init(UniqueStringObject* self, PyObject* args, PyObject* kwds) {
    const char* str = NULL;
    if (!PyArg_ParseTuple(args, "s", &str)) {
        return -1;
    }
    self->str = strdup(str);
    self->length = strlen(str);
    return 0;
}

// Length method
static PyObject* UniqueString_length(UniqueStringObject* self, PyObject* Py_UNUSED(ignored)) {
    return PyLong_FromSsize_t(self->length);
}

// Docstring
PyDoc_STRVAR(unique_string_doc, "UniqueString object with a string and length method.");

// Mapping
static PyMethodDef UniqueString_methods[] = {
    {"length", (PyCFunction)UniqueString_length, METH_NOARGS, "Return the length of the string"},
    {NULL}  // Sentinel
};

// Type definition
static PyTypeObject UniqueStringType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "unique.UniqueString",
    .tp_doc = unique_string_doc,
    .tp_basicsize = sizeof(UniqueStringObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = UniqueString_new,
    .tp_init = (initproc)UniqueString_init,
    .tp_dealloc = (destructor)UniqueString_dealloc,
    .tp_methods = UniqueString_methods,
};

// Module methods
static PyMethodDef UniqueMethods[] = {
    {"has_unique_characters", has_unique_characters, METH_VARARGS, "Check if a string has unique characters"},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef uniquemodule = {
    PyModuleDef_HEAD_INIT,
    "unique",
    "Module for checking unique characters in a string and custom UniqueString type.",
    -1,
    UniqueMethods
};

// Module initialization
PyMODINIT_FUNC PyInit_unique(void) {
    PyObject* m;
    if (PyType_Ready(&UniqueStringType) < 0)
        return NULL;

    m = PyModule_Create(&uniquemodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&UniqueStringType);
    if (PyModule_AddObject(m, "UniqueString", (PyObject*)&UniqueStringType) < 0) {
        Py_DECREF(&UniqueStringType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}