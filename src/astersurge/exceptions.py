"""
AsterSurge Exceptions

Version: 0.2.0
"""


class AsterSurgeError(Exception):
    """
    Base exception for AsterSurge.
    """

    pass


class ConfigurationError(AsterSurgeError):
    """
    Invalid configuration.
    """

    pass


class ProviderError(AsterSurgeError):
    """
    Provider-related errors.
    """

    pass


class ToolError(AsterSurgeError):
    """
    Tool execution errors.
    """

    pass


class PluginError(AsterSurgeError):
    """
    Plugin-related errors.
    """

    pass


class MemoryError(AsterSurgeError):
    """
    Memory-related errors.
    """

    pass


class ModelError(AsterSurgeError):
    """
    Model-related errors.
    """

    pass


class CacheError(AsterSurgeError):
    """
    Cache-related errors.
    """

    pass


class ValidationError(AsterSurgeError):
    """
    Validation errors.
    """

    pass
