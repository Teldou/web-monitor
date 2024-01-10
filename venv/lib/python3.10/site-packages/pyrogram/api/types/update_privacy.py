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


class UpdatePrivacy(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0xee3b272a``

    Args:
        key: :class:`pyrogram.api.types.PrivacyKey`
        rules: List of :class:`pyrogram.api.types.PrivacyRule`
    """
    ID = 0xee3b272a

    def __init__(self, key, rules):
        self.key = key  # PrivacyKey
        self.rules = rules  # Vector<PrivacyRule>

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdatePrivacy":
        # No flags
        
        key = Object.read(b)
        
        rules = Object.read(b)
        
        return UpdatePrivacy(key, rules)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.key.write())
        
        b.write(Vector(self.rules))
        
        return b.getvalue()
