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


class Found(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xb3134d9d``

    Args:
        my_results: List of :class:`pyrogram.api.types.Peer`
        results: List of :class:`pyrogram.api.types.Peer`
        chats: List of :class:`pyrogram.api.types.Chat`
        users: List of :class:`pyrogram.api.types.User`
    """
    ID = 0xb3134d9d

    def __init__(self, my_results, results, chats, users):
        self.my_results = my_results  # Vector<Peer>
        self.results = results  # Vector<Peer>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args) -> "Found":
        # No flags
        
        my_results = Object.read(b)
        
        results = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return Found(my_results, results, chats, users)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.my_results))
        
        b.write(Vector(self.results))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
