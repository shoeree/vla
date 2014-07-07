'''
Utilities for loading info from CSV files.
'''
import csv
from volition.models import Volunteer

CSV_COLS = {
    'first_name': 0,
    'last_name': 1,
    'comments': 3,
    'email': 4,
    'phone': 5,
    'address_house': 6,
    'address_city': 7,
    'address_postal': 8,
}

def load_volunteers_from_csv(csv_file_name):
    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        row_ind = 0
        for row in csv_reader:
            if row_ind == 0:
                row_ind += 1
                continue
            # Extract the Volunteer info
            last_name = row[CSV_COLS['last_name']]
            first_name = row[CSV_COLS['first_name']]
            email = row[CSV_COLS['email']]
            phone = row[CSV_COLS['phone']]
            address_house = row[CSV_COLS['address_house']]
            address_city = row[CSV_COLS['address_city']]
            address_postal = row[CSV_COLS['address_postal']]
            comments = row[CSV_COLS['comments']]

            if len(last_name) > 0 and len(first_name) > 0:
                volunteer, created = Volunteer.objects.update_or_create(
                    last_name = last_name,
                    first_name = first_name,
                    email = email,
                    phone = phone,
                    address_house = address_house,
                    address_city = address_city,
                    address_postal = address_postal,
                    comments = comments
                )

                if created:
                    # new Volunteer was created
                    volunteer.is_active = False
                    print "Created a new Volunteer: %s" % volunteer
                else:
                    print "Updated existing Volunteer: %s" % volunteer
            else:
                print "Ignoring bad row %d:\n\t%s" % (row_ind, row)

            row_ind += 1

