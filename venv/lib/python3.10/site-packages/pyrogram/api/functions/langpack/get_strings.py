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


class GetStrings(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x2e1ee318``

    Args:
        lang_code: :obj:`string`
        keys: List of :obj:`string`

    Returns:
        List of :class:`pyrogram.api.types.LangPackString` | List of :class:`pyrogram.api.types.LangPackStringPluralized` | List of :class:`pyrogram.api.types.LangPackStringDeleted`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x2e1ee318

    def __init__(self, lang_code, keys):
        self.lang_code = lang_code  # string
        self.keys = keys  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args) -> "GetStrings":
        # No flags
        
        lang_code = String.read(b)
        
        keys = Object.read(b, String)
        
        return GetStrings(lang_code, keys)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_code))
        
        b.write(Vector(self.keys, String))
        
        return b.getvalue()
