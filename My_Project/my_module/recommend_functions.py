#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests

from random import randint


# In[2]:


API_KEY= '_axJRffwq6smSqC34oVV4shz-8B8Yj4qIUniLyPJoMxH4C7QrKmxE8BJFe627O5unS2U2naCDx8lY9PnTKerwUTs4Tdi0SFPLMgZc0WRORX6ddkBUiIO1cZKtIjxXXYx'
API_URL = 'https://api.yelp.com/v3/businesses/search'


# In[3]:


def request(url, api_key, url_param = None):
    '''
    API token, needed to authenticate Yelp API, got the actual code from the website stated below(not mine):
    https://python.gotrained.com/yelp-fusion-api-tutorial/
    '''   
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }
    
    #API call
    response = requests.request('GET', url, headers=headers, params = url_param)
    return response.json()


# In[4]:


def search(url, api_key, term, location): 
    '''
    start point for recommendations, area of access
    
    parameters
    ----------
    requests is the api query but search is like the interface for it
    where term is 'retaurants' and location is the inputed city
    
    returns
    -------
    requests
    '''
    sort_pref = ['best_match', 'rating', 'review_count', 'distance']
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': 50,
        'radius': 4000, #in meters - 25000m = 25mi
        'price': "1",
        'sort_by': sort_pref[randint(0,3)], #random sort-by selection
    }
    return request(url, api_key, url_param = url_params)

def get_categories(restaurants):
    '''
    finds unique categories in area
    '''
    unique = []
    for i in restaurants['businesses']:
        unique.append(i['categories'][0]['title'])
    unique = list(set(unique))
    
    #categories array
    categories = [[] for i in range(len(unique))]
    for i in range(len(unique)):
        categories[i].append(unique[i])

    #Sort restaurants by their category
    for i in range(len(restaurants['businesses'])):

        for j in range(len(categories)):
            if (restaurants['businesses'][i]['categories'][0]['title'] == categories[j][0]):
                categories[j].append(i)
    return categories

def generate_nonfactor(categories):
    '''
    chooses an increment so that the recommendations dont repeat categories
    '''

    length = len(categories)
    
    while True:
        x = randint(2, length)
        if length % x != 0:
            return x
        
def recommend(categories, results):
    #remove_category = False
    increment = generate_nonfactor(categories)
    initial = randint(0, len(categories) - 1)
    
    if(len(categories[initial]) > 1):
        return categories[initial][0], results['businesses'][categories[initial].pop()]
    
    else:
        #remove category 
        remove_category(categories,categories[initial][0])
        intial = (initial+increment) % len(categories) -1 
        
def remove_category(categories, cat_to_remove):
    print(len(categories))

    for i in range(len(categories)):
        if categories[i][0] == cat_to_remove:
            del categories[i]
            break
            
    return False

