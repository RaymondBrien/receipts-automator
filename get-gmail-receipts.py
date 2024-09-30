# # import gmail api

# # type 1 = Royal Cars receipts
# call gmail api

# get all emails from 'taxi' label

# filter by month

# filter by COMPLETED in the email description

# for each email:
#     extract relevant data:
#         valid date
#         valid time
#         valid amount
#         valid trasaction id
#         valid pickup location
#         valid dropoff location
#         valid time completed
        # ADD LOG associated with Provider/ROYAL CARS AND NOT UBER

#     save to royal_cars_{MONTH.YEAR}.csv (save to google drive too as backup?)

# # error handling
# all relevant fields are not Null
# check only within date ranage
# check no duplicates - via transaction id?
# confirm no 'booked' emails are included (only completed trips)


# import uber api
# handle creds

# # # type 2 = Ubers
# for each trip:
#     extract relevant data:
#         valid date
#         valid time
#         valid amount
#         valid trasaction id
#         valid pickup location
#         valid dropoff location
#         valid time completed
#         LOG AS UBER (not RoyalCars)
#
# Save to ubers_{MONTH.YEAR}.csv (save to google drive too as backup?)


# error handling
# all relevant fields are not Null
# check only within date ranage
# check no duplicates - via transaction id?
# handle any api call restrictions or auth errors

# global utility functions:
# count of trips per day
# confirm total number of trips for the month
# convert any date time into correct format
# convert any location data into long/lat?
# Merge uber and royal car csv files into one and save to drive
