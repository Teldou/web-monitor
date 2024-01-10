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


class AcceptEncryption(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x3dbc0415``

    Args:
        peer: :class:`pyrogram.api.types.InputEncryptedChat`
        g_b: :obj:`bytes`
        key_fingerprint: :obj:`int`

    Returns:
        :class:`pyrogram.api.types.EncryptedChatEmpty` | :class:`pyrogram.api.types.EncryptedChatWaiting` | :class:`pyrogram.api.types.EncryptedChatRequested` | :class:`pyrogram.api.types.EncryptedChat` | :class:`pyrogram.api.types.EncryptedChatDiscarded`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x3dbc0415

    def __init__(self, peer, g_b, key_fingerprint):
        self.peer = peer  # InputEncryptedChat
        self.g_b = g_b  # bytes
        self.key_fingerprint = key_fingerprint  # long

    @staticmethod
    def read(b: BytesIO, *args) -> "AcceptEncryption":
        # No flags
        
        peer = Object.read(b)
        
        g_b = Bytes.read(b)
        
        key_fingerprint = Long.read(b)
        
        return AcceptEncryption(peer, g_b, key_fingerprint)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bytes(self.g_b))
        
        b.write(Long(self.key_fingerprint))
        
        return b.getvalue()
