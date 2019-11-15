from file.FileService import FileService
from logs.LoggingService import LoggingService
from os import path as ospath

TAG = "FileServiceTests"
logger = LoggingService()
fs = FileService(logger)
path = "out.txt"
data = {"version": "0.0.1"}


def test_write():
    logger.log(TAG, "Writing file " + path)
    fs.write(path, data)
    exists = str(ospath.exists(path))
    logger.log(TAG, "File was created : " + exists)


def test_read():
    logger.log(TAG, "Reading file " + path)
    content = str(fs.read(path, True))
    matches = str(content == str(data))
    logger.log(TAG, "Content : " + content)
    logger.log(TAG, "Content matches data : " + matches)


def main():
    test_write()
    test_read()


if __name__== "__main__":
   main()
