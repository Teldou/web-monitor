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


class PageBlockList(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x3a58c7f4``

    Args:
        ordered: :obj:`bool`
        items: List of :class:`pyrogram.api.types.RichText`
    """
    ID = 0x3a58c7f4

    def __init__(self, ordered, items):
        self.ordered = ordered  # Bool
        self.items = items  # Vector<RichText>

    @staticmethod
    def read(b: BytesIO, *args) -> "PageBlockList":
        # No flags
        
        ordered = Bool.read(b)
        
        items = Object.read(b)
        
        return PageBlockList(ordered, items)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bool(self.ordered))
        
        b.write(Vector(self.items))
        
        return b.getvalue()
