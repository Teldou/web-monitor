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


class StickerSet(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xb60a24a6``

    Args:
        set: :class:`pyrogram.api.types.StickerSet`
        packs: List of :class:`pyrogram.api.types.StickerPack`
        documents: List of :class:`pyrogram.api.types.Document`
    """
    ID = 0xb60a24a6

    def __init__(self, set, packs, documents):
        self.set = set  # StickerSet
        self.packs = packs  # Vector<StickerPack>
        self.documents = documents  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args) -> "StickerSet":
        # No flags
        
        set = Object.read(b)
        
        packs = Object.read(b)
        
        documents = Object.read(b)
        
        return StickerSet(set, packs, documents)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.set.write())
        
        b.write(Vector(self.packs))
        
        b.write(Vector(self.documents))
        
        return b.getvalue()
