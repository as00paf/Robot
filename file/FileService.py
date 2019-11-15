import json
import sys
from os import path as ospath


class FileService:
    TAG = "FileService"

    def __init__(self, logger):
        self.logger = logger
        logger.log(self.TAG, "FileService instantiated")

    def write(self, path, data):
        with open(path, 'w', encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True)
        self.logger.log(self.TAG, "File written at " + path)

    def read(self, path, print_result):
        try:
            with open(path, 'r', -1, encoding="utf-8") as json_file:
                data = json.load(json_file)
                if print_result:
                    self.logger.log(self.TAG, "File content : " + str(data))
                return data
        except Exception:
            print("Could not read file " + path, sys.exc_info()[0])
            return str(sys.exc_info()[0])

    # noinspection PyMethodMayBeStatic
    def exists(self, path):
        return ospath.exists(path)
