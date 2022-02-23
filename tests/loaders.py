from src.linein.loader import Loader, M2MFieldWithThrough
from tests.models import *
from tests.serializers import *


class UserLoader(Loader):
    model = User
    serializer_class = UserSerializer


class TagLoader(Loader):
    model = Tag
    serializer_class = TagSerializer


class ProductLoader(Loader):
    model = Product
    serializer_class = ProductSerializer


class OrderLoader(Loader):
    model = Order
    serializer_class = OrderSerializerWithSave


class AltOrderLoader(Loader):
    model = Order
    serializer_class = OrderSerializerWithoutSave
    m2m_fields_with_through = [
        M2MFieldWithThrough(name='product_entries', serializer_class=OrderProductEntrySerializer, host_id_key='order')
    ]


class EntityLoader(Loader):
    model = Entity
    serializer_class = EntitySerializer
