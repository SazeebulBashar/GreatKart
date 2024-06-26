from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import Cart, CartItem
from carts.views import _cart_id
from django.core.paginator  import Paginator,  EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.

def store(request, category_slug=None):
    category = None
    products = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=category, is_available=True).order_by('id')
        no_of_products = products.count()
        paginator = Paginator(products, 6)
        page =  request.GET.get('page')
        paged_products = paginator.get_page(page)

    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        no_of_products = products.count()
        paginator = Paginator(products, 6)
        page =  request.GET.get('page')
        paged_products = paginator.get_page(page)
    context = {
        'products': paged_products,
        'no_of_products': no_of_products
    }
    return render(request, 'store/store.html',context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id =  _cart_id(request), product=single_product)
    except Exception as e:
        raise e
    context={
        'single_product': single_product,
        'in_cart'       : in_cart,
    }
    return render(request, 'store/product_details.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            no_of_products = products.count()
    context ={
        'products': products,
        'no_of_products': no_of_products
    }
    return render(request, 'store/store.html', context)