"""Mock authentication for development and testing."""

from typing import List
from fastapi import HTTPException
from fastapi.security import HTTPBearer

# HTTP bearer scheme
security_scheme = HTTPBearer(auto_error=True)

class BearerAuth:
    """Mock Bearer Authentication class."""
    def __init__(self, token: str="", roles: List[str] = None):
        self.token = token
        self.roles = roles or ["feedback:read", "feedback:write"]
        self.user_id = "mock-user-001"
    
    def has_role(self, role:str) -> bool:
        """Check if user has specific role."""
        return role in self.roles

def security(any_role: List[str] = None, all_roles: List[str] = None):
    """Security decorators for FastAPI routes."""
    any_role = any_role or []
    all_roles = all_roles or []

    def decorator(func):
        async def wrapper(*args, **kwargs):
            # pass all authentication checks
            return await func(*args, **kwargs)
        return wrapper
    return decorator