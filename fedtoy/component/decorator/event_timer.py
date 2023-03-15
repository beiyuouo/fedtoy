#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\component\decorator\event_timer.py
# @Time    :   2023-03-13 16:09:14
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0


from functools import wraps
import time
from ..timer import Timer


def event_timer(f):
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        timer = self._timer
        event = args[0]
        start_time = time.time()
        print("start_time", start_time)

        result = f(self, *args, **kwargs)

        end_time = time.time()
        print("end_time", end_time)
        delta_time = end_time - start_time
        timer.tick(delta_time=delta_time, event=event)

        return result

    return wrapper
