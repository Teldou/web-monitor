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


class DifferenceSlice(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xa8fb1981``

    Args:
        new_messages: List of :class:`pyrogram.api.types.Message`
        new_encrypted_messages: List of :class:`pyrogram.api.types.EncryptedMessage`
        other_updates: List of :class:`pyrogram.api.types.Update`
        chats: List of :class:`pyrogram.api.types.Chat`
        users: List of :class:`pyrogram.api.types.User`
        intermediate_state: :class:`pyrogram.api.types.updates.State`
    """
    ID = 0xa8fb1981

    def __init__(self, new_messages, new_encrypted_messages, other_updates, chats, users, intermediate_state):
        self.new_messages = new_messages  # Vector<Message>
        self.new_encrypted_messages = new_encrypted_messages  # Vector<EncryptedMessage>
        self.other_updates = other_updates  # Vector<Update>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.intermediate_state = intermediate_state  # updates.State

    @staticmethod
    def read(b: BytesIO, *args) -> "DifferenceSlice":
        # No flags
        
        new_messages = Object.read(b)
        
        new_encrypted_messages = Object.read(b)
        
        other_updates = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        intermediate_state = Object.read(b)
        
        return DifferenceSlice(new_messages, new_encrypted_messages, other_updates, chats, users, intermediate_state)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.new_messages))
        
        b.write(Vector(self.new_encrypted_messages))
        
        b.write(Vector(self.other_updates))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        b.write(self.intermediate_state.write())
        
        return b.getvalue()
