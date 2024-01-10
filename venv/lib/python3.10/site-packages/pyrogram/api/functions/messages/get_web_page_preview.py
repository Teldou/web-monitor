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


class GetWebPagePreview(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x8b68b0cc``

    Args:
        message: :obj:`string`
        entities: List of :class:`pyrogram.api.types.MessageEntity` (optional)

    Returns:
        :class:`pyrogram.api.types.MessageMediaEmpty` | :class:`pyrogram.api.types.MessageMediaPhoto` | :class:`pyrogram.api.types.MessageMediaGeo` | :class:`pyrogram.api.types.MessageMediaContact` | :class:`pyrogram.api.types.MessageMediaUnsupported` | :class:`pyrogram.api.types.MessageMediaDocument` | :class:`pyrogram.api.types.MessageMediaWebPage` | :class:`pyrogram.api.types.MessageMediaVenue` | :class:`pyrogram.api.types.MessageMediaGame` | :class:`pyrogram.api.types.MessageMediaInvoice` | :class:`pyrogram.api.types.MessageMediaGeoLive`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x8b68b0cc

    def __init__(self, message, entities=None):
        self.message = message  # string
        self.entities = entities  # flags.3?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args) -> "GetWebPagePreview":
        flags = Int.read(b)
        
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 3) else []
        
        return GetWebPagePreview(message, entities)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.entities is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        return b.getvalue()
