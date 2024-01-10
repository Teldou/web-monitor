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


class PageBlockEmbedPost(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x292c7be9``

    Args:
        url: :obj:`string`
        webpage_id: :obj:`int`
        author_photo_id: :obj:`int`
        author: :obj:`string`
        date: :obj:`int`
        blocks: List of :class:`pyrogram.api.types.PageBlock`
        caption: :class:`pyrogram.api.types.RichText`
    """
    ID = 0x292c7be9

    def __init__(self, url, webpage_id, author_photo_id, author, date, blocks, caption):
        self.url = url  # string
        self.webpage_id = webpage_id  # long
        self.author_photo_id = author_photo_id  # long
        self.author = author  # string
        self.date = date  # int
        self.blocks = blocks  # Vector<PageBlock>
        self.caption = caption  # RichText

    @staticmethod
    def read(b: BytesIO, *args) -> "PageBlockEmbedPost":
        # No flags
        
        url = String.read(b)
        
        webpage_id = Long.read(b)
        
        author_photo_id = Long.read(b)
        
        author = String.read(b)
        
        date = Int.read(b)
        
        blocks = Object.read(b)
        
        caption = Object.read(b)
        
        return PageBlockEmbedPost(url, webpage_id, author_photo_id, author, date, blocks, caption)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.url))
        
        b.write(Long(self.webpage_id))
        
        b.write(Long(self.author_photo_id))
        
        b.write(String(self.author))
        
        b.write(Int(self.date))
        
        b.write(Vector(self.blocks))
        
        b.write(self.caption.write())
        
        return b.getvalue()
