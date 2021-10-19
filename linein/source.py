__all__ = ['Source', 'JSONFileSource', 'JSONFolderSource']

import os
import json
import glob


class Source:
    def __iter__(self):
        return


class JSONFileSource(Source):
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        with open(self.file_path) as f:
            data = json.load(f, strict=False)
            assert isinstance(data, list)
            return iter(data)


class JSONFolderSource(Source):
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def __iter__(self):
        for file_path in glob.iglob(os.path.join(self.folder_path, '**/*.json'), recursive=True):
            with open(file_path) as f:
                data = json.load(f)
                yield data