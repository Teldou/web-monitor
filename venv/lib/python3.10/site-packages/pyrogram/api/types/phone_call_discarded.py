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


class PhoneCallDiscarded(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x50ca4de1``

    Args:
        id: :obj:`int`
        need_rating: :obj:`bool` (optional)
        need_debug: :obj:`bool` (optional)
        reason: :class:`pyrogram.api.types.PhoneCallDiscardReason` (optional)
        duration: :obj:`int` (optional)
    """
    ID = 0x50ca4de1

    def __init__(self, id, need_rating=None, need_debug=None, reason=None, duration=None):
        self.need_rating = need_rating  # flags.2?true
        self.need_debug = need_debug  # flags.3?true
        self.id = id  # long
        self.reason = reason  # flags.0?PhoneCallDiscardReason
        self.duration = duration  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args) -> "PhoneCallDiscarded":
        flags = Int.read(b)
        
        need_rating = True if flags & (1 << 2) else False
        need_debug = True if flags & (1 << 3) else False
        id = Long.read(b)
        
        reason = Object.read(b) if flags & (1 << 0) else None
        
        duration = Int.read(b) if flags & (1 << 1) else None
        return PhoneCallDiscarded(id, need_rating, need_debug, reason, duration)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.need_rating is not None else 0
        flags |= (1 << 3) if self.need_debug is not None else 0
        flags |= (1 << 0) if self.reason is not None else 0
        flags |= (1 << 1) if self.duration is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.id))
        
        if self.reason is not None:
            b.write(self.reason.write())
        
        if self.duration is not None:
            b.write(Int(self.duration))
        
        return b.getvalue()
