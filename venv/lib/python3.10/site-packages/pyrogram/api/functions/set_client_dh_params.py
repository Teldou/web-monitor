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


class SetClientDHParams(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xf5045f1f``

    Args:
        nonce: :obj:`int`
        server_nonce: :obj:`int`
        encrypted_data: :obj:`bytes`

    Returns:
        :class:`pyrogram.api.types.DhGenOk` | :class:`pyrogram.api.types.DhGenRetry` | :class:`pyrogram.api.types.DhGenFail`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0xf5045f1f

    def __init__(self, nonce, server_nonce, encrypted_data):
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.encrypted_data = encrypted_data  # bytes

    @staticmethod
    def read(b: BytesIO, *args) -> "SetClientDHParams":
        # No flags
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        encrypted_data = Bytes.read(b)
        
        return SetClientDHParams(nonce, server_nonce, encrypted_data)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Bytes(self.encrypted_data))
        
        return b.getvalue()
