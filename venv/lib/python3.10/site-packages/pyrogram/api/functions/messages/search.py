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


class Search(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x8614ef68``

    Args:
        peer: :class:`pyrogram.api.types.InputPeer`
        q: :obj:`string`
        filter: :class:`pyrogram.api.types.MessagesFilter`
        min_date: :obj:`int`
        max_date: :obj:`int`
        offset_id: :obj:`int`
        add_offset: :obj:`int`
        limit: :obj:`int`
        max_id: :obj:`int`
        min_id: :obj:`int`
        hash: :obj:`int`
        from_id: :class:`pyrogram.api.types.InputUser` (optional)

    Returns:
        :class:`pyrogram.api.types.messages.Messages` | :class:`pyrogram.api.types.messages.MessagesSlice` | :class:`pyrogram.api.types.messages.ChannelMessages` | :class:`pyrogram.api.types.messages.MessagesNotModified`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x8614ef68

    def __init__(self, peer, q, filter, min_date, max_date, offset_id, add_offset, limit, max_id, min_id, hash, from_id=None):
        self.peer = peer  # InputPeer
        self.q = q  # string
        self.from_id = from_id  # flags.0?InputUser
        self.filter = filter  # MessagesFilter
        self.min_date = min_date  # int
        self.max_date = max_date  # int
        self.offset_id = offset_id  # int
        self.add_offset = add_offset  # int
        self.limit = limit  # int
        self.max_id = max_id  # int
        self.min_id = min_id  # int
        self.hash = hash  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "Search":
        flags = Int.read(b)
        
        peer = Object.read(b)
        
        q = String.read(b)
        
        from_id = Object.read(b) if flags & (1 << 0) else None
        
        filter = Object.read(b)
        
        min_date = Int.read(b)
        
        max_date = Int.read(b)
        
        offset_id = Int.read(b)
        
        add_offset = Int.read(b)
        
        limit = Int.read(b)
        
        max_id = Int.read(b)
        
        min_id = Int.read(b)
        
        hash = Int.read(b)
        
        return Search(peer, q, filter, min_date, max_date, offset_id, add_offset, limit, max_id, min_id, hash, from_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.from_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(String(self.q))
        
        if self.from_id is not None:
            b.write(self.from_id.write())
        
        b.write(self.filter.write())
        
        b.write(Int(self.min_date))
        
        b.write(Int(self.max_date))
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.add_offset))
        
        b.write(Int(self.limit))
        
        b.write(Int(self.max_id))
        
        b.write(Int(self.min_id))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
