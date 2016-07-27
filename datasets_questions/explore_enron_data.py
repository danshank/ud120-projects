#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "There are %d people in the dataset" % len(enron_data)
print "There are %d attributes for each person" % len(enron_data[enron_data.keys()[0]])

count_poi = 0
for key in enron_data.keys():
	if enron_data[key]["poi"] == 1:
		count_poi = count_poi + 1

print "There are %d people of interest" % count_poi

print "James Prentice had a $%d total stock value" % enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Wesley Colwell sent %d emails to poi" % enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "Jeffery K Skilling exercised $%d of stock options" % enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Skilling took away $%d, Lay $%d, and Fastow $%d" % (enron_data["SKILLING JEFFREY K"]["total_payments"], enron_data["LAY KENNETH L"]["total_payments"], enron_data["FASTOW ANDREW S"]["total_payments"])

count_known_sal = 0
for key in enron_data.keys():
	if enron_data[key]["salary"] != 'NaN':
		count_known_sal = count_known_sal + 1

print "There are %d known salaries in the dataset" % count_known_sal

count_emails = 0
for key in enron_data.keys():
	if enron_data[key]["email_address"] != 'NaN':
		count_emails = count_emails + 1

print "There are %d emails in the dataset" % count_emails

count_no_payments = 0
for key in enron_data.keys():
	if enron_data[key]["total_payments"] == 'NaN':
		count_no_payments = count_no_payments + 1

print "There are %d people who have unknown total payments,\nthey represent %f percent of the data set" % (count_no_payments, float(count_no_payments) / len(enron_data) * 100)

count_nopay_poi = 0
for key in enron_data.keys():
	if enron_data[key]["total_payments"] == 'NaN' and enron_data[key]["poi"]:
		count_nopay_poi = count_nopay_poi + 1

print "%d poi have no info on their payments, this represents %% %f of the dataset" % (count_nopay_poi, 100 * float(count_nopay_poi) / len(enron_data))