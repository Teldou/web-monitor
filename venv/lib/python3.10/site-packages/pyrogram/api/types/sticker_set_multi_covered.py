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


class StickerSetMultiCovered(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x3407e51b``

    Args:
        set: :class:`pyrogram.api.types.StickerSet`
        covers: List of :class:`pyrogram.api.types.Document`
    """
    ID = 0x3407e51b

    def __init__(self, set, covers):
        self.set = set  # StickerSet
        self.covers = covers  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args) -> "StickerSetMultiCovered":
        # No flags
        
        set = Object.read(b)
        
        covers = Object.read(b)
        
        return StickerSetMultiCovered(set, covers)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.set.write())
        
        b.write(Vector(self.covers))
        
        return b.getvalue()
