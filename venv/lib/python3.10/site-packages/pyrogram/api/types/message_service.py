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


class MessageService(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x9e19a1f6``

    Args:
        id: :obj:`int`
        to_id: :class:`pyrogram.api.types.Peer`
        date: :obj:`int`
        action: :class:`pyrogram.api.types.MessageAction`
        out: :obj:`bool` (optional)
        mentioned: :obj:`bool` (optional)
        media_unread: :obj:`bool` (optional)
        silent: :obj:`bool` (optional)
        post: :obj:`bool` (optional)
        from_id: :obj:`int` (optional)
        reply_to_msg_id: :obj:`int` (optional)
    """
    ID = 0x9e19a1f6

    def __init__(self, id, to_id, date, action, out=None, mentioned=None, media_unread=None, silent=None, post=None, from_id=None, reply_to_msg_id=None):
        self.out = out  # flags.1?true
        self.mentioned = mentioned  # flags.4?true
        self.media_unread = media_unread  # flags.5?true
        self.silent = silent  # flags.13?true
        self.post = post  # flags.14?true
        self.id = id  # int
        self.from_id = from_id  # flags.8?int
        self.to_id = to_id  # Peer
        self.reply_to_msg_id = reply_to_msg_id  # flags.3?int
        self.date = date  # int
        self.action = action  # MessageAction

    @staticmethod
    def read(b: BytesIO, *args) -> "MessageService":
        flags = Int.read(b)
        
        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        silent = True if flags & (1 << 13) else False
        post = True if flags & (1 << 14) else False
        id = Int.read(b)
        
        from_id = Int.read(b) if flags & (1 << 8) else None
        to_id = Object.read(b)
        
        reply_to_msg_id = Int.read(b) if flags & (1 << 3) else None
        date = Int.read(b)
        
        action = Object.read(b)
        
        return MessageService(id, to_id, date, action, out, mentioned, media_unread, silent, post, from_id, reply_to_msg_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out is not None else 0
        flags |= (1 << 4) if self.mentioned is not None else 0
        flags |= (1 << 5) if self.media_unread is not None else 0
        flags |= (1 << 13) if self.silent is not None else 0
        flags |= (1 << 14) if self.post is not None else 0
        flags |= (1 << 8) if self.from_id is not None else 0
        flags |= (1 << 3) if self.reply_to_msg_id is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        if self.from_id is not None:
            b.write(Int(self.from_id))
        
        b.write(self.to_id.write())
        
        if self.reply_to_msg_id is not None:
            b.write(Int(self.reply_to_msg_id))
        
        b.write(Int(self.date))
        
        b.write(self.action.write())
        
        return b.getvalue()
