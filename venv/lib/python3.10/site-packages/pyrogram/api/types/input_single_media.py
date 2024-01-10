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


class InputSingleMedia(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x1cc6e91f``

    Args:
        media: :class:`pyrogram.api.types.InputMedia`
        random_id: :obj:`int`
        message: :obj:`string`
        entities: List of :class:`pyrogram.api.types.MessageEntity` (optional)
    """
    ID = 0x1cc6e91f

    def __init__(self, media, random_id, message, entities=None):
        self.media = media  # InputMedia
        self.random_id = random_id  # long
        self.message = message  # string
        self.entities = entities  # flags.0?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args) -> "InputSingleMedia":
        flags = Int.read(b)
        
        media = Object.read(b)
        
        random_id = Long.read(b)
        
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 0) else []
        
        return InputSingleMedia(media, random_id, message, entities)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.entities is not None else 0
        b.write(Int(flags))
        
        b.write(self.media.write())
        
        b.write(Long(self.random_id))
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        return b.getvalue()
