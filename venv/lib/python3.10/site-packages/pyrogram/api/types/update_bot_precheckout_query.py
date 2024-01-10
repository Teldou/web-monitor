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


class UpdateBotPrecheckoutQuery(Object):
    """
    Attributes:
        ID (:obj:`int`): ``0x5d2f3aa9``

    Args:
        query_id: :obj:`int`
        user_id: :obj:`int`
        payload: :obj:`bytes`
        currency: :obj:`string`
        total_amount: :obj:`int`
        info: :class:`pyrogram.api.types.PaymentRequestedInfo` (optional)
        shipping_option_id: :obj:`string` (optional)
    """
    ID = 0x5d2f3aa9

    def __init__(self, query_id, user_id, payload, currency, total_amount, info=None, shipping_option_id=None):
        self.query_id = query_id  # long
        self.user_id = user_id  # int
        self.payload = payload  # bytes
        self.info = info  # flags.0?PaymentRequestedInfo
        self.shipping_option_id = shipping_option_id  # flags.1?string
        self.currency = currency  # string
        self.total_amount = total_amount  # long

    @staticmethod
    def read(b: BytesIO, *args) -> "UpdateBotPrecheckoutQuery":
        flags = Int.read(b)
        
        query_id = Long.read(b)
        
        user_id = Int.read(b)
        
        payload = Bytes.read(b)
        
        info = Object.read(b) if flags & (1 << 0) else None
        
        shipping_option_id = String.read(b) if flags & (1 << 1) else None
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        return UpdateBotPrecheckoutQuery(query_id, user_id, payload, currency, total_amount, info, shipping_option_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.info is not None else 0
        flags |= (1 << 1) if self.shipping_option_id is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.query_id))
        
        b.write(Int(self.user_id))
        
        b.write(Bytes(self.payload))
        
        if self.info is not None:
            b.write(self.info.write())
        
        if self.shipping_option_id is not None:
            b.write(String(self.shipping_option_id))
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        return b.getvalue()
