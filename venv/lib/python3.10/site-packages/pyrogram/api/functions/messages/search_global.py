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


class SearchGlobal(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x9e3cacb0``

    Args:
        q: :obj:`string`
        offset_date: :obj:`int`
        offset_peer: :class:`pyrogram.api.types.InputPeer`
        offset_id: :obj:`int`
        limit: :obj:`int`

    Returns:
        :class:`pyrogram.api.types.messages.Messages` | :class:`pyrogram.api.types.messages.MessagesSlice` | :class:`pyrogram.api.types.messages.ChannelMessages` | :class:`pyrogram.api.types.messages.MessagesNotModified`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x9e3cacb0

    def __init__(self, q, offset_date, offset_peer, offset_id, limit):
        self.q = q  # string
        self.offset_date = offset_date  # int
        self.offset_peer = offset_peer  # InputPeer
        self.offset_id = offset_id  # int
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "SearchGlobal":
        # No flags
        
        q = String.read(b)
        
        offset_date = Int.read(b)
        
        offset_peer = Object.read(b)
        
        offset_id = Int.read(b)
        
        limit = Int.read(b)
        
        return SearchGlobal(q, offset_date, offset_peer, offset_id, limit)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.q))
        
        b.write(Int(self.offset_date))
        
        b.write(self.offset_peer.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
