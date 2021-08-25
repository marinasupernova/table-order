from datetime import date, datetime 
from django.shortcuts import render
from tables_reservations.models import Table, Reservation
from django.core.exceptions import ObjectDoesNotExist



def display_tables(request):
    if request.GET and request.GET['date_reservation']:
        date_reservation = request.GET['date_reservation']
    else:
        date_reservation = str(date.today())


    if request.POST and request.POST['table_number']:
        date_reservation = request.POST['date_reservation']
        try:
            reservation = Reservation.objects.get(table_number=request.POST['table_number'], date=date_reservation)
            reservation.delete()

        except ObjectDoesNotExist:
            print("The reservation doesn't exist.")
            new_reservation = Reservation(date=date_reservation, table_number=request.POST['table_number'])
            new_reservation.save()



    tables = Table.objects.all()
    reservations = Reservation.objects.filter(date=date_reservation)
    for reservation in reservations:
        for table in tables:
            if table.number == reservation.table_number:
                table.reserved_status = True
    year, month, day = date_reservation.split("-")
    context = {
        'tables': tables,
        'current_date': date_reservation,
        #'previous_day': (datetime.date(int(year), int(month), int(day)) - datetime.timedelta(1)).isoformat(),
        #'next_day': (datetime.date(int(year), int(month), int(day)) + datetime.timedelta(1)).isoformat()
    }

    return render(request, 'table_reservations.html', context)
