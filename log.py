import functools
from os import path
from datetime import datetime


class Logging:
    """
    Lightweight Logger for python
    Version: 0.9.2
    Last Update: 04.06.2022
    Developer: XO30

    Parameters
    :param name: str: designation of the logger
    :param file_name: str: path and name of the logfile
    :param file_mode: str: file access modes
    :param logging_level: str: logging level
    :param console_output: boolean: activate/deactivate console output

    Methods
    :method set_datetime_format(str): set the datetime format
    :method debug(str): logs to level DEBUG
    :method info(str): logs to level INFO
    :method warning(str): logs to level WARNING
    :method error(str): logs to level ERROR
    :method critical(str): logs to level CRITICAL
    :method func_log(str): decorator that logs the start and end of a func call, logs the func documentation and possible runtime errors
    """

    def __init__(self, name: str, file_name: str = None, file_mode: str = 'w+', logging_level: str = 'WARNING', console_output: bool = True):
        """
        init method of class Logging
        :param name: str: designation of the logger
        :param file_name: str: path and name of the logfile
        :param file_mode: str: file access modes
        :param logging_level: str: logging level
        :param console_output: boolean: activate/deactivate console output
        """
        self.date_time_format = '%Y-%m-%d:%H:%M:%S'
        self.exception_log_level = 'WARNING'
        self.se_log_level = 'DEBUG'
        self.info_log_level = 'INFO'
        if self._validate_init(name, file_name, file_mode, logging_level, console_output):
            self.name = name
            self.file_name = file_name
            self.file_mode = file_mode
            self.logging_level = logging_level
            self.console_output = console_output
            self._create_logfile()

    def __repr__(self):
        """
        repr method of class Logger
        :return: str: str representation of class
        """
        rep = 'log.Logger({}, {}, {}, {}, {})'.format(
            self.name,
            self.file_name,
            self.file_mode,
            self.logging_level,
            self.console_output
        )
        return rep

    def __str__(self):
        """
        str method of class Logger
        :return: str: Information about Logger
        """
        title = ' \033[1m' + 'Logger detail' + '\033[0m\n'
        info = (
            ' name: {}\n'.format(self.name),
            'file_name: {}\n'.format(self.file_name),
            'file_mode: {}\n'.format(self.file_mode),
            'logging_level: {}\n'.format(self.logging_level),
            'console_output: {}\n'.format(self.console_output),
            'date_time_format: {}\n'.format(self.date_time_format),
            'exception_log_level: {}\n'.format(self.exception_log_level),
            'se_log_level: {}\n'.format(self.se_log_level),
            'info_log_level: {}\n'.format(self.info_log_level)
        )
        return title + ' '.join(info)

    @staticmethod
    def _validate_init(name: str, file_name: str, file_mode: str, logging_level: str, console_output: bool):
        """
        validation of user inputs
        :param name: str: designation of the logger
        :param file_name: str: path and name of the logfile
        :param file_mode: str: file access modes
        :param logging_level: str: logging level
        :param console_output: boolean: activate/deactivate console output
        :return: bool: True
        """
        if not isinstance(name, str):
            raise TypeError('name can not be {} it has to be {}.'.format(type(name), str))
        if not isinstance(file_name, str) and file_name is not None:
            raise TypeError('file_name can not be {} it has to be {} or {}'.format(type(file_name), str, type(None)))
        if not isinstance(file_mode, str):
            raise TypeError('file_mode can not be {} it has to be {}'.format(type(file_name), str))
        if file_mode not in ['w', 'a']:
            raise ValueError('file_mode can not be {}, it has to be "w" or or "a"'.format(file_mode))
        if not isinstance(logging_level, str):
            raise TypeError('logging_level can not be {} it has to be {}'.format(type(file_name), str))
        if logging_level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            raise ValueError('logging_level can not be {}, it has to be "DEBUG", "INFO", "WARNING", "ERROR" or "CRITICAL"'.format(logging_level))
        if not isinstance(console_output, bool):
            raise TypeError('console_output can not be {} it has to be {}'.format(type(console_output), bool))
        return True

    @staticmethod
    def _prepare_message(name: str, level: str, date_time: str, message: str):
        """
        prepares and returns the message
        :param level: str: logging level as
        :param date_time: str: actual datetime
        :param message: str: message
        :return: str: log entry
        """
        return date_time + ':' + name + ':' + level + ':' + message + '\n'

    @staticmethod
    def _any_to_str(message: any):
        """
        tries to convert any type to string
        :param message: any: message
        :return: validated_message: message
        """
        try:
            validated_message = str(message)
            return validated_message
        except TypeError:
            print('{} can not be converted to {}'.format(type(message), str))

    def _is_file(self):
        """
        check if logfile is activated
        :return: bool: activated/deactivated
        """
        if self.file_name:
            return True
        return False

    def _check_logfile(self):
        """
        checks if logfile exists and creates one if not
        :return: bool: True
        """
        if path.exists(self.file_name):
            return True
        else:
            open(self.file_name, 'w+')
            return True

    def _create_logfile(self):
        """
        if necessary creates the logfile while initializing
        :return: bool: True
        """
        if path.exists(self.file_name):
            if self.file_mode == 'w':
                open(self.file_name, 'w+')
        else:
            open(self.file_name, 'w+')
        return True

    def _write_logfile(self, name: str, level: str, date_time: str, message: str):
        """
        writes the message to the logfile
        :param level: str: logging level
        :param date_time: str: actual datetime
        :param message: str: log entry
        :return: boolean: True
        """
        if self._is_file() and self._check_logfile():
            with open(self.file_name, 'a') as f:
                f.write(self._prepare_message(name, level, date_time, message))
        return True

    def _print_log(self, name: str, level: str, date_time: str, message: str):
        """
        prints the message to the console
        :param level: str: logging level
        :param date_time: str: actual datetime
        :param message: str: message
        :return: boolean: True
        """
        if self.console_output:
            print(self._prepare_message(name, level, date_time, message))
        return True

    def _get_date_time(self):
        """
        returns the actual datetime
        :return: str: actual datetime
        """
        return str(datetime.now().strftime(self.date_time_format))

    def _level_interpreter(self, level: str):
        """
        takes logging level as a string and decides if message should be logged
        :param level: str: logging level
        :return: bool: log/nlog
        """
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

    def _direct_to_log_level(self, level: str):
        """
        checks to which level a message should be assigned
        :param level: str: logging level
        :return: func: logging function
        """
        redirection = {
            'DEBUG': self.debug,
            'INFO': self.info,
            'WARNING': self.warning,
            'ERROR': self.error,
            'CRITICAL': self.critical,
            None: None
        }
        return redirection[level]

    def set_datetime_format(self, date_time_format: str):
        """
        set the datetime format
        :param date_time_format: str: format of the datetime
        :return: bool: True
        """
        self.date_time_format = date_time_format
        return True

    def debug(self, message: str):
        """
        logs to level DEBUG
        :param message: str: message
        :return: bool: True
        """
        level = 'DEBUG'
        message = self._any_to_str(message)
        if self._level_interpreter(level):
            self._write_logfile(self.name, level, self._get_date_time(), message)
        self._print_log(self.name, level, self._get_date_time(), message)
        return True

    def info(self, message: any):
        """
        logs to level INFO
        :param message: any: message
        :return: bool: True
        """
        level = 'INFO'
        message = self._any_to_str(message)
        if self._level_interpreter(level):
            self._write_logfile(self.name, level, self._get_date_time(), message)
        self._print_log(self.name, level, self._get_date_time(), message)
        return True

    def warning(self, message: any):
        """
        logs to level WARNING
        :param message: any: message
        :return: bool: True
        """
        level = 'WARNING'
        message = self._any_to_str(message)
        if self._level_interpreter(level):
            self._write_logfile(self.name, level, self._get_date_time(), message)
        self._print_log(self.name, level, self._get_date_time(), message)
        return True

    def error(self, message: any):
        """
        logs to level ERROR
        :param message: any: message
        :return: bool: True
        """
        level = 'ERROR'
        message = self._any_to_str(message)
        if self._level_interpreter(level):
            self._write_logfile(self.name, level, self._get_date_time(), message)
        self._print_log(self.name, level, self._get_date_time(), message)
        return True

    def critical(self, message: str):
        """
        logs to level CRITICAL
        :param message: str: message
        :return: bool: True
        """
        level = 'CRITICAL'
        message = self._any_to_str(message)
        if self._level_interpreter(level):
            self._write_logfile(self.name, level, self._get_date_time(), message)
        self._print_log(self.name, level, self._get_date_time(), message)
        return True

    def func_log(self, func):
        """
        decorator that logs the start and end of a func call, logs the func documentation and possible runtime errors
        :param func: func: decorated function
        :return: func: wrapper
        """
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
