from django.test import TestCase
from src.linein.registry import RegistryManager, register
from src.linein.loader import NullLoader
from src.linein.source import *
from tests.loaders import *


class TestRegistry(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        RegistryManager().clear()

    def test_register(self):
        manager = RegistryManager()
        manager.register(UserLoader, category='sample', source=JSONFileSource('tests/samples/user.json'))
        register(UserLoader, category='preset', source=JSONFolderSource('tests/presets/user'))

        sample_loader = manager.get_loader(User, category='sample')
        preset_loader = manager.get_loader(User, category='preset')
        null_loader = manager.get_loader(User, category='not_exist')

        self.assertIsInstance(sample_loader, UserLoader)
        self.assertIsInstance(preset_loader, UserLoader)
        self.assertIsInstance(null_loader, NullLoader)

        self.assertIsNot(sample_loader, preset_loader)