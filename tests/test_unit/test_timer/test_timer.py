#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   tests\test_unit\test_timer\test_timer.py
# @Time    :   2023-03-15 23:51:36
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

from time import sleep
from fedtoy.component.timer import Timer


class TestTimer(object):
    def test_set_start_time(self):
        # Initialize Timer object.
        cfg = None  # Replace with an actual Config object.
        logger = None  # Replace with an actual Logger object.
        timer = Timer(cfg, logger)

        # Set start time to 10 seconds.
        timer.set_start_time(10)

        # Check that start time was set correctly.
        assert timer._start_time == 10

    def test_get_virtual_time(self):
        # Initialize Timer object.
        cfg = None  # Replace with an actual Config object.
        logger = None  # Replace with an actual Logger object.
        timer = Timer(cfg, logger)

        # Set virtual time to 20 seconds.
        timer._virtual_time = 20

        # Check that virtual time was returned correctly.
        assert timer.get_virtual_time() == 20

    def test_tick(self):
        # Initialize Timer object.
        cfg = None  # Replace with an actual Config object.
        logger = None  # Replace with an actual Logger object.
        timer = Timer(cfg, logger)

        # Save current wall time and set start time to current time.
        curr_wall_time = timer.get_wall_time()
        timer.set_start_time(curr_wall_time)

        # Tick once with delta time=5 sec.
        sleep(5)
        timer.tick(delta_time=5)

        # Check that virtual time is accurate.
        assert (
            abs(timer.get_virtual_time() - 5) < 0.2
        )  # Allow for 0.2 second error margin.

        # Tick again without specifying delta time.
        sleep(2)
        timer.tick()

        # Check that virtual time has advanced by 2 seconds.
        assert (
            abs(timer.get_virtual_time() - 7) < 0.2
        )  # Allow for 0.2 second error margin.
