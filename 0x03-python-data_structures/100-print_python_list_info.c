#include <Python.h>

/**
 * print_python_list_info? (- reverse list)?
 *
 * @h: input head
 * Return: n
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0, x = Py_SIZE(p);
	PyObject *z;
	PyListObject *ls = (PyListObject *)p;

	printf("[*] Size of the Python List = %lu\n",x);
	printf("[*] Allocated = %lu\n", (unsigned long)(ls->allocated));
	if (x != 0)
	{
		while (i < x)
		{
			z = PyList_GetItem(p, i);
			printf("Element %lu: %s\n",i, Py_TYPE(z)->tp_name);
			i++;
		}
	}
}
