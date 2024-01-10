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


class ChannelAdminLogEventsFilter(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xea107ae4``

    Args:
        join: :obj:`bool` (optional)
        leave: :obj:`bool` (optional)
        invite: :obj:`bool` (optional)
        ban: :obj:`bool` (optional)
        unban: :obj:`bool` (optional)
        kick: :obj:`bool` (optional)
        unkick: :obj:`bool` (optional)
        promote: :obj:`bool` (optional)
        demote: :obj:`bool` (optional)
        info: :obj:`bool` (optional)
        settings: :obj:`bool` (optional)
        pinned: :obj:`bool` (optional)
        edit: :obj:`bool` (optional)
        delete: :obj:`bool` (optional)
    """
    ID = 0xea107ae4

    def __init__(self, join=None, leave=None, invite=None, ban=None, unban=None, kick=None, unkick=None, promote=None, demote=None, info=None, settings=None, pinned=None, edit=None, delete=None):
        self.join = join  # flags.0?true
        self.leave = leave  # flags.1?true
        self.invite = invite  # flags.2?true
        self.ban = ban  # flags.3?true
        self.unban = unban  # flags.4?true
        self.kick = kick  # flags.5?true
        self.unkick = unkick  # flags.6?true
        self.promote = promote  # flags.7?true
        self.demote = demote  # flags.8?true
        self.info = info  # flags.9?true
        self.settings = settings  # flags.10?true
        self.pinned = pinned  # flags.11?true
        self.edit = edit  # flags.12?true
        self.delete = delete  # flags.13?true

    @staticmethod
    def read(b: BytesIO, *args) -> "ChannelAdminLogEventsFilter":
        flags = Int.read(b)
        
        join = True if flags & (1 << 0) else False
        leave = True if flags & (1 << 1) else False
        invite = True if flags & (1 << 2) else False
        ban = True if flags & (1 << 3) else False
        unban = True if flags & (1 << 4) else False
        kick = True if flags & (1 << 5) else False
        unkick = True if flags & (1 << 6) else False
        promote = True if flags & (1 << 7) else False
        demote = True if flags & (1 << 8) else False
        info = True if flags & (1 << 9) else False
        settings = True if flags & (1 << 10) else False
        pinned = True if flags & (1 << 11) else False
        edit = True if flags & (1 << 12) else False
        delete = True if flags & (1 << 13) else False
        return ChannelAdminLogEventsFilter(join, leave, invite, ban, unban, kick, unkick, promote, demote, info, settings, pinned, edit, delete)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.join is not None else 0
        flags |= (1 << 1) if self.leave is not None else 0
        flags |= (1 << 2) if self.invite is not None else 0
        flags |= (1 << 3) if self.ban is not None else 0
        flags |= (1 << 4) if self.unban is not None else 0
        flags |= (1 << 5) if self.kick is not None else 0
        flags |= (1 << 6) if self.unkick is not None else 0
        flags |= (1 << 7) if self.promote is not None else 0
        flags |= (1 << 8) if self.demote is not None else 0
        flags |= (1 << 9) if self.info is not None else 0
        flags |= (1 << 10) if self.settings is not None else 0
        flags |= (1 << 11) if self.pinned is not None else 0
        flags |= (1 << 12) if self.edit is not None else 0
        flags |= (1 << 13) if self.delete is not None else 0
        b.write(Int(flags))
        
        return b.getvalue()
