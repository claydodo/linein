__all__ = [
    'Source',
    'FolderSourceBase',
    'FileTypeFolderSourceBase',
    'JSONFolderSource',
    'JSONFileSource',
]

import os
import json
import glob


class Source:
    def __iter__(self):
        return


class FolderSourceBase(Source):
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def __iter__(self):
        for file_path in self.list_files():
            yield self.load_file(file_path)

    def list_files(self):
        return glob.iglob(os.path.join(self.folder_path, '*'))

    def load_file(self, file_path):
        raise NotImplementedError


class FileTypeFolderSourceBase(FolderSourceBase):
    ext = ''

    def list_files(self):
        if not self.ext:
            file_pattern = '*'
        else:
            file_pattern = '*.{}'.format(self.ext.lstrip('.'))
        return glob.iglob(os.path.join(self.folder_path, file_pattern))


class JSONFolderSource(FileTypeFolderSourceBase):
    ext = 'json'

    def load_file(self, file_path):
        with open(file_path) as f:
            return json.load(f)


class JSONFileSource(Source):
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        with open(self.file_path) as f:
            data = json.load(f, strict=False)
            assert isinstance(data, list)
            return iter(data)


