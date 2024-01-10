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


class PagePart(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x8e3f9ebe``

    Args:
        blocks: List of :class:`pyrogram.api.types.PageBlock`
        photos: List of :class:`pyrogram.api.types.Photo`
        documents: List of :class:`pyrogram.api.types.Document`
    """
    ID = 0x8e3f9ebe

    def __init__(self, blocks, photos, documents):
        self.blocks = blocks  # Vector<PageBlock>
        self.photos = photos  # Vector<Photo>
        self.documents = documents  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args) -> "PagePart":
        # No flags
        
        blocks = Object.read(b)
        
        photos = Object.read(b)
        
        documents = Object.read(b)
        
        return PagePart(blocks, photos, documents)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.blocks))
        
        b.write(Vector(self.photos))
        
        b.write(Vector(self.documents))
        
        return b.getvalue()
