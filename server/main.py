from WAFormer.utils.logger import logger
from WAFormer.utils.exceptions import (
    ConfigurationError,
    DataValidationError,
    ProcessingError,
    FileOperationError,
)


def main():
    logger.debug("Debug message - detailed diagnostic info")
    logger.info("Info message - general informational message")
    logger.warning("Warning message - something unexpected happened")
    logger.error("Error message - serious problem occurred")

    try:
        logger.info("Testing ConfigurationError...")
        raise ConfigurationError(
            "Invalid configuration setting provided",
            config_key="database.host",
        )
    except ConfigurationError as e:
        logger.error(f"{e.error_code}: {e.message}", extra=e.to_dict())

    try:
        logger.info("Testing DataValidationError...")
        raise DataValidationError(
            "Input data does not meet validation requirements",
            invalid_field="email",
            expected="valid email format",
            received="invalid-email",
        )
    except DataValidationError as e:
        logger.warning(f"{e.error_code}: {e.message}", extra=e.to_dict())

    try:
        logger.info("Testing ProcessingError...")
        raise ProcessingError(
            "Failed to process data due to internal error",
            step="data_transformation",
            retryable=True,
        )
    except ProcessingError as e:
        logger.error(
            f"{e.error_code}: {e.message} (retryable: {e.retryable})", extra=e.to_dict()
        )

    try:
        logger.info("Testing FileOperationError...")
        raise FileOperationError(
            "Unable to read file from specified path",
            filepath="/data/input.csv",
            operation="read",
        )
    except FileOperationError as e:
        logger.error(
            f"{e.error_code}: {e.message} (retryable: {e.retryable})", extra=e.to_dict()
        )

    logger.info("Exception testing completed successfully!")


if __name__ == "__main__":
    main()
