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


class GetBlocked(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xf57c350f``

    Args:
        offset: :obj:`int`
        limit: :obj:`int`

    Returns:
        :class:`pyrogram.api.types.contacts.Blocked` | :class:`pyrogram.api.types.contacts.BlockedSlice`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0xf57c350f

    def __init__(self, offset, limit):
        self.offset = offset  # int
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetBlocked":
        # No flags
        
        offset = Int.read(b)
        
        limit = Int.read(b)
        
        return GetBlocked(offset, limit)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.offset))
        
        b.write(Int(self.limit))
        
        return b.getvalue()
