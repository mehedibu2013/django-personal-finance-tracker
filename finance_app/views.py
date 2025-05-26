from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transaction, Category
from .forms import TransactionForm, CategoryForm


@login_required
def dashboard(request):
    """Show recent transactions on the dashboard."""
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')[:5]
    return render(request, 'dashboard.html', {'transactions': transactions})


@login_required
def transaction_list(request):
    """Display all transactions for the logged-in user."""
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transaction_list.html', {'transactions': transactions})


@login_required
def add_transaction(request):
    """Add a new transaction."""
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()

    return render(request, 'transaction_form.html', {'form': form, 'title': 'Add Transaction'})


@login_required
def edit_transaction(request, pk):
    """Edit an existing transaction."""
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'transaction_form.html', {'form': form, 'title': 'Edit Transaction'})


@login_required
def delete_transaction(request, pk):
    """Delete a transaction after confirmation."""
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')

    return render(request, 'confirm_delete.html', {'object': transaction})


@login_required
def profile(request):
    """User profile view."""
    return render(request, 'profile.html', {'user': request.user})


@login_required
def category_list(request):
    """List all categories for the logged-in user."""
    categories = Category.objects.filter(user=request.user)
    return render(request, 'category_list.html', {'categories': categories})


@login_required
def add_category(request):
    """Add a new category."""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'category_form.html', {'form': form, 'title': 'Add Category'})


@login_required
def edit_category(request, pk):
    """Edit an existing category."""
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'category_form.html', {'form': form, 'title': 'Edit Category'})


@login_required
def delete_category(request, pk):
    """Delete a category after confirmation."""
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')

    return render(request, 'confirm_delete.html', {'object': category})