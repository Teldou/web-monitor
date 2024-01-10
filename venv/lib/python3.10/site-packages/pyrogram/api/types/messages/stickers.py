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


class Stickers(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x8a8ecd32``

    Args:
        hash: :obj:`string`
        stickers: List of :class:`pyrogram.api.types.Document`
    """
    ID = 0x8a8ecd32

    def __init__(self, hash, stickers):
        self.hash = hash  # string
        self.stickers = stickers  # Vector<Document>

    @staticmethod
    def read(b: BytesIO, *args) -> "Stickers":
        # No flags
        
        hash = String.read(b)
        
        stickers = Object.read(b)
        
        return Stickers(hash, stickers)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.hash))
        
        b.write(Vector(self.stickers))
        
        return b.getvalue()
