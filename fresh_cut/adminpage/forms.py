from django import forms
from .models import Category, SubCategory, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ["category", "name"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "category",
            "subcategory",
            "name",
            "price",
            "description",
            "image",
            "stock",
            "is_active",
        ]
