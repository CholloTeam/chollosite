import random
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.shortcuts import render, get_object_or_404
from chollosite.chollo_cart.forms import CartAddProductForm
from .models import Category, Product, Profile
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, SearchForm



def home(request):
    categories = list(Category.objects.all())

    # Select six random categories
    random_category = random.sample(categories, k=6)

    # Select random product from the categories
    random_products = []
    for category in random_category:
        # Retrieve a random product from each catogory
        random_product = Product.objects.filter(category=category).order_by('?').first()
        random_products.append(random_product)

    return render(request, "chollo_main/index.html",
                  {'random_products': random_products})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, "chollo_main/product_list.html",
                  {'category': category,
                  'categories': categories,
                  'products': products})


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id,
                                slug=slug,
                                available=True
                                )
    cart_product_form = CartAddProductForm()
    return render(request,
                  "chollo_main/product.html",
                  {"product": product,
                   "cart_product_form": cart_product_form,
                   }
                  )


@login_required
def dashboard(request):
    return render(request, 'registration/login.html',
                  {'section': 'dashboard'})

#
# def cart_details(request):
#     return render(request, "chollo_main/cart-details.html")


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but avoid saving
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # save the user object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request, 'chollo_main/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'chollo_main/register.html', {'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')

        else: messages.error(request, "Error updating your profile")

    else:
        user_form = UserRegistrationForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile
        )

        return render(request, 'chollo_main/edit.html',
                      {'user_form': user_form, 'profile_form': profile_form})


def item_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('name', weight='A') + SearchVector('description', weight='B',  config='spanish')
            search_query = SearchQuery(query, config='spanish')
            products = Product.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)).filter(rank__gte=0.3).order_by('-rank')
            results = products
    return render(request, 'chollo_main/search.html',
                  {'form': form, 'query': query, 'results': results})

