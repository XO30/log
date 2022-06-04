import log
log = log.Logging('test', file_name='test.log', file_mode='w', logging_level='DEBUG', console_output=True)

print(log)
log.info('hallo, das ist ein Test')
log.error('keine Ahnung')

@log.func_log
def square(x):
    """
    function to square a int
    :param x: int: input nr.
    :return: int: output nr.
    """
    return x ** 2

square(5)

log.se_log_level = None

square(3)

log.debug('hello')
log.info('this')
log.warning('is')
log.info('a')
log.critical('example')