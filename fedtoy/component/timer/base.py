#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\component\timer\base.py
# @Time    :   2023-03-13 14:00:35
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

import time


class Timer(object):
    """Timer.

    Args:
        cfg (Config): Config.
        logger (Logger): Logger.
    """

    def __init__(self, cfg, logger):
        self._cfg = cfg
        self._logger = logger

        self._start_time = 0
        self._virtual_time = 0
        self._event_times = {}  # 记录每种事件的总耗时

    def set_start_time(self, start_time):
        """Set start time.

        Args:
            start_time (int): Start time.
        """
        self._start_time = start_time

    def get_virtual_time(self):
        """Get virtual time.

        Returns:
            int: Virtual time.
        """
        return self._virtual_time

    def get_wall_time(self):
        """Get wall time.

        Returns:
            int: Wall time.
        """
        return int(time.time())

    def _log(self, msg):
        """Log.

        Args:
            msg (str): Message.
        """
        if self._logger:
            self._logger.debug(msg, extra={"component": "timer"})

    def tick(self, delta_time=None, event=None):
        """Tick."""
        if delta_time is None:
            self._virtual_time = self.get_wall_time() - self._start_time
        else:
            self._virtual_time += delta_time

        # 记录每种事件的总耗时
        if event is not None:
            if event not in self._event_times:
                self._event_times[event] = 0
            self._event_times[event] += delta_time

        msg = f"[[tick]] virtual_time: {self._virtual_time} | delta_time: {delta_time} | event: {event} | wall_time: {self.get_wall_time()}"
        self._log(msg)

    def get_event_time(self, event):
        """Get event time.

        Args:
            event (str): Event.

        Returns:
            int: Event time.
        """
        return self._event_times.get(event, 0)

    def print_event_times(self):
        """Print event times."""
        for event, time in self._event_times.items():
            self._log(f"[[event_time]] event: {event} | time: {time}")
