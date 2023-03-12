#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\component\message\base.py
# @Time    :   2023-03-11 17:06:56
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0


from abc import ABCMeta, abstractmethod


class BaseMessage(metaclass=ABCMeta):
    """Base class for all messages."""

    @abstractmethod
    def serialize(self):
        """Serialize the message to bytes."""
        pass

    @abstractmethod
    def deserialize(self, message):
        """Deserialize the message from bytes."""
        pass

    @abstractmethod
    def get_type(self):
        """Get the message type."""
        pass

    @abstractmethod
    def get_sender(self):
        """Get the sender worker id."""
        pass

    @abstractmethod
    def get_receiver(self):
        """Get the receiver worker id."""
        pass

    @abstractmethod
    def get_body(self):
        """Get the message body."""
        pass

    @abstractmethod
    def set_sender(self, sender):
        """Set the sender worker id."""
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        """Set the receiver worker id."""
        pass

    @abstractmethod
    def set_body(self, body):
        """Set the message body."""
        pass
