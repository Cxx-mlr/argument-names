__version__ = "0.1.0a1"

import inspect
import functools
import dis

def argument_names(func_=None, /, *, function = None):
    def decorator_argument_names(func):
        @functools.wraps(func)
        def wrapper_argument_names(*args, **kwargs):
            frame = inspect.currentframe().f_back
            try:
                instructions = list(dis.get_instructions(frame.f_code))
                relevant_instructions = [instr for instr in instructions if instr.offset <= frame.f_lasti]

                names = []

                for instr in reversed(relevant_instructions):
                    if instr.opname in ("LOAD_NAME",):
                        names.append(instr.argval)
                    if len(names) == len(args):
                        break
                
                if function is not None:
                    function(*names[::-1])

                return func(*args, **kwargs)
            finally:
                del frame
                return func(*args, **kwargs)
        return wrapper_argument_names
    
    if func_ is None:
        return decorator_argument_names
    else:
        return decorator_argument_names(func_)