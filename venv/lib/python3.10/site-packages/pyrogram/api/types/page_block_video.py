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


class PageBlockVideo(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xd9d71866``

    Args:
        video_id: :obj:`int`
        caption: :class:`pyrogram.api.types.RichText`
        autoplay: :obj:`bool` (optional)
        loop: :obj:`bool` (optional)
    """
    ID = 0xd9d71866

    def __init__(self, video_id, caption, autoplay=None, loop=None):
        self.autoplay = autoplay  # flags.0?true
        self.loop = loop  # flags.1?true
        self.video_id = video_id  # long
        self.caption = caption  # RichText

    @staticmethod
    def read(b: BytesIO, *args) -> "PageBlockVideo":
        flags = Int.read(b)
        
        autoplay = True if flags & (1 << 0) else False
        loop = True if flags & (1 << 1) else False
        video_id = Long.read(b)
        
        caption = Object.read(b)
        
        return PageBlockVideo(video_id, caption, autoplay, loop)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.autoplay is not None else 0
        flags |= (1 << 1) if self.loop is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.video_id))
        
        b.write(self.caption.write())
        
        return b.getvalue()
