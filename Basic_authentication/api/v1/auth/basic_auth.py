#!/usr/bin/env python3
"""Basic Auth"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth (Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract_base64_authorization_header that returns the Base64
        part of the Authorization header for a Basic Authentication"""

        if authorization_header is None or not isinstance(
                authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header
        decoded value of a Base64 string
        base64_authorization_header"""

        if (base64_authorization_header is None or
                (type(base64_authorization_header) != str)):
            return None
        try:
            decodeBytes = base64.b64decode(base64_authorization_header)
            decodedStr = decodeBytes.decode("utf-8")
            return decodedStr
        except ValueError :
            return None
