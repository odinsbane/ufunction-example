#include "Python.h"
#include "math.h"
#include "numpy/ndarraytypes.h"
#include "numpy/ufuncobject.h"

static PyMethodDef FunnyMethods[] = {
        {NULL, NULL, 0, NULL}
};

/* This is the loop that we want to evaluate. */

static void double_funny(char **args, npy_intp *dimensions,
                            npy_intp* steps, void* data)
{
    npy_intp i;
    npy_intp n = dimensions[0];
    char *in1 = args[0], *in2 = args[1];
    char *out1 = args[2];
    npy_intp in1_step = steps[0], in2_step = steps[1];
    npy_intp out1_step = steps[2];

    double x,y;
    
    for (i = 0; i < n; i++) {
        /*BEGIN main ufunc computation*/
        x = *(double *)in1;
        y = *(double *)in2;
        *((double *)out1) = x*x*x + x*x*y + x*y*y + y*y*y - 0.1;
        /*END main ufunc computation*/

        in1 += in1_step;
        in2 += in2_step;
        out1 += out1_step;
        
    }
}


/*This a pointer to the above function*/
PyUFuncGenericFunction funcs[1] = {&double_funny};

/* These are the input and return dtypes of logit.*/

static char types[3] = {NPY_DOUBLE, NPY_DOUBLE, NPY_DOUBLE};


static void *data[1] = {NULL};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "ufunny",
    NULL,
    -1,
    FunnyMethods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyObject *PyInit_ufunny(void)
{
    PyObject *m, *funny, *d;
    m = PyModule_Create(&moduledef);
    if (!m) {
        return NULL;
    }

    import_array();
    import_umath();

    funny = PyUFunc_FromFuncAndData(funcs, data, types, 1, 2, 1,
                                    PyUFunc_None, "funny",
                                    "funny_docstring", 0);

    d = PyModule_GetDict(m);

    PyDict_SetItemString(d, "funny", funny);
    Py_DECREF(funny);

    return m;
}
