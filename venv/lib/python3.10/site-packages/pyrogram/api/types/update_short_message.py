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


class UpdateShortMessage(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x914fbf11``

    Args:
        id: :obj:`int`
        user_id: :obj:`int`
        message: :obj:`string`
        pts: :obj:`int`
        pts_count: :obj:`int`
        date: :obj:`int`
        out: :obj:`bool` (optional)
        mentioned: :obj:`bool` (optional)
        media_unread: :obj:`bool` (optional)
        silent: :obj:`bool` (optional)
        fwd_from: :class:`pyrogram.api.types.MessageFwdHeader` (optional)
        via_bot_id: :obj:`int` (optional)
        reply_to_msg_id: :obj:`int` (optional)
        entities: List of :class:`pyrogram.api.types.MessageEntity` (optional)
    """
    ID = 0x914fbf11

    def __init__(self, id, user_id, message, pts, pts_count, date, out=None, mentioned=None, media_unread=None, silent=None, fwd_from=None, via_bot_id=None, reply_to_msg_id=None, entities=None):
        self.out = out  # flags.1?true
        self.mentioned = mentioned  # flags.4?true
        self.media_unread = media_unread  # flags.5?true
        self.silent = silent  # flags.13?true
        self.id = id  # int
        self.user_id = user_id  # int
        self.message = message  # string
        self.pts = pts  # int
        self.pts_count = pts_count  # int
        self.date = date  # int
        self.fwd_from = fwd_from  # flags.2?MessageFwdHeader
        self.via_bot_id = via_bot_id  # flags.11?int
        self.reply_to_msg_id = reply_to_msg_id  # flags.3?int
        self.entities = entities  # flags.7?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateShortMessage":
        flags = Int.read(b)
        
        out = True if flags & (1 << 1) else False
        mentioned = True if flags & (1 << 4) else False
        media_unread = True if flags & (1 << 5) else False
        silent = True if flags & (1 << 13) else False
        id = Int.read(b)
        
        user_id = Int.read(b)
        
        message = String.read(b)
        
        pts = Int.read(b)
        
        pts_count = Int.read(b)
        
        date = Int.read(b)
        
        fwd_from = Object.read(b) if flags & (1 << 2) else None
        
        via_bot_id = Int.read(b) if flags & (1 << 11) else None
        reply_to_msg_id = Int.read(b) if flags & (1 << 3) else None
        entities = Object.read(b) if flags & (1 << 7) else []
        
        return UpdateShortMessage(id, user_id, message, pts, pts_count, date, out, mentioned, media_unread, silent, fwd_from, via_bot_id, reply_to_msg_id, entities)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.out is not None else 0
        flags |= (1 << 4) if self.mentioned is not None else 0
        flags |= (1 << 5) if self.media_unread is not None else 0
        flags |= (1 << 13) if self.silent is not None else 0
        flags |= (1 << 2) if self.fwd_from is not None else 0
        flags |= (1 << 11) if self.via_bot_id is not None else 0
        flags |= (1 << 3) if self.reply_to_msg_id is not None else 0
        flags |= (1 << 7) if self.entities is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(Int(self.user_id))
        
        b.write(String(self.message))
        
        b.write(Int(self.pts))
        
        b.write(Int(self.pts_count))
        
        b.write(Int(self.date))
        
        if self.fwd_from is not None:
            b.write(self.fwd_from.write())
        
        if self.via_bot_id is not None:
            b.write(Int(self.via_bot_id))
        
        if self.reply_to_msg_id is not None:
            b.write(Int(self.reply_to_msg_id))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        return b.getvalue()
