import sys
import logging
import io
import functools


def logger(func=None, *, handle=sys.stdout):
    def decorator(f):
        @functools.wraps(f)
        def swapper(*args, **kwargs):
            start_msg = f"start {f.__name__} with args={args}, kwargs={kwargs}"
            if isinstance(handle, logging.Logger):
                handle.info(start_msg)
            elif isinstance(handle, io.StringIO):
                handle.write(f"[INFO] {start_msg}\n")
            else:
                handle.write(f"[INFO] {start_msg}\n")
                handle.flush()
            try:
                result = f(*args, **kwargs)
                success_msg = f"success {f.__name__} with result: {result} \n"
                if isinstance(handle, logging.Logger):
                    handle.info(success_msg)
                elif isinstance(handle, io.StringIO):
                    handle.write(f"[INFO] {success_msg}\n")
                else:
                    handle.write(f"[INFO] {success_msg}\n")
                    handle.flush()
                return result

            except Exception as e:
                # log loi
                error_msg = f"error in {f.__name__} with args={args}: {type(e).__name__}: {str(e)}"
                if isinstance(handle, logging.Logger):
                    handle.error(error_msg)
                elif isinstance(handle, io.StringIO):
                    handle.write(f"[ERROR] {error_msg}\n")
                else:
                    handle.write(f"[ERROR] {error_msg}\n")
                    handle.flush()
                raise e

        return swapper

    if func is None:
        return decorator
    else:
        return decorator(func)
