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


class PageBlockSlideshow(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x130c8963``

    Args:
        items: List of :class:`pyrogram.api.types.PageBlock`
        caption: :class:`pyrogram.api.types.RichText`
    """
    ID = 0x130c8963

    def __init__(self, items, caption):
        self.items = items  # Vector<PageBlock>
        self.caption = caption  # RichText

    @staticmethod
    def read(b: BytesIO, *args) -> "PageBlockSlideshow":
        # No flags
        
        items = Object.read(b)
        
        caption = Object.read(b)
        
        return PageBlockSlideshow(items, caption)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.items))
        
        b.write(self.caption.write())
        
        return b.getvalue()
