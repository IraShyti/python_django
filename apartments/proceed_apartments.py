from .models import Apartment


def proceed_apartments(apartment_data):
    # CHECK IF APARMENT IS IN DB

    apartment = Apartment.objects.get(id=apartment_data['id'])

    if apartment:
        # UPDATE APARTMENT
        data = Apartment(id=apartment_data['id'], city=apartment_data['city'],
                         street=apartment_data['street'],
                         deleted=apartment_data['deleted'],
                         shower=apartment_data['shower'],
                         bathtub=apartment_data['bathtub'],
                         microwave=apartment_data['microwave'],
                         balcony=apartment_data['balcony'],
                         water_included=apartment_data['water_included'],
                         heating_included=apartment_data['heating_included'])
        apartment = data
        apartment.save()
        pass
    else:
        # ADD NEW APARTMENT
        data = Apartment.objects.create(id=apartment_data['id'], city=apartment_data['city'],
                                     street=apartment_data['street'],
                                    deleted=apartment_data['deleted'],
                                    shower=apartment_data['shower'],
                                    bathtub=apartment_data['bathtub'],
                                    microwave=apartment_data['microwave'],
                                    balcony=apartment_data['balcony'],
                                    water_included=apartment_data['water_included'],
                                    heating_included=apartment_data['heating_included'])

        data.save(force_insert=True)




