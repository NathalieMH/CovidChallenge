import csv
import sys
import io

# checks whether the first columns of two files contain identical elements
# prints out any elements which were found in the second file (edit file), but were not found in the first file (base file)
if __name__ == "__main__":
    print('starting script...')

    base_file = open(sys.argv[1])   # file with correct format 
    edit_file = open(sys.argv[2])   # file with the format that might need to be adjusted to fit the base file's format

    csv_base = csv.reader(base_file, delimiter=',')
    csv_edit = csv.reader(edit_file, delimiter=',')

    # build country set
    country_set = set()
    for row in csv_base:
        country_set.add(row[0])

    # check if edit_file contains any countries not in country_set
    not_in_base = set()

    for row in csv_edit:
        if not (row[0] in country_set):
            not_in_base.add(row[0])

    print('these country names are not in the base file: ')
    for country in not_in_base:
        print("- " + country)

