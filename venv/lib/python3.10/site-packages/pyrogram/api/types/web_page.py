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


class WebPage(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x5f07b4bc``

    Args:
        id: :obj:`int`
        url: :obj:`string`
        display_url: :obj:`string`
        hash: :obj:`int`
        type: :obj:`string` (optional)
        site_name: :obj:`string` (optional)
        title: :obj:`string` (optional)
        description: :obj:`string` (optional)
        photo: :class:`pyrogram.api.types.Photo` (optional)
        embed_url: :obj:`string` (optional)
        embed_type: :obj:`string` (optional)
        embed_width: :obj:`int` (optional)
        embed_height: :obj:`int` (optional)
        duration: :obj:`int` (optional)
        author: :obj:`string` (optional)
        document: :class:`pyrogram.api.types.Document` (optional)
        cached_page: :class:`pyrogram.api.types.Page` (optional)
    """
    ID = 0x5f07b4bc

    def __init__(self, id, url, display_url, hash, type=None, site_name=None, title=None, description=None, photo=None, embed_url=None, embed_type=None, embed_width=None, embed_height=None, duration=None, author=None, document=None, cached_page=None):
        self.id = id  # long
        self.url = url  # string
        self.display_url = display_url  # string
        self.hash = hash  # int
        self.type = type  # flags.0?string
        self.site_name = site_name  # flags.1?string
        self.title = title  # flags.2?string
        self.description = description  # flags.3?string
        self.photo = photo  # flags.4?Photo
        self.embed_url = embed_url  # flags.5?string
        self.embed_type = embed_type  # flags.5?string
        self.embed_width = embed_width  # flags.6?int
        self.embed_height = embed_height  # flags.6?int
        self.duration = duration  # flags.7?int
        self.author = author  # flags.8?string
        self.document = document  # flags.9?Document
        self.cached_page = cached_page  # flags.10?Page

    @staticmethod
    def read(b: BytesIO, *args) -> "WebPage":
        flags = Int.read(b)
        
        id = Long.read(b)
        
        url = String.read(b)
        
        display_url = String.read(b)
        
        hash = Int.read(b)
        
        type = String.read(b) if flags & (1 << 0) else None
        site_name = String.read(b) if flags & (1 << 1) else None
        title = String.read(b) if flags & (1 << 2) else None
        description = String.read(b) if flags & (1 << 3) else None
        photo = Object.read(b) if flags & (1 << 4) else None
        
        embed_url = String.read(b) if flags & (1 << 5) else None
        embed_type = String.read(b) if flags & (1 << 5) else None
        embed_width = Int.read(b) if flags & (1 << 6) else None
        embed_height = Int.read(b) if flags & (1 << 6) else None
        duration = Int.read(b) if flags & (1 << 7) else None
        author = String.read(b) if flags & (1 << 8) else None
        document = Object.read(b) if flags & (1 << 9) else None
        
        cached_page = Object.read(b) if flags & (1 << 10) else None
        
        return WebPage(id, url, display_url, hash, type, site_name, title, description, photo, embed_url, embed_type, embed_width, embed_height, duration, author, document, cached_page)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.type is not None else 0
        flags |= (1 << 1) if self.site_name is not None else 0
        flags |= (1 << 2) if self.title is not None else 0
        flags |= (1 << 3) if self.description is not None else 0
        flags |= (1 << 4) if self.photo is not None else 0
        flags |= (1 << 5) if self.embed_url is not None else 0
        flags |= (1 << 5) if self.embed_type is not None else 0
        flags |= (1 << 6) if self.embed_width is not None else 0
        flags |= (1 << 6) if self.embed_height is not None else 0
        flags |= (1 << 7) if self.duration is not None else 0
        flags |= (1 << 8) if self.author is not None else 0
        flags |= (1 << 9) if self.document is not None else 0
        flags |= (1 << 10) if self.cached_page is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        b.write(String(self.url))
        
        b.write(String(self.display_url))
        
        b.write(Int(self.hash))
        
        if self.type is not None:
            b.write(String(self.type))
        
        if self.site_name is not None:
            b.write(String(self.site_name))
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.embed_url is not None:
            b.write(String(self.embed_url))
        
        if self.embed_type is not None:
            b.write(String(self.embed_type))
        
        if self.embed_width is not None:
            b.write(Int(self.embed_width))
        
        if self.embed_height is not None:
            b.write(Int(self.embed_height))
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        if self.author is not None:
            b.write(String(self.author))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.cached_page is not None:
            b.write(self.cached_page.write())
        
        return b.getvalue()
