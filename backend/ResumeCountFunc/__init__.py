import logging

import azure.functions as func

from .resume_counter import count_updater


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return count_updater(req)