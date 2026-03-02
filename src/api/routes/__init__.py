"""
API Routes package for Meeting Intelligence Agent.
Contains all route handlers organized by functionality.
"""

from .health_routes import router as health_router

__all__ = [
    "health_router",

]