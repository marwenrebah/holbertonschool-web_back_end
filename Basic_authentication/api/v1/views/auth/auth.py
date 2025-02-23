#!/usr/bin/env python3
"""manage the API authentication"""

from flask import request
from typing import List, TypeVar, Union


class Auth:
    """Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        for i in range(len(excluded_paths)):
            if excluded_paths[i].rstrip("/") == path.rstrip("/"):
                return False
        return True

    def authorization_header(self, request=None) -> Union[str, None]:
        """authorization_header method"""
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar("User"):
        """current_user method"""
