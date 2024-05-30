#include <Python.h>
#include <math.h>
#include "structmember.h"

typedef struct {
    PyObject_HEAD
    int x1;
    int y1;
    int x2;
    int y2;
} Line;

static void Line_dealloc(Line* self) {
    Py_TYPE(self)->tp_free((PyObject*)self);
}

static PyObject* Line_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    Line *self;

    self = (Line *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->x1 = 0;
        self->y1 = 0;
        self->x2 = 0;
        self->y2 = 0;
    }

    return (PyObject *)self;
}

static int Line_init(Line *self, PyObject *args, PyObject *kwds) {
    if (!PyArg_ParseTuple(args, "iiii", &self->x1, &self->y1, &self->x2, &self->y2)) {
        return -1;
    }
    return 0;
}

static PyMemberDef Line_members[] = {
    {"x1", T_INT, offsetof(Line, x1), 0, "x-coordinate of the first point"},
    {"y1", T_INT, offsetof(Line, y1), 0, "y-coordinate of the first point"},
    {"x2", T_INT, offsetof(Line, x2), 0, "x-coordinate of the second point"},
    {"y2", T_INT, offsetof(Line, y2), 0, "y-coordinate of the second point"},
    {NULL}
};

static PyObject* Line_length(Line* self) {
    double length = sqrt(pow(self->x2 - self->x1, 2) + pow(self->y2 - self->y1, 2));
    return Py_BuildValue("d", length);
}

static PyMethodDef Line_methods[] = {
    {"length", (PyCFunction)Line_length, METH_NOARGS, "Return the length of the line"},
    {NULL}
};

static PyObject* Line_str(Line* self) {
    return PyUnicode_FromFormat("Line((%i, %i), (%i, %i))", self->x1, self->y1, self->x2, self->y2);
}

static PyTypeObject line_LineType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    "line.Line",             /* tp_name */
    sizeof(Line),             /* tp_basicsize */
    0,                         /* tp_itemsize */
    (destructor)Line_dealloc, /* tp_dealloc */
    0,                         /* tp_print */
    0,                         /* tp_getattr */
    0,                         /* tp_setattr */
    0,                         /* tp_reserved */
    0,                         /* tp_repr */
    0,                         /* tp_as_number */
    0,                         /* tp_as_sequence */
    0,                         /* tp_as_mapping */
    0,                         /* tp_hash  */
    0,                         /* tp_call */
    (reprfunc)Line_str,       /* tp_str */
    0,                         /* tp_getattro */
    0,                         /* tp_setattro */
    0,                         /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /* tp_flags */
    "Line object",           /* tp_doc */
    0,                         /* tp_traverse */
    0,                         /* tp_clear */
    0,                         /* tp_richcompare */
    0,                         /* tp_weaklistoffset */
    0,                         /* tp_iter */
    0,                         /* tp_iternext */
    Line_methods,             /* tp_methods */
    Line_members,             /* tp_members */
    0,                         /* tp_getset */
    0,                         /* tp_base */
    0,                         /* tp_dict */
    0,                         /* tp_descr_get */
    0,                         /* tp_descr_set */
    0,                         /* tp_dictoffset */
    (initproc)Line_init,      /* tp_init */
    0,                         /* tp_alloc */
    Line_new,                 /* tp_new */
};

static struct PyModuleDef linemodule = {
    PyModuleDef_HEAD_INIT,
    "line",            /* name of module */
    "Line Module",     /* module documentation, may be NULL */
    -1,                /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    NULL, NULL, NULL, NULL, NULL
};

PyMODINIT_FUNC PyInit_line(void) {
    PyObject* m;
    if (PyType_Ready(&line_LineType) < 0)
        return NULL;

    m = PyModule_Create(&linemodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&line_LineType);
    PyModule_AddObject(m, "Line", (PyObject *)&line_LineType);
    return m;
}