# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2018 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.api.core import *


class PQInnerDataTemp(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x3c6a84d4``

    Args:
        pq: :obj:`bytes`
        p: :obj:`bytes`
        q: :obj:`bytes`
        nonce: :obj:`int`
        server_nonce: :obj:`int`
        new_nonce: :obj:`int`
        expires_in: :obj:`int`
    """
    ID = 0x3c6a84d4

    def __init__(self, pq, p, q, nonce, server_nonce, new_nonce, expires_in):
        self.pq = pq  # bytes
        self.p = p  # bytes
        self.q = q  # bytes
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.new_nonce = new_nonce  # int256
        self.expires_in = expires_in  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "PQInnerDataTemp":
        # No flags
        
        pq = Bytes.read(b)
        
        p = Bytes.read(b)
        
        q = Bytes.read(b)
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        new_nonce = Int256.read(b)
        
        expires_in = Int.read(b)
        
        return PQInnerDataTemp(pq, p, q, nonce, server_nonce, new_nonce, expires_in)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.pq))
        
        b.write(Bytes(self.p))
        
        b.write(Bytes(self.q))
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Int256(self.new_nonce))
        
        b.write(Int(self.expires_in))
        
        return b.getvalue()
