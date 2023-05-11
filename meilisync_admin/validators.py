import i18n
from email_validator import EmailNotValidError
from fastapi import HTTPException
from pydantic import validate_email
from starlette.status import HTTP_400_BAD_REQUEST
from tortoise.validators import Validator


class EmailValidator(Validator):
    def __call__(self, value: str):
        if not value:
            return
        try:
            validate_email(value)
        except EmailNotValidError:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail=i18n.t("email_invalid", email=value),
            )
