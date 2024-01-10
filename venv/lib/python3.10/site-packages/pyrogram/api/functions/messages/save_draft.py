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


class SaveDraft(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xbc39e14b``

    Args:
        peer: :class:`pyrogram.api.types.InputPeer`
        message: :obj:`string`
        no_webpage: :obj:`bool` (optional)
        reply_to_msg_id: :obj:`int` (optional)
        entities: List of :class:`pyrogram.api.types.MessageEntity` (optional)

    Returns:
        :obj:`bool`

    Raises:
        :class:`pyrogram.Error`
    """
    ID = 0xbc39e14b

    def __init__(self, peer, message, no_webpage=None, reply_to_msg_id=None, entities=None):
        self.no_webpage = no_webpage  # flags.1?true
        self.reply_to_msg_id = reply_to_msg_id  # flags.0?int
        self.peer = peer  # InputPeer
        self.message = message  # string
        self.entities = entities  # flags.3?Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args) -> "SaveDraft":
        flags = Int.read(b)
        
        no_webpage = True if flags & (1 << 1) else False
        reply_to_msg_id = Int.read(b) if flags & (1 << 0) else None
        peer = Object.read(b)
        
        message = String.read(b)
        
        entities = Object.read(b) if flags & (1 << 3) else []
        
        return SaveDraft(peer, message, no_webpage, reply_to_msg_id, entities)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.no_webpage is not None else 0
        flags |= (1 << 0) if self.reply_to_msg_id is not None else 0
        flags |= (1 << 3) if self.entities is not None else 0
        b.write(Int(flags))
        
        if self.reply_to_msg_id is not None:
            b.write(Int(self.reply_to_msg_id))
        
        b.write(self.peer.write())
        
        b.write(String(self.message))
        
        if self.entities is not None:
            b.write(Vector(self.entities))
        
        return b.getvalue()
