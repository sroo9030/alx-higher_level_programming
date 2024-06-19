#include <Python.h>

/**
  * print_python_list - Print basic info about Python lists
  * @p: Python object
  */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
		Py_ssize_t size = PyList_Size(p);
		Py_ssize_t i;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List: %ld\n", size);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (i = 0; i < size; ++i)
			printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
	else
		fprintf(stderr, "Invalid List Object\n");
}

/**
  * print_python_bytes - Print basic info about Python bytes objects
  * @p: Python object
  */
void print_python_bytes(PyObject *p)
{
	char *bytes_str;

	if (PyBytes_Check(p))
	{
		Py_ssize_t size = PyBytes_Size(p);
		Py_ssize_t i;

		printf("[.] bytes object info\n");
		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", PyUnicode_AsUTF8(PyObject_Str(p)));
		printf("  first %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
		bytes_str = PyBytes_AsString(p);

		for (i = 0; i < size + 1 && i < 10; ++i)
			printf("%02hhx ", bytes_str[i]);

		printf("\n");
	}
	else
		fprintf(stderr, "Invalid Bytes Object\n");
}
