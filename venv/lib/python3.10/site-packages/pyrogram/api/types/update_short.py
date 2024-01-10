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


class UpdateShort(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x78d4dec1``

    Args:
        update: :class:`pyrogram.api.types.Update`
        date: :obj:`int`
    """
    ID = 0x78d4dec1

    def __init__(self, update, date):
        self.update = update  # Update
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateShort":
        # No flags
        
        update = Object.read(b)
        
        date = Int.read(b)
        
        return UpdateShort(update, date)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.update.write())
        
        b.write(Int(self.date))
        
        return b.getvalue()
