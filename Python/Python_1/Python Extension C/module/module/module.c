#include <Python.h>
#include "structmember.h" // T_OBJECT... etc

static PyObject *moduleError;

int is_prime(int number) 
{
	if (number < 0)// exception
	{
		moduleError = PyErr_NewException("module.is_prime", NULL, NULL);
		PyErr_SetString(moduleError, "Number cannot be negative!");
		Py_INCREF(moduleError);

		return -1;
	}

	if (number < 2) return 0;
	if (number == 2) return 1;
	if (number % 2 == 0) return 0;

	for (int i = 3; (i*i) <= number; i += 2) 
	{
		if (number % i == 0) return 0;
	}
	return 1;
}

// modulio docstring
static char module_docstring[] =
"Testinis modulis pirmai Python uzduociai";

// funkcijos docstring
static char is_prime_docstring[] =
"Nustato ar skaicius yra pirminis";

// python wrapperis
static PyObject *module_is_prime(PyObject *self, PyObject *args)
{
	int input;
	int result; // 1 0 -1 true/false/exception
	PyObject *pyObject;

	// python integer to C integer "i"
	if (!PyArg_ParseTuple(args, "i", &input))
		return NULL;// exception
		
	// do stuff
	result = is_prime(input);

	if (result == -1)// exception
		return NULL; 

	// converts result to python object
	if(result == 0)
		pyObject = Py_BuildValue("s", "false");
	else if(result == 1)
		pyObject = Py_BuildValue("s", "true");
	else return NULL;

	return pyObject;
}

// methodu lentele
static PyMethodDef module_methods[] =
{
	{ "is_prime", module_is_prime, METH_VARARGS, "" },
	{ NULL, NULL, 0, NULL }
};

// modulio inicializavimas
static struct PyModuleDef module =
{
	PyModuleDef_HEAD_INIT,
	"module",
	"Some module documentation",
	1,
	module_methods
};

// naujas tipas
typedef struct 
{
	PyObject_HEAD
	PyObject* numbers;
	int prime_numbers;
	int non_prime_numbers;

} module_SomeObject;

// init
static int module_SomeObject_init(module_SomeObject *self)
{
	self->numbers = PyList_New(0);
	self->prime_numbers = 0;
	self->non_prime_numbers = 0;
	
	return 0;
}

// dealloc
static void module_SomeObject_dealloc(module_SomeObject *self)
{
	Py_XDECREF(self->numbers);
	Py_TYPE(self)->tp_free((PyObject*)self);
}

// make data available in python
static PyMemberDef module_SomeObject_members[] =
{
	{
		"numbers",
		T_OBJECT_EX,
		offsetof(module_SomeObject, numbers),
		0,
		"List of numbers"
	},

	{
		"prime_numbers",
		T_INT,
		offsetof(module_SomeObject, prime_numbers),
		0,
		"Prime numbers counter"
	},

	{
		"non_prime_numbers",
		T_INT,
		offsetof(module_SomeObject, non_prime_numbers),
		0,
		"Non prime numbers counter"
	},

	{NULL}
};

// method #1
static PyObject* module_SomeObject_AddNumber(module_SomeObject *self, PyObject* args)
{
	int number;// input

	if (!PyArg_ParseTuple(args, "i", &number))
		return NULL;

	PyObject *python_number = Py_BuildValue("i", number);
	PyList_Append(self->numbers, python_number);
	
	int result = is_prime(number);

	if (result == 1)
		self->prime_numbers++;
	else
		self->non_prime_numbers++;

	return Py_BuildValue("s", "Successfully added a new number!");
}

// method #2
static PyObject* module_SomeObject_CountPrimeNumbers(module_SomeObject *self)
{
	PyObject *pyObject = Py_BuildValue("i", self->prime_numbers);
	return pyObject;
}

// method #3
static PyObject* module_SomeObject_CountNonPrimeNumbers(module_SomeObject * self)
{
	PyObject *pyObject = Py_BuildValue("i", self->non_prime_numbers);
	return pyObject;
}

// declare methods
static PyMethodDef module_SomeObject_methods[] = 
{
	{
		"addNumber",
		(PyCFunction)module_SomeObject_AddNumber,
		METH_VARARGS,
		"Add a number to a list of numbers"
	},

	{
		"countPrimeNumbers",
		(PyCFunction)module_SomeObject_CountPrimeNumbers,
		METH_VARARGS,
		"Get a number of prime numbers"
	},

	{
		"countNonPrimeNumbers",
		(PyCFunction)module_SomeObject_CountNonPrimeNumbers,
		METH_VARARGS,
		"Get a number of non-prime numbers"
	},

	{NULL}
};

// declare the type components
static PyTypeObject module_SomeType =
{
	PyObject_HEAD_INIT(NULL, 0)
	"module.SomeType",							/* tp_name        */
	sizeof(module_SomeObject),					/* tp_basicsize   */
	0,											/* tp_itemsize    */
	(destructor)module_SomeObject_dealloc,		/* tp_dealloc     */
	0,											/* tp_print       */
	0,											/* tp_getattr     */
	0,											/* tp_setattr     */
	0,											/* tp_compare     */
	0,											/* tp_repr        */
	0,											/* tp_as_number   */
	0,											/* tp_as_sequence */
	0,											/* tp_as_mapping  */
	0,											/* tp_hash        */
	0,											/* tp_call        */
	0,											/* tp_str         */
	0,											/* tp_getattro    */
	0,											/* tp_setattro    */
	0,											/* tp_as_buffer   */
	Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,	/* tp_flags       */
	"How many prime and non-prime \
	numbers are there?",						/* tp_doc         */
	0,											/* tp_traverse */
	0,											/* tp_clear */
	0,											/* tp_richcompare */
	0,											/* tp_weaklistoffset */
	0,											/* tp_iter */
	0,											/* tp_iternext */
	module_SomeObject_methods,					/* tp_methods */
	module_SomeObject_members,					/* tp_members */
	0,											/* tp_getset */
	0,											/* tp_base */
	0,											/* tp_dict */
	0,											/* tp_descr_get */
	0,											/* tp_descr_set */
	0,											/* tp_dictoffset */
	(initproc)module_SomeObject_init,			/* tp_init */
	0,											/* tp_alloc */
	0,											/* tp_new */
};

 PyMODINIT_FUNC PyInit_module(void)
 {
	 PyObject *m;

	 module_SomeType.tp_new = PyType_GenericNew;
	 if (PyType_Ready(&module_SomeType) < 0)
		 return NULL;

	 m = PyModule_Create(&module);
	 if (m == NULL)
		 return NULL;

	 // adds the type to the module dictionary
	 Py_INCREF(&module_SomeType);
	 PyModule_AddObject(m, "SomeType", (PyObject*)&module_SomeType);

	 return m;
 }