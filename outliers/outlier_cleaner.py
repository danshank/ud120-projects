#!/usr/bin/python
import numpy

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """    
    e2 = (net_worths - predictions)**2
    errors = net_worths - predictions
    #cleaned_data = numpy.array([ages, networths, errors])
    set_size = len(ages)

    ### your code goes here
    #for deletion in int(0.1 * set_size):
    #    index = numpy.argmax(cleaned_data, axis=1)[2]
    #    cleaned_data = numpy.delete(cleaned_data, index, axis = 1)

    cleaned_data = []

    for addition in range(int(0.9 * set_size)):
        index = numpy.argmin(e2)
        cleaned_data.append([ages[index], net_worths[index], errors[index]])
        ages = numpy.delete(ages, index)
        net_worths = numpy.delete(net_worths, index)
        errors = numpy.delete(errors, index)
        e2 = numpy.delete(e2, index)

    return cleaned_data

#a = np.arange(30).reshape(3, 10)
#print np.argmax(a, axis=1)[0]
#a = np.delete(a, 9, axis=1)
#print a

#a = numpy.arange(30).reshape(3, 10)
#print outlierCleaner(a[0], a[1], a[2])