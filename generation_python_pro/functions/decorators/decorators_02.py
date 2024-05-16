import functools
import time



def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value
    return wrapper_debug




def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down




def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)





def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__}()")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls






def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if wrapper_singleton.instance is None:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton





@singleton
class TheOne:
    pass


first_one = TheOne()
another_one = TheOne()

print(id(first_one))


print(id(another_one))


print(first_one is another_one)



import functools

# ...

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = {}
    return wrapper_cache























# @count_calls
# def say_whee():
#     print("Whee!")
#
#
# say_whee()
#
# say_whee()
#
# say_whee()
#
#
#
# print(say_whee.__dict__)


















# # @repeat
# def say_whee():
#     print("Whee!")
#
#
# # @repeat(num_times=3)
# def greet(name):
#     print(f"Hello {name}")
#
# say_whee = repeat(say_whee)
#
# say_whee()
#
# greet = repeat()(greet)
#
# greet("Penny")











# make_greeting("Benjamin")
# print()
# make_greeting("Juan", age=114)
# print()
# make_greeting(name="Maria", age=116)





# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         sum([number**2 for number in range(10_000)])
#
#
# @timer
# def waste_map_time(num_times):
#     for _ in range(num_times):
#         sum((map(lambda x: x**2, range(10_000))))
#
#
# waste_some_time(99)
# waste_map_time(99)

























