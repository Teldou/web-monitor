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

count = 64

exceptions = {
    303: {
        "FILE_MIGRATE_X": "FileMigrate",
        "PHONE_MIGRATE_X": "PhoneMigrate",
        "NETWORK_MIGRATE_X": "NetworkMigrate",
        "USER_MIGRATE_X": "UserMigrate",
    },
    400: {
        "FIRSTNAME_INVALID": "FirstnameInvalid",
        "LASTNAME_INVALID": "LastnameInvalid",
        "PHONE_NUMBER_INVALID": "PhoneNumberInvalid",
        "PHONE_CODE_HASH_EMPTY": "PhoneCodeHashEmpty",
        "PHONE_CODE_EMPTY": "PhoneCodeEmpty",
        "PHONE_CODE_EXPIRED": "PhoneCodeExpired",
        "PHONE_CODE_INVALID": "PhoneCodeInvalid",
        "API_ID_INVALID": "ApiIdInvalid",
        "PHONE_NUMBER_OCCUPIED": "PhoneNumberOccupied",
        "PHONE_NUMBER_UNOCCUPIED": "PhoneNumberUnoccupied",
        "USERS_TOO_FEW": "UsersTooFew",
        "USERS_TOO_MUCH": "UsersTooMuch",
        "TYPE_CONSTRUCTOR_INVALID": "TypeConstructorInvalid",
        "FILE_PART_INVALID": "FilePartInvalid",
        "FILE_PARTS_INVALID": "FilePartsInvalid",
        "FILE_PART_X_MISSING": "FilePartMissing",
        "MD5_CHECKSUM_INVALID": "Md5ChecksumInvalid",
        "PHOTO_INVALID_DIMENSIONS": "PhotoInvalidDimensions",
        "FIELD_NAME_INVALID": "FieldNameInvalid",
        "FIELD_NAME_EMPTY": "FieldNameEmpty",
        "MSG_WAIT_FAILED": "MsgWaitFailed",
        "PEER_ID_INVALID": "PeerIdInvalid",
        "MESSAGE_EMPTY": "MessageEmpty",
        "ENCRYPTED_MESSAGE_INVALID": "EncryptedMessageInvalid",
        "INPUT_METHOD_INVALID": "InputMethodInvalid",
        "PASSWORD_HASH_INVALID": "PasswordHashInvalid",
        "USERNAME_NOT_OCCUPIED": "UsernameNotOccupied",
        "USERNAME_INVALID": "UsernameInvalid",
        "MESSAGE_ID_INVALID": "MessageIdInvalid",
        "MESSAGE_NOT_MODIFIED": "MessageNotModified",
        "ENTITY_MENTION_USER_INVALID": "EntityMentionUserInvalid",
        "MESSAGE_TOO_LONG": "MessageTooLong",
        "ACCESS_TOKEN_EXPIRED": "AccessTokenExpired",
        "BOT_METHOD_INVALID": "BotMethodInvalid",
        "QUERY_TOO_SHORT": "QueryTooShort",
        "SEARCH_QUERY_EMPTY": "SearchQueryEmpty",
        "CHAT_ID_INVALID": "ChatIdInvalid",
        "DATE_EMPTY": "DateEmpty",
        "PERSISTENT_TIMESTAMP_EMPTY": "PersistentTimestampEmpty",
        "CDN_METHOD_INVALID": "CdnMethodInvalid",
        "VOLUME_LOC_NOT_FOUND": "VolumeLocNotFound",
        "FILE_ID_INVALID": "FileIdInvalid",
        "LOCATION_INVALID": "LocationInvalid",
        "CHAT_ADMIN_REQUIRED": "ChatAdminRequired",
        "PHONE_NUMBER_BANNED": "PhoneNumberBanned",
        "ABOUT_TOO_LONG": "AboutTooLong",
        "MULTI_MEDIA_TOO_LONG": "MultiMediaTooLong",
        "USERNAME_OCCUPIED": "UsernameOccupied",
        "BOT_INLINE_DISABLED": "BotInlineDisabled",
        "INLINE_RESULT_EXPIRED": "InlineResultExpired",
    },
    401: {
        "AUTH_KEY_UNREGISTERED": "AuthKeyUnregistered",
        "AUTH_KEY_INVALID": "AuthKeyInvalid",
        "USER_DEACTIVATED": "UserDeactivated",
        "SESSION_REVOKED": "SessionRevoked",
        "SESSION_EXPIRED": "SessionExpired",
        "ACTIVE_USER_REQUIRED": "ActiveUserRequired",
        "AUTH_KEY_PERM_EMPTY": "AuthKeyPermEmpty",
        "SESSION_PASSWORD_NEEDED": "SessionPasswordNeeded",
    },
    420: {
        "FLOOD_WAIT_X": "FloodWait",
    },
    500: {
        "AUTH_RESTART": "AuthRestart",
    },
}
