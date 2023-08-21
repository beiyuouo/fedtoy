#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\component\event\event_type.py
# @Time    :   2023-03-16 11:03:52
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

class EventType:
    """Event type.
    """

    AGGREGATE_EVENT = "aggregate_event"
    TRAIN_EVENT = "train_event"
    EVAL_EVENT = "eval_event"
    PREDICT_EVENT = "predict_event"
    UPDATE_EVENT = "update_event"

    COMMUNICATION_EVENT = "communication_event"
    SEND_EVENT = "send_event"
    RECEIVE_EVENT = "receive_event"
    