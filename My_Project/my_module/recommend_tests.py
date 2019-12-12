#!/usr/bin/env python
# coding: utf-8

# In[5]:


import recommend_functions as rec


# In[10]:


def test_unique_cat():
    
    assert callable(search)
    
    results = search(API_URL, API_KEY, 'restaurant', "San Diego")
    
    assert callable(get_categories)
    
    categories = get_categories(results)
    
    s = set()
    for element in categories:
        s.add(element)
    
    assert len(s) == len(categories)

