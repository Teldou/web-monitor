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


class ReceivedQueue(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x55a5bb66``

    Args:
        max_qts: :obj:`int`

    Returns:
        List of :obj:`int`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x55a5bb66

    def __init__(self, max_qts):
        self.max_qts = max_qts  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "ReceivedQueue":
        # No flags
        
        max_qts = Int.read(b)
        
        return ReceivedQueue(max_qts)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.max_qts))
        
        return b.getvalue()
