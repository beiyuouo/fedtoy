#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\core\communicator\dist.py
# @Time    :   2023-03-18 16:09:43
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

import torch
import os
import torch.distributed as dist


class DistributedCommunicator:
    def __init__(self, cfg, logger=None):
        self.world_size = cfg.dist.world_size
        self.rank = cfg.dist.rank
        self.init_method = cfg.dist.init_method
        self.backend = cfg.dist.backend
        self.dist_initialized = False

    def initialize(self):
        if not self.dist_initialized:
            dist.init_process_group(
                backend=self.backend,
                init_method=self.init_method,
                world_size=self.world_size,
                rank=self.rank,
            )
            self.dist_initialized = True

    def finalize(self):
        if self.dist_initialized:
            dist.destroy_process_group()
            self.dist_initialized = False

    def broadcast(self, data, src=0):
        self.initialize()
        dist.broadcast(data, src=src)

    def all_gather(self, data):
        self.initialize()
        gathered_data = [torch.zeros_like(data) for _ in range(self.world_size)]
        dist.all_gather(gathered_data, data)
        return gathered_data

    def reduce(self, data, op=dist.ReduceOp.SUM, dst=0):
        self.initialize()
        dist.reduce(data, dst, op)

    def all_reduce(self, data, op=dist.ReduceOp.SUM):
        self.initialize()
        dist.all_reduce(data, op)
