__all__ = ['Loader', 'NullLoader']


class Loader:
    model = None
    source = None
    serializer_class = None

    def load(self):
        if not self.source or not self.serializer_class:
            return

        for raw_data in self.source:
            data = self.parse(raw_data)
            serializer = self.serializer_class(data=data)
            serializer.save()

    def parse(self, raw_data):
        return raw_data


class NullLoader(Loader):
    def load(self):
        return