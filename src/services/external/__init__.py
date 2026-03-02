"""
External service integrations.

This module contains services that integrate with external APIs and services
such as email providers and third-party platforms.
"""

from .email.sendgrid_service import SendGridEmailService

__all__ = [
    "SendGridEmailService"
]