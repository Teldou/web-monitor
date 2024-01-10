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


class GetDifference(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x25939651``

    Args:
        pts: :obj:`int`
        date: :obj:`int`
        qts: :obj:`int`
        pts_total_limit: :obj:`int` (optional)

    Returns:
        :class:`pyrogram.api.types.updates.DifferenceEmpty` | :class:`pyrogram.api.types.updates.Difference` | :class:`pyrogram.api.types.updates.DifferenceSlice` | :class:`pyrogram.api.types.updates.DifferenceTooLong`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0x25939651

    def __init__(self, pts, date, qts, pts_total_limit=None):
        self.pts = pts  # int
        self.pts_total_limit = pts_total_limit  # flags.0?int
        self.date = date  # int
        self.qts = qts  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetDifference":
        flags = Int.read(b)
        
        pts = Int.read(b)
        
        pts_total_limit = Int.read(b) if flags & (1 << 0) else None
        date = Int.read(b)
        
        qts = Int.read(b)
        
        return GetDifference(pts, date, qts, pts_total_limit)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.pts_total_limit is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.pts))
        
        if self.pts_total_limit is not None:
            b.write(Int(self.pts_total_limit))
        
        b.write(Int(self.date))
        
        b.write(Int(self.qts))
        
        return b.getvalue()
