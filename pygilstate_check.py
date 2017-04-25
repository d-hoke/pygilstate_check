import ctypes
import glob
from os.path import realpath, dirname, join
import sys

__all__ = ['gilstate_check', 'gilstate_check_py']

_ext = {'win32':'pyd', 'darwin':'dylib'}.get(sys.platform, 'so')
_libname = join(dirname(realpath(__file__)), '_pygilstate_check.'+_ext)

_lib = ctypes.cdll.LoadLibrary(_libname)
_pylib = ctypes.pydll.LoadLibrary(_libname)

gilstate_check = lambda: _lib.PyGILState_Check2()==1
gilstate_check_py = lambda: _pylib.PyGILState_Check2()==1

def test():
    assert not gilstate_check()
    assert gilstate_check_py()

if __name__ == '__main__':
    test()
