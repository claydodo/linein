class Source:
    def __iter__(self):
        return


class JSONFileSource(Source):
    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        return


class JSONFolderSource(Source):
    def __init__(self, folder_path):
        self.folder_path = folder_path
