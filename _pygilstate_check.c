#include <Python.h>
#include <stdio.h>

#include "pygilstate_check.h"

extern PyThreadState * _PyThreadState_Current;


int PyGILState_Check2(void) {
  PyThreadState * tstate = _PyThreadState_Current;
#ifdef DEBUG
  printf("%p; %p\n", (void*)tstate, (void*)PyGILState_GetThisThreadState());
#endif
  return tstate && (tstate == PyGILState_GetThisThreadState());
}
