class GOST3412Kuz(object):
    def __init__(self, key: bytes) -> None: ...

    def encrypt(self, blk: bytes) -> bytes: ...

    def decrypt(self, blk: bytes) -> bytes: ...
