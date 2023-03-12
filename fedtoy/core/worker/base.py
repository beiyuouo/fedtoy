#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\core\worker\base.py
# @Time    :   2023-03-12 16:30:06
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

from fedtoy.core.communicator import get_communicator


class BaseWorker(object):
    """Base worker.

    Args:
        cfg (Config): Config.
        logger (Logger): Logger.
    """

    def __init__(self, cfg, logger):
        self.cfg = cfg
        self.logger = logger
        self.communicator = get_communicator(cfg.communicator)(cfg, logger)

        self.event_handlers = {}

        self._register_default_handler()

    def register_handler(self, event_type, handler, *args, **kwargs):
        """Register handler.

        Args:
            event_type (str): Event type.
            handler (function): Handler.
            *args: Args.
            **kwargs: Kwargs.
        """
        self.event_handlers[event_type] = (handler, args, kwargs)

    def _register_default_handler(self):
        """Register default handler."""
        pass
