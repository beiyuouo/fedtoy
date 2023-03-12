#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\core\communicator\mpi\mpi.py
# @Time    :   2023-03-11 17:08:51
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

import mpi4py.MPI as MPI

from fedtoy.core.communicator.base import BaseCommunicator


class MPICommunicator(BaseCommunicator):
    """MPI communicator."""

    def __init__(self, cfg=None, logger=None):
        self.comm = MPI.COMM_WORLD
        self.rank = self.comm.Get_rank()
        self.size = self.comm.Get_size()

    def send(self, message, dest):
        self.comm.send(message, dest=dest)

    def recv(self, source):
        return self.comm.recv(source=source)

    def barrier(self):
        self.comm.Barrier()

    def broadcast(self, message, root):
        return self.comm.bcast(message, root=root)

    def reduce(self, message, op, root):
        return self.comm.reduce(message, op=op, root=root)

    def get_rank(self):
        return self.rank

    def get_size(self):
        return self.size

    def get_name(self):
        return "mpi"

    def __str__(self):
        return f"MPICommunicator(rank={self.rank}, size={self.size})"

    def __repr__(self):
        return f"MPICommunicator(rank={self.rank}, size={self.size})"

    def finalize(self):
        self.comm.Free()
