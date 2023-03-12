#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   tests\test_unit\test_commuicator\test_mpi.py
# @Time    :   2023-03-11 17:17:33
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0


import pytest

from fedtoy.core.communicator import get_communicator


class TestMPICommunicator:
    """Test MPI communicator."""

    def test_get_communicator(self):
        """Test get communicator."""
        communicator = get_communicator("mpi")()
        assert communicator.get_name() == "mpi"
        assert communicator.get_rank() == 0
        assert communicator.get_size() == 1
