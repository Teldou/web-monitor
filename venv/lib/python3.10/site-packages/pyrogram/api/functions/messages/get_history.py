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


class GetHistory(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xdcbb8260``

    Args:
        peer: :class:`pyrogram.api.types.InputPeer`
        offset_id: :obj:`int`
        offset_date: :obj:`int`
        add_offset: :obj:`int`
        limit: :obj:`int`
        max_id: :obj:`int`
        min_id: :obj:`int`
        hash: :obj:`int`

    Returns:
        :class:`pyrogram.api.types.messages.Messages` | :class:`pyrogram.api.types.messages.MessagesSlice` | :class:`pyrogram.api.types.messages.ChannelMessages` | :class:`pyrogram.api.types.messages.MessagesNotModified`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0xdcbb8260

    def __init__(self, peer, offset_id, offset_date, add_offset, limit, max_id, min_id, hash):
        self.peer = peer  # InputPeer
        self.offset_id = offset_id  # int
        self.offset_date = offset_date  # int
        self.add_offset = add_offset  # int
        self.limit = limit  # int
        self.max_id = max_id  # int
        self.min_id = min_id  # int
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetHistory":
        # No flags
        
        peer = Object.read(b)
        
        offset_id = Int.read(b)
        
        offset_date = Int.read(b)
        
        add_offset = Int.read(b)
        
        limit = Int.read(b)
        
        max_id = Int.read(b)
        
        min_id = Int.read(b)
        
        hash = Int.read(b)
        
        return GetHistory(peer, offset_id, offset_date, add_offset, limit, max_id, min_id, hash)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.offset_date))
        
        b.write(Int(self.add_offset))
        
        b.write(Int(self.limit))
        
        b.write(Int(self.max_id))
        
        b.write(Int(self.min_id))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
