import cProfile


def profile_coroutine(coroutine):
    async def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        result = None

        try:
            profiler.enable()
            result = await coroutine(*args, **kwargs)
        finally:
            profiler.disable()
            profiler.print_stats()
        return result

    return wrapper
