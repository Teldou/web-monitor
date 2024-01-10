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


class SearchGifs(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xbf9a776b``

    Args:
        q: :obj:`string`
        offset: :obj:`int`

    Returns:
        :class:`pyrogram.api.types.messages.FoundGifs`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0xbf9a776b

    def __init__(self, q, offset):
        self.q = q  # string
        self.offset = offset  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "SearchGifs":
        # No flags
        
        q = String.read(b)
        
        offset = Int.read(b)
        
        return SearchGifs(q, offset)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.q))
        
        b.write(Int(self.offset))
        
        return b.getvalue()
