#include <Python.h>

int main(int argc, char *argv[])
{
	PyObject *pScriptName, *pModule, *pDict, *pFunc;
	PyObject *pArgs, *pValue; 
	int i;

	// argv[0] my program
 	// argv[1] script name
	// argv[2] function name
	// argv [3..] arguments
	// argc - how many command line args are passed to main()

	fprintf(stderr, "\n");

	if (argc < 3)
	{
		fprintf(stderr, "ERROR: Too few arguments\n");
		return 1;
	}

	Py_Initialize();

	pScriptName = PyUnicode_DecodeFSDefault(argv[1]); 
	pModule = PyImport_Import(pScriptName);
	Py_DECREF(pScriptName);

	if (pModule != NULL)
	{
		pFunc = PyObject_GetAttrString(pModule, argv[2]);

		if (pFunc && PyCallable_Check(pFunc))
		{
			pArgs = PyTuple_New(argc - 3);
			for (i = 0; i < argc - 3; ++i)
			{
				pValue = PyLong_FromLong(atoi(argv[i + 3]));
				if (!pValue)
				{
					Py_DECREF(pArgs);
					Py_DECREF(pModule);
					fprintf(stderr, "ERROR: Cannot convert argument\n");
					return 1;
				}
				PyTuple_SetItem(pArgs, i, pValue);// insert a ref to pValue at i of tuple pointed to by pArgs
												  // kortezas pasiema reference i pValue ir tampa atsakingas uz vietos atlaisvinima (steals a ref)
			}
			pValue = PyObject_CallObject(pFunc, pArgs);
			Py_DECREF(pArgs);
			if (pValue != NULL)
			{
				int result = PyLong_AsLong(pValue);

				if(result == 1)
					printf("Result of Python func \"\%s\" call: True\n", argv[2]);
				else 
					printf("Result of Python func \"\%s\" call: False\n", argv[2]);
				Py_DECREF(pValue);
			}
			else
			{
				Py_DECREF(pFunc);
				Py_DECREF(pModule);
				PyErr_Print();
				fprintf(stderr, "ERROR: Function call failed\n");

				return 1;
			}
		}
		else
		{
			if (PyErr_Occurred())
				PyErr_Print();
			fprintf(stderr, "ERROR: Function \"%s\" not found\n", argv[2]);
		}
		Py_XDECREF(pFunc);
		Py_DECREF(pModule);
	}
	else
	{
		PyErr_Print();
		fprintf(stderr, "ERROR: Failed to load the script, named \"%s\"\n", argv[1]);
		return 1;
	}

	Py_Finalize();
	return 0;
}
