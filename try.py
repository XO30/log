import log
log = log.Logging('example', file_name='example.log', file_mode='w', logging_level='DEBUG', console_output=True)

log.debug('hello')
log.info('this')
log.warning('is')
log.error('an')
log.critical('example')


@log.func_log
def square(x):
    """
    function to square an int
    :param x: int: input nr.
    :return: int: output nr.
    """
    return x ** 2


square(5)
