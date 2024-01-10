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


class UpdateUserTyping(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x5c486927``

    Args:
        user_id: :obj:`int`
        action: :class:`pyrogram.api.types.SendMessageAction`
    """
    ID = 0x5c486927

    def __init__(self, user_id, action):
        self.user_id = user_id  # int
        self.action = action  # SendMessageAction

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateUserTyping":
        # No flags
        
        user_id = Int.read(b)
        
        action = Object.read(b)
        
        return UpdateUserTyping(user_id, action)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.user_id))
        
        b.write(self.action.write())
        
        return b.getvalue()
