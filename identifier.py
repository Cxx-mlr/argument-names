import linecache
import inspect
import ast
import functools

def identifiers(func_=None, /, *, function):
    def decorator_identifiers(func):
        @functools.wraps(func)
        def wrapper_identifiers(*args, **kwargs):
            frame = inspect.currentframe().f_back
            try:
                frame_info = inspect.getframeinfo(frame)
                positions = frame_info.positions

                code_lns = [linecache.getline(frame.f_code.co_filename, lineno, frame.f_globals) for lineno in range(positions.lineno, positions.end_lineno + 1)]

                if len(code_lns) == 1:
                    code_lns[0] = code_lns[0][positions.col_offset:positions.end_col_offset]
                else:
                    code_lns[0] = code_lns[0][positions.col_offset:]
                    code_lns[-1] = code_lns[-1][:positions.end_col_offset]

                source = "".join(code_lns)

                identifiers = []
                for arg in ast.parse(source, mode="eval").body.args:
                    for node in ast.walk(arg):
                        if isinstance(node, ast.Name):
                            identifiers.append(node.id)
            finally:
                del frame
            function(*identifiers)
            return func(*args, **kwargs)
        return wrapper_identifiers
    if func_ is not None:
        return decorator_identifiers(func_)
    else:
        return decorator_identifiers
