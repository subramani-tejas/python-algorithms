class InvalidOpertionError(Exception):
    pass


class Stream:
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


class FileStream(Stream):
    def read(self):
        print("reading data from file...")


class NetworkStream(Stream):
    def read(self):
        print("reading data from network...")
