from log import Logging
log = Logging('test', file_name='test.log', file_mode='w', logging_level='DEBUG', console_output=True)

log.debug('hallo')
log.info('das')
log.warning('ist')
log.error('ein')
log.critical('test')


print(log)
print(repr(log))
