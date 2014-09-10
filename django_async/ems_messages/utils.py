import contextlib
from decorator import decorator
from django.utils.translation import activate, get_language
import time
import logging


logger = logging.getLogger(__name__)


def logged(the_logger):
    """
    Protects a view if given product is not activated
    """
    @decorator
    def internal_decorator(func, *args, **kwargs):
        the_logger.debug('Calling function {} with parameters {} {}'.format(func, args, kwargs))
        result = func(*args, **kwargs)
        the_logger.debug('Function result: {}'.format(result))
        return result

    return internal_decorator


@contextlib.contextmanager
def language(code):
    """
    Activate given language
    """
    old_lang = get_language()
    activate(code)
    try:
        yield
    finally:
        activate(old_lang)


class TimerMiddleware(object):

    def process_request(self, request):
        request.logging_start_time = time.time()

    def process_response(self, request, response):
        response.logging_end_time = time.time()
        response.logging_start_time = request.logging_start_time
        response.logging_elapsed_time =  (response.logging_end_time - response.logging_start_time)

        logger.debug('Handled request {} in {} seconds'.format(request.path, response.logging_elapsed_time))

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        logger.debug('Process view {}'.format(view_func))


