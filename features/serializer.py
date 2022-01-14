

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = ForeignKeyField(queryset=Category.objects, filter_by="name")
    class Meta:
        model = Product
        fields = "__all__"




class ProductFieldSerializer(serializers.ModelSerializer):
    product = ForeignKeyField(queryset=Products.objects, filter_by="product")
    class Meta:
        model = Product
        fields = "__all__"

