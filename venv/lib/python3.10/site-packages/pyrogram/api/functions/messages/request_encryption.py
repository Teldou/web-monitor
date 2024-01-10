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


class RequestEncryption(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xf64daf43``

    Args:
        user_id: :class:`pyrogram.api.types.InputUser`
        random_id: :obj:`int`
        g_a: :obj:`bytes`

    Returns:
        :class:`pyrogram.api.types.EncryptedChatEmpty` | :class:`pyrogram.api.types.EncryptedChatWaiting` | :class:`pyrogram.api.types.EncryptedChatRequested` | :class:`pyrogram.api.types.EncryptedChat` | :class:`pyrogram.api.types.EncryptedChatDiscarded`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0xf64daf43

    def __init__(self, user_id, random_id, g_a):
        self.user_id = user_id  # InputUser
        self.random_id = random_id  # int
        self.g_a = g_a  # bytes

    @staticmethod
    def read(b: BytesIO, *args) -> "RequestEncryption":
        # No flags
        
        user_id = Object.read(b)
        
        random_id = Int.read(b)
        
        g_a = Bytes.read(b)
        
        return RequestEncryption(user_id, random_id, g_a)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(Int(self.random_id))
        
        b.write(Bytes(self.g_a))
        
        return b.getvalue()
