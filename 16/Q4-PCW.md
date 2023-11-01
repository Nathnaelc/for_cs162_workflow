List of Classes in the Logging Library
The Python logging library defines a variety of classes for different logging functionalities. Some of the main classes and their parent classes are:

Handler (Base class)
StreamHandler (inherits from Handler)
FileHandler (inherits from StreamHandler)
RotatingFileHandler (inherits from FileHandler)
TimedRotatingFileHandler (inherits from RotatingFileHandler)
SocketHandler (inherits from Handler)
DatagramHandler (inherits from SocketHandler)
SysLogHandler (inherits from Handler)
SMTPHandler (inherits from Handler)
NullHandler (inherits from Handler)
MemoryHandler (inherits from BufferingHandler, which inherits from Handler)
HTTPHandler (inherits from Handler)
QueueHandler (inherits from Handler)
NTEventLogHandler (inherits from Handler)
Methods in FileHandler Class
The FileHandler class inherits from StreamHandler and ultimately from Handler. Here are some methods that one can call on a FileHandler object:

**init**(self, filename, mode, encoding, delay)
close(self)
emit(self, record)
\_open(self)
flush(self)
handle(self, record)
setFormatter(self, fmt)
setLevel(self, level)
addFilter(self, filter)
removeFilter(self, filter)
