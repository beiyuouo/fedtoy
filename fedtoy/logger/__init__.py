#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\logger\__init__.py
# @Time    :   2023-03-12 16:07:55
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

import loguru


def get_logger(cfg):
    """Get logger.

    Args:
        cfg (Config): Config.

    Returns:
        logger: Logger.
    """
    logger = loguru.logger
    logger.remove()
    logger.add(
        sink=cfg.log_dir / cfg.log_file,
        level=cfg.log_level,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file}:{line} | {message}",
    )
    return logger
