import getpass
import hashlib
import logging


logger = logging.getLogger('password_checker')

def input_and_check_password():
    password: str = getpass.getpass()

    if not password:
        logger.error('Syötät tyhjä salasana ')
        return False

    try:
        hasher = hashlib.md5()
        logger.info(f'Luodaan hasher objektti {hasher}')
        hasher.update(password.encode('latin-1'))

        if hasher.hexdigest() == '098klgjmdfg658asffsdfg36709lkdfg':
            return True
    except ValueError as ex:
        logger.exception('Syötat väärin merkkiä', exc_info=ex)


    return False


if __name__ == "__main__":
    logger.info('Yrität tunnistaa itsesi sivustolla')
    count_number: int = 3

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1
    logger.error('salasana on väärin 3 kertää')
    exit(1)