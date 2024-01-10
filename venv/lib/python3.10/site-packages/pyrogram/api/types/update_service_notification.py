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


class UpdateServiceNotification(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xebe46819``

    Args:
        type: :obj:`string`
        message: :obj:`string`
        media: :class:`pyrogram.api.types.MessageMedia`
        entities: List of :class:`pyrogram.api.types.MessageEntity`
        popup: :obj:`bool` (optional)
        inbox_date: :obj:`int` (optional)
    """
    ID = 0xebe46819

    def __init__(self, type, message, media, entities, popup=None, inbox_date=None):
        self.popup = popup  # flags.0?true
        self.inbox_date = inbox_date  # flags.1?int
        self.type = type  # string
        self.message = message  # string
        self.media = media  # MessageMedia
        self.entities = entities  # Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateServiceNotification":
        flags = Int.read(b)
        
        popup = True if flags & (1 << 0) else False
        inbox_date = Int.read(b) if flags & (1 << 1) else None
        type = String.read(b)
        
        message = String.read(b)
        
        media = Object.read(b)
        
        entities = Object.read(b)
        
        return UpdateServiceNotification(type, message, media, entities, popup, inbox_date)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.popup is not None else 0
        flags |= (1 << 1) if self.inbox_date is not None else 0
        b.write(Int(flags))
        
        if self.inbox_date is not None:
            b.write(Int(self.inbox_date))
        
        b.write(String(self.type))
        
        b.write(String(self.message))
        
        b.write(self.media.write())
        
        b.write(Vector(self.entities))
        
        return b.getvalue()
