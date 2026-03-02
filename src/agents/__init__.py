"""Agents package for the Enhanced Meeting Intelligence Agent.

This package provides tools and workflows for orchestrating meeting intelligence,
including database integration, audit logging, and AI-driven summarization.
"""

# Try to import core agent components with fallback handling
try:
    from .meeting_agent import UnifiedMeetingAgent, WorkflowState, WorkflowStep
    AGENTS_AVAILABLE = True
    # Define public API of the package
    __all__ = ["UnifiedMeetingAgent", "WorkflowState", "WorkflowStep"]
except (ImportError, AttributeError) as e:
    # Fallback when langchain dependencies are not available
    print(f"Warning: Agent imports failed due to dependency issues: {e}")
    print("Some agent functionality may not be available. Run 'python fix_dependencies.py' to resolve.")
    AGENTS_AVAILABLE = False
    __all__ = []

    # Define fallback classes for when imports fail
    class UnifiedMeetingAgent:
        def __init__(self, *args, **kwargs):
            raise RuntimeError("Meeting agent unavailable due to dependency issues")

    class WorkflowState:
        def __init__(self, *args, **kwargs):
            raise RuntimeError("Workflow state unavailable due to dependency issues")

    class WorkflowStep:
        def __init__(self, *args, **kwargs):
            raise RuntimeError("Workflow step unavailable due to dependency issues")