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


class UpdateShortSentMessage(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x11f1331c``

    Args:
        id: :obj:`int`
        pts: :obj:`int`
        pts_count: :obj:`int`
        date: :obj:`int`
        out: :obj:`bool` (optional)
        media: :class:`pyrogram.api.types.MessageMedia` (optional)
        entities: List of :class:`pyrogram.api.types.MessageEntity` (optional)
    """
    ID = 0x11f1331c

    def __init__(self, id, pts, pts_count, date, out=None, media=None, entities=None):
        self.out = out  # flags.1?true
        self.id = id  # int
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.date = date  # int
        self.media = media  # flags.9?MessageMedia
        self.entities = entities  # flags.7?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateShortSentMessage":
        flags = Int.read(b)
        
        out = True if flags & (1 << 1) else False
        id = Int.read(b)
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        date = Int.read(b)
        
        media = Object.read(b) if flags & (1 << 9) else None
        
        entities = Object.read(b) if flags & (1 << 7) else []
        
        return UpdateShortSentMessage(id, pts, pts_count, date, out, media, entities)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out is not None else 0
        flags |= (1 << 9) if self.media is not None else 0
        flags |= (1 << 7) if self.entities is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        b.write(Int(self.date))
        
        if self.media is not None:
            b.write(self.media.write())
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        return b.getvalue()
