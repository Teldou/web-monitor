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


class PageBlockPhoto(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xe9c69982``

    Args:
        photo_id: :obj:`int`
        caption: :class:`pyrogram.api.types.RichText`
    """
    ID = 0xe9c69982

    def __init__(self, photo_id, caption):
        self.photo_id = photo_id  # long
        self.caption = caption  # RichText

    @staticmethod
    def read(b: BytesIO, *args) -> "PageBlockPhoto":
        # No flags
        
        photo_id = Long.read(b)
        
        caption = Object.read(b)
        
        return PageBlockPhoto(photo_id, caption)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.photo_id))
        
        b.write(self.caption.write())
        
        return b.getvalue()
