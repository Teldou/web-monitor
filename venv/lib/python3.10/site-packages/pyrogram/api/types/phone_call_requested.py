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


class PhoneCallRequested(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x83761ce4``

    Args:
        id: :obj:`int`
        access_hash: :obj:`int`
        date: :obj:`int`
        admin_id: :obj:`int`
        participant_id: :obj:`int`
        g_a_hash: :obj:`bytes`
        protocol: :class:`pyrogram.api.types.PhoneCallProtocol`
    """
    ID = 0x83761ce4

    def __init__(self, id, access_hash, date, admin_id, participant_id, g_a_hash, protocol):
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # int
        self.participant_id = participant_id  # int
        self.g_a_hash = g_a_hash  # bytes
        self.protocol = protocol  # PhoneCallProtocol

    @staticmethod
    def read(b: BytesIO, *args) -> "PhoneCallRequested":
        # No flags
        
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Int.read(b)
        
        participant_id = Int.read(b)
        
        g_a_hash = Bytes.read(b)
        
        protocol = Object.read(b)
        
        return PhoneCallRequested(id, access_hash, date, admin_id, participant_id, g_a_hash, protocol)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Int(self.admin_id))
        
        b.write(Int(self.participant_id))
        
        b.write(Bytes(self.g_a_hash))
        
        b.write(self.protocol.write())
        
        return b.getvalue()
