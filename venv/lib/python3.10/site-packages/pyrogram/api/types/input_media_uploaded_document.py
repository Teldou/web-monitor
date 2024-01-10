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


class InputMediaUploadedDocument(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x5b38c6c1``

    Args:
        file: :class:`pyrogram.api.types.InputFile`
        mime_type: :obj:`string`
        attributes: List of :class:`pyrogram.api.types.DocumentAttribute`
        nosound_video: :obj:`bool` (optional)
        thumb: :class:`pyrogram.api.types.InputFile` (optional)
        stickers: List of :class:`pyrogram.api.types.InputDocument` (optional)
        ttl_seconds: :obj:`int` (optional)
    """
    ID = 0x5b38c6c1

    def __init__(self, file, mime_type, attributes, nosound_video=None, thumb=None, stickers=None, ttl_seconds=None):
        self.nosound_video = nosound_video  # flags.3?true
        self.file = file  # InputFile
        self.thumb = thumb  # flags.2?InputFile
        self.mime_type = mime_type  # string
        self.attributes = attributes  # Vector<DocumentAttribute>
        self.stickers = stickers  # flags.0?Vector<InputDocument>
        self.ttl_seconds = ttl_seconds  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args) -> "InputMediaUploadedDocument":
        flags = Int.read(b)
        
        nosound_video = True if flags & (1 << 3) else False
        file = Object.read(b)
        
        thumb = Object.read(b) if flags & (1 << 2) else None
        
        mime_type = String.read(b)
        
        attributes = Object.read(b)
        
        stickers = Object.read(b) if flags & (1 << 0) else []
        
        ttl_seconds = Int.read(b) if flags & (1 << 1) else None
        return InputMediaUploadedDocument(file, mime_type, attributes, nosound_video, thumb, stickers, ttl_seconds)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.nosound_video is not None else 0
        flags |= (1 << 2) if self.thumb is not None else 0
        flags |= (1 << 0) if self.stickers is not None else 0
        flags |= (1 << 1) if self.ttl_seconds is not None else 0
        b.write(Int(flags))
        
        b.write(self.file.write())
        
        if self.thumb is not None:
            b.write(self.thumb.write())
        
        b.write(String(self.mime_type))
        
        b.write(Vector(self.attributes))
        
        if self.stickers is not None:
            b.write(Vector(self.stickers))
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        return b.getvalue()
