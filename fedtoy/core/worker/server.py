#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\core\worker\server.py
# @Time    :   2023-03-12 16:37:10
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

from .base import BaseWorker


class BaseServer(BaseWorker):
    """Base server.

    Args:
        cfg (Config): Config.
        logger (Logger): Logger.
    """

    def __init__(self, cfg, logger):
        super(BaseServer, self).__init__(cfg, logger)

        self._register_default_handler()

    def _register_default_handler(self):
        """Register default handler."""
        super(BaseServer, self)._register_default_handler()

        pass
