from celery.decorators import task
from celery.utils.log import get_task_logger

from .email_conf import send_review_email

logger = get_task_logger(__name__)


@task(name="send_email_task")
def send_email_task(email):
    logger.info("Sent review email")
    return send_review_email(email)