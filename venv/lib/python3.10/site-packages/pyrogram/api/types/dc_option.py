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


class DcOption(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x05d8c6cc``

    Args:
        id: :obj:`int`
        ip_address: :obj:`string`
        port: :obj:`int`
        ipv6: :obj:`bool` (optional)
        media_only: :obj:`bool` (optional)
        tcpo_only: :obj:`bool` (optional)
        cdn: :obj:`bool` (optional)
        static: :obj:`bool` (optional)
    """
    ID = 0x05d8c6cc

    def __init__(self, id, ip_address, port, ipv6=None, media_only=None, tcpo_only=None, cdn=None, static=None):
        self.ipv6 = ipv6  # flags.0?true
        self.media_only = media_only  # flags.1?true
        self.tcpo_only = tcpo_only  # flags.2?true
        self.cdn = cdn  # flags.3?true
        self.static = static  # flags.4?true
        self.id = id  # int
        self.ip_address = ip_address  # string
        self.port = port  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "DcOption":
        flags = Int.read(b)
        
        ipv6 = True if flags & (1 << 0) else False
        media_only = True if flags & (1 << 1) else False
        tcpo_only = True if flags & (1 << 2) else False
        cdn = True if flags & (1 << 3) else False
        static = True if flags & (1 << 4) else False
        id = Int.read(b)
        
        ip_address = String.read(b)
        
        port = Int.read(b)
        
        return DcOption(id, ip_address, port, ipv6, media_only, tcpo_only, cdn, static)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.ipv6 is not None else 0
        flags |= (1 << 1) if self.media_only is not None else 0
        flags |= (1 << 2) if self.tcpo_only is not None else 0
        flags |= (1 << 3) if self.cdn is not None else 0
        flags |= (1 << 4) if self.static is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.ip_address))
        
        b.write(Int(self.port))
        
        return b.getvalue()
