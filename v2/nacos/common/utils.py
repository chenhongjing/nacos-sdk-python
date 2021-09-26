import ctypes
import threading
import time
from threading import Thread

from v2.nacos.exception.nacos_exception import NacosException


def get_current_time_millis():
    t = time.time()
    return int(round(t * 1000))


def synchronized_with_attr(lock_name):
    def decorator(method):
        def synced_method(self, *args, **kws):
            lock = getattr(self, lock_name)
            with lock:
                return method(self, *args, **kws)

        return synced_method

    return decorator


class ConvertUtils:
    NULL_STR = "null"

    @staticmethod
    def to_int(val: str, default_value: int):
        if not val.strip() or val.lower() == ConvertUtils.NULL_STR:
            return default_value
        try:
            return int(val.strip())
        except NacosException:
            return default_value


# def terminate_thread(thread):
#     """Terminates a python thread from another thread.
#
#     :param thread: a threading.Thread instance
#     """
#     if not thread.isAlive():
#         return
#
#     exc = ctypes.py_object(SystemExit)
#     res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
#         ctypes.c_long(thread.ident), exc)
#     if res == 0:
#         raise ValueError("nonexistent thread id")
#     elif res > 1:
#         # """if it returns a number greater than one, you're in trouble,
#         # and you should call it again with exc=NULL to revert the effect"""
#         ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
#         raise SystemError("PyThreadState_SetAsyncExc failed")

def terminate_thread(thread):
    """raises the exception, performs cleanup if needed"""
    tid = thread.ident
    tid = ctypes.c_long(tid)

    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(SystemExit))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")