#include <Python.h>
/**
 * print_python_list? (- reverse list)?
 *
 * @h: input head
 * Return: n
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t /*i = 0,*/ x = PyBytes_Size(p);
/*	int m = 0;
	if (*p)
	{
*/		printf("[.] bytes object info\n");
		printf("  size: %lu\n",x);
		printf("  trying string: %s\n", PyBytes_AsString(p));
		/*len = first Number of bytes if <= 10;*/
/*		for (;m <= 10; m++)
			;
		for (;i <= 10 || (unsigned int)p[i]; i++)
		printf("  first %d bytes: %02x\n",m, (unsigned int)p[i]);
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object");
	}
*/



}

/**
 * print_python_list? (- reverse list)?
 *
 * @h: input head
 * Return: n
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i = 0, x = PyList_Size(p);
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
