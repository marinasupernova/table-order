import datetime 
from django.shortcuts import render
from tables_reservations.models import Table, Reservation
from django.core.exceptions import ObjectDoesNotExist



def display_tables(request):
    if request.GET and request.GET['date_reservation']:
        date_reservation = request.GET['date_reservation']
    else:
        date_reservation = str(datetime.date.today())


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

    context = {
        'tables': tables,
        'current_date': date_reservation,
        'previous_date': (datetime.datetime.fromisoformat(date_reservation) - datetime.timedelta(1)).isoformat()[:-9],
        'next_date':     (datetime.datetime.fromisoformat(date_reservation) + datetime.timedelta(1)).isoformat()[:-9]
    }

    return render(request, 'table_reservations.html', context)

# 2021-08-23T00:00:00 => 2021-08-23
# str[:-8]