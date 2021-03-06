# -*- coding: utf-8 -*-
import logging
logger = logging.getLogger('rer.al.mcorevideoportlet')

from os import environ
timeout_value_str = environ.get('URLLIB_TIMEOUT', '')
try:
    DEFAULT_TIMEOUT = int(timeout_value_str)
except ValueError:
    DEFAULT_TIMEOUT = 15
    logger.warning('Environment variable URLLIB_TIMEOUT wrong: %s. We use 15s as default timeout' % timeout_value_str)
