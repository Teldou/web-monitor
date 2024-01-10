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


class SentEncryptedFile(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x9493ff32``

    Args:
        date: :obj:`int`
        file: :class:`pyrogram.api.types.EncryptedFile`
    """
    ID = 0x9493ff32

    def __init__(self, date, file):
        self.date = date  # int
        self.file = file  # EncryptedFile

    @staticmethod
    def read(b: BytesIO, *args) -> "SentEncryptedFile":
        # No flags
        
        date = Int.read(b)
        
        file = Object.read(b)
        
        return SentEncryptedFile(date, file)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.date))
        
        b.write(self.file.write())
        
        return b.getvalue()
