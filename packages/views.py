from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Product, Category, Calendar, Review, Time
from .forms import ProductForm, Calendar, CalendarForm, ReviewForm, TimeForm
from django.views.generic import CreateView

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all().order_by("-price")
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    reviewed = False
    product = get_object_or_404(Product, pk=product_id)
    form = CalendarForm(request.POST)
    review = product.reviews.all()
    rating = request.POST.get('rating', 10)

    print('REVIEW before valid: ', review)


    review_form = ReviewForm(data=request.POST)
    if review_form.is_valid():
        review_form.instance.email = request.user.email
        review_form.instance.name = request.user.username
        r = review_form.save(commit=False)
        r.product = product
        r.save()
        reviewed = True
        print(f'reviewed: {reviewed}')
        print('REVIEW after valid: ', review)
    else:
        review_form = ReviewForm()

    context = {
        'product': product,
        'form': form,
        "review_form": ReviewForm(),
        "reviewed": reviewed,
        "review": review,
    }
    

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only studio owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only studio owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('packages'))


class CalendarCreateView(CreateView):
    model = Calendar
    form_class = CalendarForm
    


# View for deleting a review as Site User
@login_required
def delete_user_review(request, review_id):
    """ Delete review
    """
    eview = get_object_or_404(Review, id=review_id)
    product_id = review.product.id
    review.delete()
    messages.success(request, 'Your review was deleted successfully!')
    return HttpResponseRedirect(reverse(
'product_detail', args=[product_id]))

# View for editing a review as Site User


class EditReview(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Edit review
    """
    model = Review
    template_name = 'products/edit_user_review.html'
    form_class = ReviewForm
    success_message = 'Your review was successfully updated!'