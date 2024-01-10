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


class ChannelAdminLogEvent(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x3b5a3e40``

    Args:
        id: :obj:`int`
        date: :obj:`int`
        user_id: :obj:`int`
        action: :class:`pyrogram.api.types.ChannelAdminLogEventAction`
    """
    ID = 0x3b5a3e40

    def __init__(self, id, date, user_id, action):
        self.id = id  # long
        self.date = date  # int
        self.user_id = user_id  # int
        self.action = action  # ChannelAdminLogEventAction

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelAdminLogEvent":
        # No flags
        
        id = Long.read(b)
        
        date = Int.read(b)
        
        user_id = Int.read(b)
        
        action = Object.read(b)
        
        return ChannelAdminLogEvent(id, date, user_id, action)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Int(self.date))
        
        b.write(Int(self.user_id))
        
        b.write(self.action.write())
        
        return b.getvalue()
