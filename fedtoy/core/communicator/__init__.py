#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\core\communicator\__init__.py
# @Time    :   2023-03-11 17:18:09
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

from .base import BaseCommunicator
from .mpi import MPICommunicator

communicator_dict = {
    "base": BaseCommunicator,
    "mpi": MPICommunicator,
}


def get_communicator(name: str):
    """Get the communicator by name."""
    name = name.lower()
    if name not in communicator_dict:
        raise ValueError(
            f"Communicator {name} not found, available communicators are {communicator_dict.keys()}"
        )
    return communicator_dict[name]
