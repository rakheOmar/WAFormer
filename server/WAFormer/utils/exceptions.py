from enum import Enum
from typing import Any, Dict, Optional


class ErrorSeverity(str, Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class WAFormerException(Exception):
    def __init__(
        self,
        message: str,
        error_code: str = "UNKNOWN",
        severity: ErrorSeverity = ErrorSeverity.ERROR,
        context: Optional[Dict[str, Any]] = None,
        retryable: bool = False,
    ):
        self.message = message
        self.error_code = error_code
        self.severity = severity
        self.context = context or {}
        self.retryable = retryable
        super().__init__(self.message)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "error_code": self.error_code,
            "message": self.message,
            "severity": self.severity.value,
            "retryable": self.retryable,
            "context": self.context,
        }


class ConfigurationError(WAFormerException):
    def __init__(
        self,
        message: str,
        config_key: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message,
            error_code="CONFIG_ERROR",
            severity=ErrorSeverity.CRITICAL,
            context={**(context or {}), "config_key": config_key},
            retryable=False,
        )


class DataValidationError(WAFormerException):
    def __init__(
        self,
        message: str,
        invalid_field: Optional[str] = None,
        expected: Optional[str] = None,
        received: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message,
            error_code="VALIDATION_FAILED",
            severity=ErrorSeverity.WARNING,
            context={
                **(context or {}),
                "invalid_field": invalid_field,
                "expected": expected,
                "received": received,
            },
            retryable=False,
        )


class ProcessingError(WAFormerException):
    def __init__(
        self,
        message: str,
        step: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
        retryable: bool = True,
    ):
        super().__init__(
            message=message,
            error_code="PROCESSING_FAILED",
            severity=ErrorSeverity.ERROR,
            context={**(context or {}), "step": step},
            retryable=retryable,
        )


class FileOperationError(WAFormerException):
    def __init__(
        self,
        message: str,
        filepath: Optional[str] = None,
        operation: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(
            message=message,
            error_code="FILE_OPERATION_FAILED",
            severity=ErrorSeverity.ERROR,
            context={**(context or {}), "filepath": filepath, "operation": operation},
            retryable=True,
        )


__all__ = [
    "ErrorSeverity",
    "WAFormerException",
    "ConfigurationError",
    "DataValidationError",
    "ProcessingError",
    "FileOperationError",
]
