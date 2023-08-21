#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   tests\test_unit\test_worker\test_base.py
# @Time    :   2023-03-15 23:59:34
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

from time import sleep
from fedtoy.core.worker import BaseWorker


def test_event_driven_client():
    cfg = None
    logger = None

    client = BaseWorker(cfg, logger)

    def handler1(*args, **kwargs):
        print("event1", args, kwargs)
        sleep(1)

    def handler2(*args, **kwargs):
        print("event2", args, kwargs)
        sleep(2)

    # register event handlers
    client.register_event_handler("event1", handler1)
    client.register_event_handler("event2", handler2)

    # handle events
    client.handle_event("event1", 1, 2, 3)
    client.handle_event("event2", "foo", "bar")

    # get timer
    timer = client._timer

    # verify that timer is not None
    assert timer.get_virtual_time() > 0
    assert timer.get_wall_time() > 0

    # verify that timer has recorded event times
    assert timer.get_event_time("event1") > 0
    assert timer.get_event_time("event2") > 0

    # print event times
    timer.print_event_times()
