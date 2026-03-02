"""
Refactored Services Layer

This module provides a clean, well-organized service layer with:
- Clear separation of concerns
- Dependency injection
- Consistent error handling
- Proper abstractions
- Health checks

Architecture:
- base/: Base classes and interfaces
- core/: Core business logic services
- external/: External API integrations
- data/: Data access layer
- integration/: Platform and system integrations
"""

# Base components
from .base.service_base import BaseService, ServiceResult
from .base.repository_base import BaseRepository
from .base.interfaces import IMeetingService, IWorkflowService, ITaskService

# Core business services
from .core.meeting_service import MeetingService

# External integrations
from .external.email.sendgrid_service import SendGridEmailService

# Google services
from .google import GoogleCalendarService, GoogleDriveService, GoogleSheetsService

# Data access layer
from .data.repositories.meeting_repository import MeetingRepository

# Integration services
from .integration.activity_logger import ActivityLogger
from .integration.agent_integration_service import AgentIntegrationService
# Commented out to avoid circular imports - import directly when needed
# from .integration.elevation_ai_integration_service import ElevationAIIntegrationService
# from .integration.elevation_ai_audit_service import ElevationAIAuditService
# from .integration.platform_api_client import PlatformAPIClient
# from .integration.platform_webhook_service import PlatformWebhookService
# from .integration.chain_visibility_service import ChainVisibilityService
# from .integration.data_flow_validator import DataFlowValidator
# from .integration.external_payload_processor import ExternalPayloadProcessor
# from .integration.integrated_email_workflow_service import IntegratedEmailWorkflowService

# Service factory for dependency injection
from .service_factory import ServiceFactory, get_service_factory

# Database service
from .database_service_new import get_database_service

# Migration helper
from .migration_helper import ServiceMigrationHelper

__all__ = [
    # Base components
    "BaseService",
    "ServiceResult",
    "BaseRepository",
    "IMeetingService",
    "IWorkflowService",
    "ITaskService",

    # Core services
    "MeetingService",

    # External services
    "SendGridEmailService",

    # Google services
    "GoogleCalendarService",
    "GoogleDriveService",
    "GoogleSheetsService",

    # Data layer
    "MeetingRepository",

    # Integration services
    "ActivityLogger",
    "AgentIntegrationService",
    # Commented out to avoid circular imports
    # "ElevationAIIntegrationService",
    # "ElevationAIAuditService",
    # "PlatformAPIClient",
    # "PlatformWebhookService",
    # "ChainVisibilityService",
    # "DataFlowValidator",
    # "ExternalPayloadProcessor",
    # "IntegratedEmailWorkflowService",

    # Factory
    "ServiceFactory",
    "get_service_factory",

    # Database
    "get_database_service",

    # Migration
    "ServiceMigrationHelper"
]