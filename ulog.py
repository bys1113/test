import logging, os

'''
2020
logging模块的四大组件
  组件                           说明
loggers              提供应用程序代码直接使用的接口
handlers             用于将日志记录发送到指定的目的位置
filters              提供更细粒度的日志过滤功能，用于决定哪些日志记录将会被输出（其它的日志记录将会被忽略）
formatters           用于控制日志信息的最终输出格式

'''

_fileLogger = None
_consoleLogger = None
_defaultLogger = None
_defaultLoggerLevel = logging.INFO


# 外部接口使用
def getConsoleLogger():
    global _consoleLogger
    return _consoleLogger


# 外部接口使用
def getFileLogger():
    global _fileLogger
    return _fileLogger


# 初始化用户文件日志
def initFileLogger(filename, level=_defaultLoggerLevel):
    global _fileLogger
    logger = logging.getLogger('Ulog_File')
    fh = logging.FileHandler(filename)
    fh.setFormatter(_getLogFormater())
    logger.addHandler(fh)
    logger.setLevel(level)

    _fileLogger = logger


# 初始化控制台日志
def initConsleLogger(level=_defaultLoggerLevel):
    global _consoleLogger
    logger = logging.getLogger("Ulog_console")
    for hdlr in logger.handlers[:]:
        hdlr.close()
        logger.removeHandler(hdlr)
    ch = logging.StreamHandler()
    ch.setFormatter(_getLogFormater())
    logger.addHandler(ch)
    logger.setLevel(level)
    _consoleLogger = logger


# 定义日志格式的前缀
def _getLogFormater():
    '''统一log前缀格式'''
    fmt = logging.Formatter(fmt="%(asctime)s %(levelname)s:%(message)s", datefmt="%Y/%m/%d %H:%M:%S")
    return fmt


# 输出Info级别的LOG
def ulogInfo(msg):
    global _consoleLogger
    global _fileLogger
    if _consoleLogger:
        _consoleLogger.info(msg)
    if _fileLogger:
        _fileLogger.info(msg)


# 输出Warn级别的LOG
def ulogWarn(msg):
    global _consoleLogger
    global _fileLogger
    if _consoleLogger:
        _consoleLogger.warning(msg)
    if _fileLogger:
        _fileLogger.warning(msg)


initConsleLogger()
initFileLogger(r'E:\log.txt')
ulogInfo('HaHaHa')
