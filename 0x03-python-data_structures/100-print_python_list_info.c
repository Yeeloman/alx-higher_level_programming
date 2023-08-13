#include "Python.h"
#include <stdio.h>

/**
 *print_python_list_info - prints the infos of python list
 *@p: pointer to the list
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;

	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %d\n", list.ob_item)
	printf("[*] Allocated = %ld\n", list->allocated);
}
