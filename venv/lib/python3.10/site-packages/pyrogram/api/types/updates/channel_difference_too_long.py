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


class ChannelDifferenceTooLong(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x6a9d7b35``

    Args:
        pts: :obj:`int`
        top_message: :obj:`int`
        read_inbox_max_id: :obj:`int`
        read_outbox_max_id: :obj:`int`
        unread_count: :obj:`int`
        unread_mentions_count: :obj:`int`
        messages: List of :class:`pyrogram.api.types.Message`
        chats: List of :class:`pyrogram.api.types.Chat`
        users: List of :class:`pyrogram.api.types.User`
        final: :obj:`bool` (optional)
        timeout: :obj:`int` (optional)
    """
    ID = 0x6a9d7b35

    def __init__(self, pts, top_message, read_inbox_max_id, read_outbox_max_id, unread_count, unread_mentions_count, messages, chats, users, final=None, timeout=None):
        self.final = final  # flags.0?true
        self.pts = pts  # int
        self.timeout = timeout  # flags.1?int
        self.top_message = top_message  # int
        self.read_inbox_max_id = read_inbox_max_id  # int
        self.read_outbox_max_id = read_outbox_max_id  # int
        self.unread_count = unread_count  # int
        self.unread_mentions_count = unread_mentions_count  # int
        self.messages = messages  # Vector<Message>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelDifferenceTooLong":
        flags = Int.read(b)
        
        final = True if flags & (1 << 0) else False
        pts = Int.read(b)
        
        timeout = Int.read(b) if flags & (1 << 1) else None
        top_message = Int.read(b)
        
        read_inbox_max_id = Int.read(b)
        
        read_outbox_max_id = Int.read(b)
        
        unread_count = Int.read(b)
        
        unread_mentions_count = Int.read(b)
        
        messages = Object.read(b)
        
        chats = Object.read(b)
        
        users = Object.read(b)
        
        return ChannelDifferenceTooLong(pts, top_message, read_inbox_max_id, read_outbox_max_id, unread_count, unread_mentions_count, messages, chats, users, final, timeout)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.final is not None else 0
        flags |= (1 << 1) if self.timeout is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.pts))
        
        if self.timeout is not None:
            b.write(Int(self.timeout))
        
        b.write(Int(self.top_message))
        
        b.write(Int(self.read_inbox_max_id))
        
        b.write(Int(self.read_outbox_max_id))
        
        b.write(Int(self.unread_count))
        
        b.write(Int(self.unread_mentions_count))
        
        b.write(Vector(self.messages))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
