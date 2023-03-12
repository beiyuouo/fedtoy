#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   fedtoy\core\communicator\base.py
# @Time    :   2023-03-11 17:04:47
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0


from abc import ABCMeta, abstractmethod


class BaseCommunicator(metaclass=ABCMeta):
    """Base class for all communicators.

    Communicators are used to send and receive messages between workers.
    """

    @abstractmethod
    def send(self, message, dest):
        """Send a message to a destination worker.

        Args:
            message (bytes): Message to be sent.
            dest (int): Destination worker id.
        """
        pass

    @abstractmethod
    def recv(self, source):
        """Receive a message from a source worker.

        Args:
            source (int): Source worker id.

        Returns:
            bytes: Received message.
        """
        pass

    @abstractmethod
    def broadcast(self, message, root):
        """Broadcast a message from root worker to all workers.

        Args:
            message (bytes): Message to be broadcasted.
            root (int): Root worker id.

        Returns:
            bytes: Received message.
        """
        pass

    @abstractmethod
    def reduce(self, message, op, root):
        """Reduce a message from all workers to root worker.

        Args:
            message (bytes): Message to be reduced.
            op (str): Reduce operation, can be "sum" or "mean".
            root (int): Root worker id.

        Returns:
            bytes: Received message.
        """
        pass

    @abstractmethod
    def finalize(self):
        """Finalize the communicator."""
        pass

    @abstractmethod
    def get_rank(self):
        """Get rank of current worker.

        Returns:
            int: Rank of current worker.
        """
        pass

    @abstractmethod
    def get_size(self):
        """Get number of workers.

        Returns:
            int: Number of workers.
        """
        pass

    @abstractmethod
    def get_name(self):
        """Get name of the communicator.

        Returns:
            str: Name of the communicator.
        """
        pass
