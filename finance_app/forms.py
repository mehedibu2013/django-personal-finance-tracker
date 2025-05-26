from django import forms
from .models import Transaction, Category

# Form for adding/editing transactions
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'category', 'type']  # Excludes non-editable date field

# Form for adding/editing categories
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']