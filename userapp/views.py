
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse, HttpResponse




from adminapp.models import approval
from doctorapp.models import registeration, userdiaganosis
from django.shortcuts import render, redirect
from django.urls import reverse
import stripe
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import schedule, booking, bookingitem, registeration


from doctorapp.views import *
def get_current_user(request):
    # Implement your logic to get the current user from the session or other means
    user_id = request.session.get('user_id')
    if user_id:
        return registeration.objects.get(id=user_id)
    return None
def userindex(request):
    print(request.user)
    return render(request,'user/index.html')
def doctorlist(request):
    doctor=schedule.objects.all()
    return render(request, 'user/ourdoctor.html', {'doctor': doctor})

def createbooking(request, scheduleid):
    bookings = get_object_or_404(schedule, id=scheduleid)

    # Assuming you have a way to get the current user from your custom model
    current_user = get_current_user(request)  # Implement this function based on your authentication logic

    if current_user:
        try:
            print(current_user)
            if bookings.numoftickets > 0:
                user_cart, created = booking.objects.get_or_create(user=current_user)
                print(f"user_cart: {user_cart}, created: {created}")
                print(f"bookings: {bookings}")

                cart_item, item_created = bookingitem.objects.get_or_create(book=user_cart, sch=bookings)
                print(f"cart_item: {cart_item}, item_created: {item_created}")


                if item_created:
                    bookings.numoftickets -= 1
                    print(f"Decrementing numoftickets: {bookings.numoftickets}")
                    bookings.save()
                messages.success(request,"Booking success")
                return redirect('userindex')


            else:
                messages.error(request, "No tickets available")
                return redirect('index')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('userindex')
    else:
        messages.error(request, "Please login to book tickets")
        return redirect('login')


def cancelbooking(request,bkid):
    current_user = get_current_user(request)
    can_booking = booking.objects.get(id=bkid)
    if current_user:
        if request.method == 'POST':
            can_booking.delete()
            return redirect('approvedbookings')

    return render(request, 'user/cancelbooking.html', {'can_booking': can_booking})

def approvedbookings(request):
    current_user = get_current_user(request)  # Implement this function based on your authentication logic

    if current_user:
        approvals = approval.objects.get(user_id=request.session.get('user_id'))

        # Get all booking items related to these bookings
        # Booking_items = bookingitem.objects.all()

        context = {
            'approvals': approvals,

        }

        return render(request, 'user/approvalsform.html', context)
def viewmedicine(request):
    current_user = get_current_user(request)  # Implement this function based on your authentication logic

    if current_user:
        medications = prescription.objects.get(presc_name_id=request.session.get('user_id'))

        # Get all booking items related to these bookings
        # Booking_items = bookingitem.objects.all()

        context = {
            'medications': medications,

        }

        return render(request, 'user/viewprescriptionform.html', context)
def userhome(request):
    return redirect('userindex')
def viewmediaganosis(request):
    current_user = get_current_user(request)  # Implement this function based on your authentication logic

    if current_user:
        diag = userdiaganosis.objects.get(diaganosis_name_id=request.session.get('user_id'))

        # Get all booking items related to these bookings
        # Booking_items = bookingitem.objects.all()

        context = {
            'diag': diag,

        }
        # return JsonResponse(context)
        return render(request, 'user/viewdiaganosis.html', context)
def viewbilling(request):
    current_user = get_current_user(request)  # Implement this function based on your authentication logic
    if current_user:
#
#

        diag = userdiaganosis.objects.get(diaganosis_name_id=request.session.get('user_id'))
        medications = prescription.objects.get(presc_name_id=request.session.get('user_id'))
        meds=medications.presc_num*medications.presc_med.price

        ticketcharge=150
        total=diag.test.price + meds + ticketcharge

        context = {
            'diag': diag,
            'medications':medications,
            'meds':meds,
            'ticketcharge':ticketcharge,
            'total':total,
             }

        return render(request, 'user/billing.html', context)





def create_checkout_session(request):
    # totalcost = viewbilling(request).get('total', 0)  # Default to 0 if 'total' key is missing
    current_user = get_current_user(request)  # Implement this function based on your authentication logic
    if current_user:
        #
        #

        diag = userdiaganosis.objects.get(diaganosis_name_id=request.session.get('user_id'))
        medications = prescription.objects.get(presc_name_id=request.session.get('user_id'))
        meds = medications.presc_num * medications.presc_med.price

        ticketcharge = 150
        total = diag.test.price + meds + ticketcharge

        stripe.api_key = settings.STRIPE_SECRET_KEY
    # if request.method == 'POST':
    # if totalcost:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'INR',
                        'product_data': {
                            'name': 'TotalAmount',  # Replace with your product name
                        },
                        'unit_amount': int(total * 100),
                    },
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('cancel')),
        )
        return redirect(session.url)






def success(request):
    #     cart_items = cartitem.objects.all()
    #     for cart_item in cart_items:
    #         product = cart_item.book
    #         if product.quantity >= cart_item.quantity:
    #             product.quantity -= cart_item.quantity
    #             product.save()
    #     cart_items.delete()

    return render(request, 'user/success.html')
    #
def cancel(request):
    return render(request, 'user/cancel.html')

