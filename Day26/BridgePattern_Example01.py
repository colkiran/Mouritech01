
import sys

class Handler:
    def __init__(self, myoutput):
        self.file = myoutput

    def emit(self, message):
        self.file.write(message + "\n")
        self.file.flush()

class FilteredLogger:
    def __init__(self, pattern, handler):
        self.pattern = pattern
        self.handler = handler

    def log(self, message):
        if self.pattern in message:
            self.handler.emit(message)

handler = Handler(sys.stdout)
logger = FilteredLogger("Error", handler)

logger.log("Ignored: This will not be logged")
logger.log("Error: This is very important")
