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


class PageBlockEmbed(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xcde200d1``

    Args:
        w: :obj:`int`
        h: :obj:`int`
        caption: :class:`pyrogram.api.types.RichText`
        full_width: :obj:`bool` (optional)
        allow_scrolling: :obj:`bool` (optional)
        url: :obj:`string` (optional)
        html: :obj:`string` (optional)
        poster_photo_id: :obj:`int` (optional)
    """
    ID = 0xcde200d1

    def __init__(self, w, h, caption, full_width=None, allow_scrolling=None, url=None, html=None, poster_photo_id=None):
        self.full_width = full_width  # flags.0?true
        self.allow_scrolling = allow_scrolling  # flags.3?true
        self.url = url  # flags.1?string
        self.html = html  # flags.2?string
        self.poster_photo_id = poster_photo_id  # flags.4?long
        self.w = w  # int
        self.h = h  # int
        self.caption = caption  # RichText

    @staticmethod
    def read(b: BytesIO, *args) -> "PageBlockEmbed":
        flags = Int.read(b)
        
        full_width = True if flags & (1 << 0) else False
        allow_scrolling = True if flags & (1 << 3) else False
        url = String.read(b) if flags & (1 << 1) else None
        html = String.read(b) if flags & (1 << 2) else None
        poster_photo_id = Long.read(b) if flags & (1 << 4) else None
        w = Int.read(b)
        
        h = Int.read(b)
        
        caption = Object.read(b)
        
        return PageBlockEmbed(w, h, caption, full_width, allow_scrolling, url, html, poster_photo_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.full_width is not None else 0
        flags |= (1 << 3) if self.allow_scrolling is not None else 0
        flags |= (1 << 1) if self.url is not None else 0
        flags |= (1 << 2) if self.html is not None else 0
        flags |= (1 << 4) if self.poster_photo_id is not None else 0
        b.write(Int(flags))
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.html is not None:
            b.write(String(self.html))
        
        if self.poster_photo_id is not None:
            b.write(Long(self.poster_photo_id))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        b.write(self.caption.write())
        
        return b.getvalue()
