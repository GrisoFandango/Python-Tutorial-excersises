# How to configure and use API, in this example from YELP
# We need the requests pK
import requests
# We send a request to the endpoint that we need
url = "https://api.yelp.com/v3/businesses/search"
api_key = "ajwmaSgBbXKdVfYqmRNFMgASSZTmC1sniamwIzkwaS9Q8RMNCAAPCWfQMQA_nWb1LLe8kwImkO_MdDB4Eq8tYV1bS8t7ggS3ReUydJaj9Kla7b5uMhnW8z3tHy_VXXYx"
# We need to create the headers library where to store the api_key
headers = {
    "Authorization": "Bearer " + api_key
}
# In this case the Yelp end point require a location as a parameter
params = {
    "term": "barber",  # we can fileter
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)

# print(response.text)
# because the result given in a jason object we can store it in this way
# The json attribute convert the result in a dictionary, the key businesses in the one that we got on top of the printed result
businesses = response.json()["businesses"]
# the output is a list of directiories where we can find key as ID,alias, name
# print(businesses)
# now becuase is a list, we can iterate over it to extract the data from a key that we want

# for business in businesses:
#     print(business["name"])

# we can use list comprhension to obtain a list of barber rated over 4.5
# we use the syntax [item for item in list]
# our list is businesses (row 21)
# each item is a business (the one after for) that is a dictionary

name = [business["name"]
        for business in businesses if business["rating"] >= 4.5]
print(name)
