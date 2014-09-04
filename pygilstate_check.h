/* Function to check whether the current thread has acquired the GIL.
 * Return 1 if the current thread is holding the GIL and 0 otherwise.
 *
 * This is a kind-of untested backport of
 * https://docs.python.org/3/c-api/init.html?highlight=pygilstate_check#c.PyGILState_Check
 * It can be useful in debugging deadlocks/crashes in python-c api
 * usage by checking whether the GIL is acquired or not where expected.
 */
int PyGILState_Check2(void);
