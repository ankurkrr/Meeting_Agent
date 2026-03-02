"""
Base service layer components.

This module provides base classes and interfaces for all services in the application.
It establishes common patterns for error handling, logging, and dependency injection.
"""

from .service_base import BaseService
from .repository_base import BaseRepository
from .interfaces import (
    IMeetingService,
    IWorkflowService,
    ITaskService,
    IEmailService,
    ICalendarService,
    IRepository
)

__all__ = [
    "BaseService",
    "BaseRepository",
    "IMeetingService",
    "IWorkflowService",
    "ITaskService",
    "IEmailService",
    "ICalendarService",
    "IRepository"
]