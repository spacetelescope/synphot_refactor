/* Licensed under a 3-clause BSD style license - see LICENSE.rst */

#include "Python.h"
#include <numpy/arrayobject.h>

#include "docstrings.h"


static PyObject * py_calcbinflux(PyObject *self, PyObject *args) {
  /* input variables */
  const int out_arr_len;
  PyObject *oindices, *oindices_last, *oavflux, *odeltaw;
  PyArrayObject *indices, *indices_last, *avflux, *deltaw;

  /* local variables */
  npy_intp i, j;
  npy_intp num_indices, first, last;
  double flux_sum, delta_sum;

  /* return variables */
  npy_intp *out_dim;
  PyArrayObject *binflux, *intwave;

  /* put arguments into variables */
  if (!PyArg_ParseTuple(args, "iOOOO", &out_arr_len, &oindices, &oindices_last,
                        &oavflux, &odeltaw)) {
    return NULL;
  }

  /* turn inputs into numpy array types */
  indices = (PyArrayObject *) PyArray_FROMANY(oindices, PyArray_INT64, 1, 1,
                                              NPY_IN_ARRAY);
  indices_last = (PyArrayObject *) PyArray_FROMANY(oindices_last, PyArray_INT64,
                                                   1, 1, NPY_IN_ARRAY);
  avflux = (PyArrayObject *) PyArray_FROMANY(oavflux, PyArray_FLOAT64, 1, 1,
                                             NPY_IN_ARRAY);
  deltaw = (PyArrayObject *) PyArray_FROMANY(odeltaw, PyArray_FLOAT64, 1, 1,
                                             NPY_IN_ARRAY);
  if (!indices || !indices_last || !avflux || !deltaw) {
    return NULL;
  }

  /* finish creating return variables */
  out_dim = (npy_intp *) malloc(1 * sizeof(npy_intp));
  out_dim[0] = (npy_intp) out_arr_len;
  binflux = (PyArrayObject *) PyArray_SimpleNew(1, out_dim, PyArray_FLOAT64);
  intwave = (PyArrayObject *) PyArray_SimpleNew(1, out_dim, PyArray_FLOAT64);
  if (!binflux || !intwave) {
    return NULL;
  }

  num_indices = indices->dimensions[0];

  for (i = 0; i < num_indices; i++) {
    first = (npy_intp) *(npy_int64 *) PyArray_GETPTR1(indices,i);
    last = (npy_intp) *(npy_int64 *) PyArray_GETPTR1(indices_last,i);

    flux_sum = 0.0;
    delta_sum = 0.0;

    for (j = first; j < last; j++) {
      delta_sum += *(double *) PyArray_GETPTR1(deltaw, j);
      flux_sum += (*(double *) PyArray_GETPTR1(avflux, j)) *
                  (*(double *) PyArray_GETPTR1(deltaw, j));
    }

    if (delta_sum == 0) {
      PyErr_SetString(PyExc_ZeroDivisionError,
                      "Division by zero in synphot_utils.calcbinflux.");
      return NULL;
    }

    *(npy_float64 *) PyArray_GETPTR1(intwave,i) = (npy_float64) delta_sum;
    *(npy_float64 *) PyArray_GETPTR1(binflux,i) = (npy_float64) (flux_sum/delta_sum);
  }

  free(out_dim);

  Py_DECREF(indices);
  Py_DECREF(indices_last);
  Py_DECREF(avflux);
  Py_DECREF(deltaw);

  return Py_BuildValue("NN", binflux, intwave);
}


static PyMethodDef synphot_utils_methods[] =
{
  {"calcbinflux", (PyCFunction)py_calcbinflux, METH_VARARGS, doc_calcbinflux},
  {NULL}  /* sentinel */
};


#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef moduledef = {
  PyModuleDef_HEAD_INIT,
  "synphot_utils",     /* m_name */
  NULL,  /* m_doc */
  -1,                  /* m_size */
  synphot_utils_methods,    /* m_methods */
  NULL,                /* m_reload */
  NULL,                /* m_traverse */
  NULL,                /* m_clear */
  NULL,                /* m_free */
};
#endif


PyMODINIT_FUNC
#if PY_MAJOR_VERSION >= 3
PyInit_synphot_utils(void)
#else
initsynphot_utils(void)
#endif
{
#if PY_MAJOR_VERSION >= 3
  PyObject *module = PyModule_Create(&moduledef);
#else
  (void) Py_InitModule("synphot_utils", synphot_utils_methods);
#endif

  import_array(); /* Must be present for NumPy */

#if PY_MAJOR_VERSION >= 3
  return module;
#endif
}
