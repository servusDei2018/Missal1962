from constants.common import LANGUAGE_LATIN
from kalendar.factory import MissalFactory

missal_buffer = {}


def get_missal(year, lang=LANGUAGE_LATIN):
    missal_id = f'{year}{lang}'
    if missal_id not in missal_buffer:
        missal_buffer[missal_id] = MissalFactory().create(year, lang=lang)
    return missal_buffer[missal_id]
