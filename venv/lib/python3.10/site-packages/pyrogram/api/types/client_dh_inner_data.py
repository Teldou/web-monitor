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


class ClientDHInnerData(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x6643b654``

    Args:
        nonce: :obj:`int`
        server_nonce: :obj:`int`
        retry_id: :obj:`int`
        g_b: :obj:`bytes`
    """
    ID = 0x6643b654

    def __init__(self, nonce, server_nonce, retry_id, g_b):
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.retry_id = retry_id  # long
        self.g_b = g_b  # bytes

    @staticmethod
    def read(b: BytesIO, *args) -> "ClientDHInnerData":
        # No flags
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        retry_id = Long.read(b)
        
        g_b = Bytes.read(b)
        
        return ClientDHInnerData(nonce, server_nonce, retry_id, g_b)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Long(self.retry_id))
        
        b.write(Bytes(self.g_b))
        
        return b.getvalue()
