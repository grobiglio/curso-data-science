from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np

# Gather data
boston_dataset = load_boston()
data = pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
features = data.drop(['INDUS', 'AGE'], axis=1)
log_prices = np.log(boston_dataset.target)
target = pd.DataFrame(log_prices, columns=['PRICE'])

CRIME_IDX = 0
ZN_IDX = 1
CHAS_IDX = 2
RM_IDX = 4
PTRATIO_IDX = 8

ZILLOW_MEDEAN_PRICE = 583.3
SCALE_FACTOR = ZILLOW_MEDEAN_PRICE / np.median(boston_dataset.target)

property_status = features.mean().values.reshape(1, 11)

regr = LinearRegression().fit(features, target)
fitted_vals = regr.predict(features)

MSE = mean_squared_error(target, fitted_vals)
RMSE = np.sqrt(MSE)

def get_log_estimate(nr_rooms,
                    students_per_clasroom,
                    next_to_river=False,
                    high_confidence=True):
    
    # Configure property
    property_status[0][RM_IDX] = nr_rooms
    property_status[0][PTRATIO_IDX] = students_per_clasroom
    
    property_status[0][CHAS_IDX] = next_to_river
    
    # Make prediction
    log_estimate = regr.predict(property_status)[0][0]
    
    # Calc Range
    if high_confidence:
        upper_bound = log_estimate + 2*RMSE
        lower_bound = log_estimate - 2*RMSE
        interval = 95
    else:
        upper_bound = log_estimate + RMSE
        lower_bound = log_estimate - RMSE
        interval = 68
        
    return log_estimate, upper_bound, lower_bound, interval

def convert_log_prices(log_price):
    
    price = np.e**log_price
    todays_price = round(price*SCALE_FACTOR*1000, -3)
    return todays_price

def get_dollar_estimate(rm, ptratio, chas=False, large_range=True):
    '''Estimate the price of a property in Boston.
    
    Keyword arguments:
    rm -- number of rooms in the property
    ptratio -- number of students per teacher in the classroom for the school in the area
    chas -- True if the property is next to the river, False otherwise
    large_range -- True for a 95% prediction interval, False for a 68% interval
    '''
    
    if rm < 1 or ptratio < 1:
        print('That is unrealistic. Try again.')
        return
    
    log_estimate, upper_bound, lower_bound, conf = get_log_estimate(nr_rooms=rm,
                                                                    students_per_clasroom=ptratio,
                                                                    next_to_river=chas,
                                                                    high_confidence=large_range)
    dollar_estimate = convert_log_prices(log_estimate)
    dollar_hi = convert_log_prices(upper_bound)
    dollar_low = convert_log_prices(lower_bound)

    print(f'The estimated property value is ${dollar_estimate}.')
    print(f'At {conf}% confidence the valuation range is')
    print(f'USD {dollar_low} at the lower end to USD {dollar_hi} at the high end.')