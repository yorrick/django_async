# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import time
import logging


logger = logging.getLogger(__name__)


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


