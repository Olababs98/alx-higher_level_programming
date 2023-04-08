#include <python.h>

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
    long int length;

    printf("[.] string object info\n");

    if (p == NULL || !PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GetLength(p);

    printf("  type: %s\n", p->ob_type->tp_name);
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
