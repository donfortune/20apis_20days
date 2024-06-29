from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.conf import settings
from .forms import *
from django.views import View
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/product-list/',
        'Detail View': '/product-detail/<str:pk>/',
        'Create': '/product-create/',
        'Update': '/product-update/<str:pk>/',
        'Delete': '/product-delete/<str:pk>/',
    }
    return (Response(api_urls))

@api_view(['GET'])
def productLists(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def productList(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addProduct(request):
    data = {
        'name': request.data['name'],
        'price': request.data['price'],
        'description': request.data['description'],
    }
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateProduct(request, id):
    product = Product.objects.get(id=id)
    data = {
        'name': request.data['name'],
        'price': request.data['price'],
        'description': request.data['description'],
    }
    serializer = ProductSerializer(instance=product, data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return Response('Product deleted successfully')


@api_view(['GET'])
def orderItems(request):
    order = OrderItem.objects.all()
    serializer = OrderItemSerializer(order, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def orderItem(request, id):
    order = OrderItem.objects.get(id=id)
    serializer = OrderItemSerializer(order, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createOrderItem(request):
    data = {
        'order': request.data['order'],
        'product': request.data['product'],
        'quantity': request.data['quantity'],
    }
    serializer = OrderItemSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addOrderCart(request, id):
    order = OrderItem.objects.get(id=id)
    data = {
        'order': request.data['order'],
        'product': request.data['product'],
        'quantity': request.data['quantity'],
    }


# class PaymentView(View):
#     def get(self, request, *args, **kwargs):
#         form = PaymentForm()
#         return render(request, 'payment.html', {'form': form, 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})

#     def post(self, request, *args, **kwargs):
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             stripe_token = form.cleaned_data['stripe_token']
#             payment_method = form.cleaned_data['payment_method']
#             user = request.user
            
#             try:
#                 # Calculate the amount based on the cart items
#                 cart_items = CartItem.objects.filter(user=user, purchased=False)
#                 amount = sum(item.price for item in cart_items) * 100  # Amount in cents

#                 # Create a Stripe charge
#                 charge = stripe.Charge.create(
#                     amount=amount,
#                     currency='usd',
#                     source=stripe_token,
#                     description='Payment for cart items'
#                 )

#                 # Save the payment information to the database
#                 payment = Payment.objects.create(
#                     user=user,
#                     payment_method=payment_method,
#                     payment_status='completed',
#                     stripe_charge_id=charge.id
#                 )
#                 payment.cart_items.set(cart_items)
#                 payment.save()
                
#                 # Mark cart items as purchased
#                 cart_items.update(purchased=True)
                
#                 return redirect('payment_success')
#             except stripe.error.StripeError as e:
#                 return render(request, 'payment.html', {'form': form, 'error': str(e)})
#         return render(request, 'payment.html', {'form': form})

class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        order = Order.objects.get(user=self.request.user, ordered=False)
        context = {
            'form': form,
            'order': order
        }
        return render(self.request, 'checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                # TODO: add functionaly for these fields
                # same_billing_address = form.cleaned_data.get('same_billing_address')
                # save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')

                checkout_address = CheckoutAddress(
                    user=self.request.user,
                    street_address=street_address,
                    apartment_address=apartment_address,
                    country=country,
                    zip=zip
                )
                checkout_address.save()
                order.checkout_address = checkout_address
                order.save()

                if payment_option == 'S':
                    return redirect('core:payment', payment_option='stripe')
                elif payment_option == 'P':
                    return redirect('core:payment', payment_option='paypal')
                else:
                    messages.warning(self.request, "Invalid Payment option")
                    return redirect('core:checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("core:order-summary")