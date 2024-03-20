"""Abstract class"""

# abstract base class is a blueprint for other classes
# it means that the other classes are derieved from it but it is new initialized
# if a class is used as blueprint of other class but it is not abstract base class
# then this class can be initiated. To prevent this abstract class is declared

from abc import ABC, abstractmethod


class InvalidOperatiornError(Exception):
    """Extending exception class"""


class Stream(ABC):
    """Stream base abstract class"""

    def __init__(self):
        self.open = False

    def open_stream(self):
        """open method"""
        if self.open:
            raise InvalidOperatiornError("Stream Already open")

    def close_stream(self):
        """open method"""
        if self.open:
            raise InvalidOperatiornError("Stream Already open")

    @abstractmethod
    def read(self):
        """read abstract method"""


class FileStream(Stream):
    """file stream class"""

    def read(self):
        """read method"""
        print("Reading from file stream")


class NetWorkStream(Stream):
    """file stream class"""

    def read(self):
        """read method"""
        print("Reading from network stream")


n = NetWorkStream()
n.read()
