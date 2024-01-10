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


class PageBlockPreformatted(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xc070d93e``

    Args:
        text: :class:`pyrogram.api.types.RichText`
        language: :obj:`string`
    """
    ID = 0xc070d93e

    def __init__(self, text, language):
        self.text = text  # RichText
        self.language = language  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "PageBlockPreformatted":
        # No flags
        
        text = Object.read(b)
        
        language = String.read(b)
        
        return PageBlockPreformatted(text, language)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.text.write())
        
        b.write(String(self.language))
        
        return b.getvalue()
