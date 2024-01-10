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


class DiscardCall(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x78d413a6``

    Args:
        peer: :class:`pyrogram.api.types.InputPhoneCall`
        duration: :obj:`int`
        reason: :class:`pyrogram.api.types.PhoneCallDiscardReason`
        connection_id: :obj:`int`

    Returns:
        :class:`pyrogram.api.types.UpdatesTooLong` | :class:`pyrogram.api.types.UpdateShortMessage` | :class:`pyrogram.api.types.UpdateShortChatMessage` | :class:`pyrogram.api.types.UpdateShort` | :class:`pyrogram.api.types.UpdatesCombined` | :class:`pyrogram.api.types.Update` | :class:`pyrogram.api.types.UpdateShortSentMessage`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x78d413a6

    def __init__(self, peer, duration, reason, connection_id):
        self.peer = peer  # InputPhoneCall
        self.duration = duration  # int
        self.reason = reason  # PhoneCallDiscardReason
        self.connection_id = connection_id  # long

    @staticmethod
    def read(b: BytesIO, *args) -> "DiscardCall":
        # No flags
        
        peer = Object.read(b)
        
        duration = Int.read(b)
        
        reason = Object.read(b)
        
        connection_id = Long.read(b)
        
        return DiscardCall(peer, duration, reason, connection_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.duration))
        
        b.write(self.reason.write())
        
        b.write(Long(self.connection_id))
        
        return b.getvalue()
