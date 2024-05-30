#include <Python.h>
#include <string.h>

static int has_unique_chars(const char *s) {
    int len = strlen(s);
    int char_set[256] = {0};

    for (int i = 0; i < len; i++) {
        if (char_set[(unsigned char)s[i]]) {
            return 0;
        }
        char_set[(unsigned char)s[i]] = 1;
    }
    return 1;
}

static PyObject* py_has_unique_chars(PyObject* self, PyObject* args) {
    const char* s;
    if (!PyArg_ParseTuple(args, "s", &s)) {
        return NULL;
    }
    int result = has_unique_chars(s);
    return Py_BuildValue("i", result);
}

static PyMethodDef UniqueCharsMethods[] = {
    {"has_unique_chars", py_has_unique_chars, METH_VARARGS, "Check if a string is composed of non-repeating characters"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef uniquecharsmodule = {
    PyModuleDef_HEAD_INIT,
    "unique_chars",
    "Unique Characters Module",
    -1,
    UniqueCharsMethods
};

PyMODINIT_FUNC PyInit_unique_chars(void) {
    return PyModule_Create(&uniquecharsmodule);
}