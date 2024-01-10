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


class EncryptedChatRequested(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xc878527e``

    Args:
        id: :obj:`int`
        access_hash: :obj:`int`
        date: :obj:`int`
        admin_id: :obj:`int`
        participant_id: :obj:`int`
        g_a: :obj:`bytes`
    """
    ID = 0xc878527e

    def __init__(self, id, access_hash, date, admin_id, participant_id, g_a):
        self.id = id  # int
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # int
        self.participant_id = participant_id  # int
        self.g_a = g_a  # bytes

    @staticmethod
    def read(b: BytesIO, *args) -> "EncryptedChatRequested":
        # No flags
        
        id = Int.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Int.read(b)
        
        participant_id = Int.read(b)
        
        g_a = Bytes.read(b)
        
        return EncryptedChatRequested(id, access_hash, date, admin_id, participant_id, g_a)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Int(self.admin_id))
        
        b.write(Int(self.participant_id))
        
        b.write(Bytes(self.g_a))
        
        return b.getvalue()
