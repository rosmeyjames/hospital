from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from adminapp.models import approval
from doctorapp.models import registeration
from userapp.models import booking, bookingitem
from .models import approval, booking, registeration
def adminindex(request):
    return render(request, 'admin/index.html')





def bookingapproval(request):
    if request.method == 'POST':
        bkid = request.POST.get('bookingid')
        username = request.POST.get('username')
        bkdate = request.POST.get('bkdate')
        cons_date = request.POST.get('cons_date')

        # Debug: Print the received form data
        print(f"Booking ID: {bkid}, Username: {username}, Booking Date: {bkdate}, Consultation Date: {cons_date}")

        # Fetch the related Booking and Registeration objects
        try:
            Booking = booking.objects.get(id=bkid)
            user = registeration.objects.get(username=username)
        except booking.DoesNotExist:
            # Handle the case where the booking does not exist
            return render(request, 'index.html', {'error': 'Booking not found'})
        except registeration.DoesNotExist:
            # Handle the case where the user does not exist
            return render(request, 'index.html', {'error': 'User not found'})

        # Debug: Print the fetched objects
        print(f"Fetched Booking: {Booking}, Fetched User: {user}")

        # Create and save the Approval object
        try:
            acd = approval(books=Booking, user=user, bkngdate=bkdate, cnsultdate=cons_date)
            acd.save()
            # Debug: Print success message
            print("Approval object saved successfully")
        except Exception as e:
            # Debug: Print the exception message
            print(f"Error saving Approval object: {e}")
            return render(request, 'admin/index.html', {'error': 'Error saving approval'})

        # Redirect to a success page or another view
        return redirect('viewallbookings')  # Replace 'success_page' with your actual success page URL name

    return render(request, 'admin/viewbookingdetails.html')

# def bookingapproval(request):
#     if request.method == 'POST':
#         bkid = request.POST.get('bookingid')
#         username = request.POST.get('username')
#         bkdate = request.POST.get('bkdate')
#         cons_date = request.POST.get('cons_date')
#
#         # Fetch the related Booking and Registeration objects
#         try:
#             Booking = booking.objects.get(id=bkid)
#             user = registeration.objects.get(username=username)
#         except booking.DoesNotExist:
#             # Handle the case where the booking does not exist
#             return render(request, 'index.html', {'error': 'Booking not found'})
#         except registeration.DoesNotExist:
#             # Handle the case where the user does not exist
#             return render(request, 'adminindex.html', {'error': 'User not found'})
#
#         # Create and save the Approval object
#         acd = approval(books=Booking, user=user, bkngdate=bkdate, cnsultdate=cons_date)
#         acd.save()
#
#         # Redirect to a success page or another view
#         # return redirect('success_page')  # Replace 'success_page' with your actual success page URL name
#
#     return render(request, 'index.html')





def view_all_bookings(request):
    # Get all booking objects
    Bookings = booking.objects.all()

    # Get all booking items related to these bookings
    Booking_items = bookingitem.objects.all()

    context = {
        'Bookings': Bookings,
        'Booking_items': Booking_items,
    }

    return render(request, 'admin/viewbookingdetails.html', context)


# Create your views here.
