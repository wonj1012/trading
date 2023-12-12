from functools import wraps
from typing import Any, Callable

from loguru import logger

# Logger configuration
logger.remove()
logger.add(
    "data/logs/runtime.log",
    rotation="1 week",
    level="INFO",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    backtrace=True,
    diagnose=True,
)


def get_logger():
    """
    Get the configured logger instance.

    Returns:
        loguru.Logger: The configured logger instance.
    """
    return logger


def with_logging(func: Callable) -> Callable:
    """
    Decorator to log the execution of a function.

    Logs the function call with its arguments and keyword arguments,
    successful execution, and any exceptions that occur.

    Args:
        func (Callable): The function to be wrapped by the decorator.

    Returns:
        Callable: The wrapped function.
    """

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Logging before function call
        logger.info(
            f"Calling function: {func.__name__} with args: {args}, kwargs: {kwargs}"
        )
        try:
            # Execute the function
            result = func(*args, **kwargs)
            # Logging after successful execution
            logger.info(f"Function {func.__name__} executed successfully")
            return result
        except Exception as e:
            # Logging on exception
            logger.error(f"Error in function {func.__name__}: {e}")
            raise

    return wrapper
