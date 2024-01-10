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


class GetDocumentByHash(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x338e2464``

    Args:
        sha256: :obj:`bytes`
        size: :obj:`int`
        mime_type: :obj:`string`

    Returns:
        :class:`pyrogram.api.types.DocumentEmpty` | :class:`pyrogram.api.types.Document`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x338e2464

    def __init__(self, sha256, size, mime_type):
        self.sha256 = sha256  # bytes
        self.size = size  # int
        self.mime_type = mime_type  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "GetDocumentByHash":
        # No flags
        
        sha256 = Bytes.read(b)
        
        size = Int.read(b)
        
        mime_type = String.read(b)
        
        return GetDocumentByHash(sha256, size, mime_type)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.sha256))
        
        b.write(Int(self.size))
        
        b.write(String(self.mime_type))
        
        return b.getvalue()
