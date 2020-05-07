#include <Python.h>
/**
 * print_python_bytes? (- reverse list)?
 *
 * @p: input head
 * Return:
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t x = PyBytes_Size(p);

	printf("[.] bytes object info\n");
	printf("  size: %lu\n", x);
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %lu bytes: %02x\n", x, 000000);


}

/**
 * print_python_list? (- reverse list)?
 *
 * @p: input head
 * Return:
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i = 0, x = PyList_Size(p);
	PyObject *z;
	PyListObject *ls = (PyListObject *)p;

	printf("[*] Size of the Python List = %lu\n", x);
	printf("[*] Allocated = %lu\n", (unsigned long)(ls->allocated));
	if (x != 0)
	{
		while (i < x)
		{
			z = PyList_GetItem(p, i);
			printf("Element %lu: %s\n", i, Py_TYPE(z)->tp_name);
			i++;
		}
	}
}
