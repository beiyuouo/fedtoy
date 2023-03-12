#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\__init__.py
# @Time    :   2023-03-12 16:04:25
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

from fedtoy.cfg import Config
from fedtoy.logger import get_logger


def init():
    """Init fedtoy."""

    # init config
    cfg = Config().parse_cfg()

    # init logger
    logger = get_logger(cfg)

    # worker and communicator init

    return cfg, logger
