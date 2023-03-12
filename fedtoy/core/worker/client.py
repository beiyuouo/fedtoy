#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\core\worker\client.py
# @Time    :   2023-03-12 16:38:02
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

from .base import BaseWorker


class BaseClient(BaseWorker):
    """Base client.

    Args:
        cfg (Config): Config.
        logger (Logger): Logger.
    """

    def __init__(self, cfg, logger):
        super(BaseClient, self).__init__(cfg, logger)

        self._register_default_handler()

    def _register_default_handler(self):
        """Register default handler."""
        super(BaseClient, self)._register_default_handler()
        pass
