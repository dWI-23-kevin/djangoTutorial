import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        logger.error(f"Unhandled exception: {exc}")
        return Response({
            'error': 'Internal Server Error.'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if response.status_code == status.HTTP_400_BAD_REQUEST:
        logger.warning(f"Invalid user input: {exc}")

    return response
