"""
Email service integrations.

This module contains email service implementations for sending
notifications, summaries, and other communications.
"""

from .sendgrid_service import SendGridEmailService

__all__ = [
    "SendGridEmailService"
]