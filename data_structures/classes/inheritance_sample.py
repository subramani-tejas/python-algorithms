from abc import ABC, abstractmethod


class InvalidOpertionError(Exception):
    pass


# abstract base class (like interface)
class Stream(ABC):
    def __init__(self) -> None:
        self.is_open = False

    def open(self):
        if self.is_open:
            raise InvalidOpertionError
        self.is_open = True

    def close(self):
        if not self.is_open:
            raise InvalidOpertionError
        self.is_open = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading data from file...")


class NetworkStream(Stream):
    def read(self):
        print("reading data from network...")
