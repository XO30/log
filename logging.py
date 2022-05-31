import functools
import os.path
from os import path
from datetime import datetime

class Logging:
    def __init__(self,name:str, file_name:str = None, file_mode:str = 'w+', logging_level:str = 'DEBUG', console_output = True):
        self.name = name
        self.file_name = file_name
        self.file_mode = file_mode
        self.logging_level = logging_level
        self.console_output = console_output
        self.datetime_format = '%Y-%m-%d:%H:%M:%S'
        self.exception_log_level = 'WARNING'
        self.se_log_level = 'DEBUG'
        self.info_log_level = 'INFO'
        self._create_logfile()

    def _is_file(self):
        if self.file_name:
            return True
        return False

    def _create_logfile(self):
        if self._is_file():
            if path.exists(self.file_name):
                if os.stat(self.file_name).st_size != 0 and self.file_mode == 'a' or 'a+':
                    with open(self.file_name, self.file_mode) as f:
                        f.write('')
                elif self.mode == 'w' or 'w+':
                    with open(self.file_name, self.file_mode) as f:
                        f.write('The log ' + self.name + ' was created on ' + self._get_date_time() + '\n\n')
            else:
                with open(self.file_name, 'w+') as f:
                    f.write('The log ' + self.name + ' was created on ' + self._get_date_time() + '\n\n')
        return

    def _prepare_message(self, level:int, datetime:datetime, message:str):
        return str(datetime + ':' + level + ':' + message + '\n')

    def _write_logfile(self, level:int, datetime:datetime, message:str):
        if self._is_file():
            with open(self.file_name, 'a') as f:
                f.write(self._prepare_message(level, datetime, message))
        return

    def _print_log(self, level:int, datetime:datetime, message:str):
        if self.console_output:
            print(self._prepare_message(level, datetime, message))
        return

    def _get_date_time(self):
        return str(datetime.now().strftime(self.datetime_format))

    def _level_interpreter(self, level:str):
        translate = {
            'DEBUG': 0,
            'INFO': 1,
            'WARNING': 2,
            'ERROR': 3,
            'CRITICAL': 4
        }

        threshold = translate[self.logging_level]
        comparison = translate[level]
        if comparison >= threshold:
            return True
        return False

    def _direct_to_log_level(self, level:str):
        redirection = {
            'DEBUG': self.debug,
            'INFO': self.info,
            'WARNING': self.warning,
            'ERROR': self.error,
            'CRITICAL': self.critical,
            'NONE': None
        }
        return redirection[level]

    def set_datetime_format(self, format:str):
        self.datetime_format = format
        return

    def debug(self, message:str):
        level = 'DEBUG'
        if self._level_interpreter(level):
            self._write_logfile(level, self._get_date_time(), message)
        self._print_log(level, self._get_date_time(), message)
        return

    def info(self, message:str):
        level = 'INFO'
        if self._level_interpreter(level):
            self._write_logfile(level, self._get_date_time(), message)
        self._print_log(level, self._get_date_time(), message)
        return

    def warning(self, message:str):
        level = 'WARNING'
        if self._level_interpreter(level):
            self._write_logfile(level, self._get_date_time(), message)
        self._print_log(level, self._get_date_time(), message)
        return

    def error(self, message:str):
        level = 'ERROR'
        if self._level_interpreter(level):
            self._write_logfile(level, self._get_date_time(), message)
        self._print_log(level, self._get_date_time(), message)
        return

    def critical(self, message:str):
        level = 'CRITICAL'
        if self._level_interpreter(level):
            self._write_logfile(level, self._get_date_time(), message)
        self._print_log(level, self._get_date_time(), message)
        return

    def func_log(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            error_func = self._direct_to_log_level(self.exception_log_level)
            try:
                se_func = self._direct_to_log_level(self.se_log_level)
                info_func = self._direct_to_log_level(self.info_log_level)
                if se_func is not None:
                    se_func('About to run %s' % func.__name__)
                if func.__doc__ and info_func is not None:
                    info_func(func.__doc__)
                result = func(*args, **kwargs)
                if se_func is not None:
                    se_func('Done running %s' % func.__name__)
                return result
            except Exception as e:
                if error_func is not None:
                    error_func(f"Exception raised in {func.__code__.co_filename}, function: {func.__name__}. exception: {str(e)}")
                raise e
        return wrapper
