from starlette.config import Config

config = Config()


class Settings:
    """Settings for the module"""

    TRANSACTION_MIDDLEWARE_LOG_LEVEL: str = config(
        "TRANSACTION_MIDDLEWARE_LOG_LEVEL", cast=str, default="INFO"
    ).upper()
    TRANSACTION_MIDDLEWARE_LOG_FORMAT: str = config(
        "TRANSACTION_MIDDLEWARE_LOG_FORMAT",
        cast=str,
        default="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    )

    # Disable transaction for the whole application
    TRANSACTION_MIDDLEWARE_DISABLED = config(
        "TRANSACTION_MIDDLEWARE_DISABLED", cast=bool, default=False
    )


settings = Settings()
