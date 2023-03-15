#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\core\worker\base.py
# @Time    :   2023-03-12 16:30:06
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

from fedtoy.core.communicator import get_communicator
from fedtoy.component.decorator import event_timer
from fedtoy.component.timer import Timer
from loguru import logger as loguru_logger


class BaseWorker(object):
    """Base worker.

    Args:
        cfg (Config): Config.
        logger (Logger): Logger.
    """

    def __init__(self, cfg, logger=None):
        self._cfg = cfg
        self._logger = logger or (self._cfg.logger if self._cfg else loguru_logger)

        if self._cfg:
            self._communicator = get_communicator(self._cfg.communicator)(
                self._cfg, self._logger
            )

        self._timer = Timer(self._cfg, self._logger)

        self._event_handlers = {}

        self._register_default_handler()

    def register_event_handler(self, event_type, handler):
        """Register event handler.

        Args:
            event_type (str): Event type.
            handler (function): Handler.
        """
        self._event_handlers[event_type] = handler

    def _register_default_handler(self):
        """Register default handler."""
        pass

    @event_timer
    def handle_event(self, event_type, *args, **kwargs):
        handler = self._event_handlers.get(event_type, None)
        if handler:
            handler(*args, **kwargs)
        else:
            self._log("No handler for event: {}".format(event_type))

    def _log(self, msg):
        """Log."""
        if self._logger:
            self._logger.debug(msg, extra={"component": "worker"})
