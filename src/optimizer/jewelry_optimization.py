
# coding: utf-8

# # Jewelery Pricing algorithms
# This is a python notebook that contains code regarding how we should price our jewlery.

# In[57]:

import collections
from sklearn import linear_model
import numpy as np
import pandas as pd


from . import api_rest

# # DATA
# This section contains data that we need to collect.

# In[86]:

# Read hard-coded data inputs from CSV
market_data_df = pd.read_csv("market_data.csv", header=0)
user_product_collection_df = pd.read_csv("user_product_collection_data.csv", header=0)

# Encode material costs
MATERIAL_COSTS = {'gold': {'carat_9k':10.0, 'carat_10k': 20.0, 'carat_14k': 30.0}}


# # Data Structures
# This section defines data structures for computing values.

# In[135]:

# Define data structures
JewelerProfile = collections.namedtuple(typename="JewelerProfile", field_names=['name', 'hourly_rate', 'influence_score', 'product_line'])
MaterialProfile = collections.namedtuple("MaterialProfile", field_names=['weight', 'unit_cost'])
Product = collections.namedtuple("Product", field_names=['jeweler', 'product_class', 'price', 'cost'])

class PRODUCT_CLASS:
    GOLD_RING = "gold"


# # Costs

# In[ ]:

#
# Cost functions
#
def material_cost(material):
    """Return material cost."""
    return material.weight * material.unit_cost
    
def product_cost(product, jeweler_profile):
    """Price of product in terms of material composition."""
    return sum([material_cost(m) for m in product.material_composition])

#
# Finance questions
#
def revenue(product, jeweler_profile):
    """Price jeweler charges for product."""
    return labor_fee(product, jeweler_profile) + product_cost(product, jeweler_profile)
    
def profit(product, jeweler_profile):
    return revenue(product, jeweler_profile) - product_cost(product, jeweler_profile)


# # Inference
# This section contains code for inferring relevant parameters based on market data.

# In[164]:

def _get_material_cost_from_row_data(row_data):
    m = MaterialProfile(unit_cost=MATERIAL_COSTS[row_data['material_name']][row_data['carat']], 
                           weight=row_data['weight'])
    return material_cost(m)
        
def _get_x(row_data):
    """Return features (x) for single training example in dataframe."""
    return [row_data['likes'], row_data['followers']]
    
def _get_y(row_data):
    """Return response (y) for single training example in dataframe."""
    return row_data['price'] - _get_material_cost_from_row_data(row_data)

class MarketParameters:
    """Struct containing regression parameters for inferring pricing algorithm."""
    def __init__(self, alpha_likes, alpha_followers, alpha_constant):
        self.alpha_likes = alpha_likes
        self.alpha_followers = alpha_followers
        self.alpha_constant = alpha_constant      

def generate_market_data_for_product_class(market_data_df, product_class_identifier):
    """Infer market parameters based on product class.
    
    :param market_data: dataframe of jewelery market
    :param product_class: PRODUCT_CLASS enum indicating filter condition
    """
    product_df = market_data_df[market_data_df['product_class'] == product_class_identifier]
    X = np.asarray([_get_x(row_data) for (_, row_data) in product_df.iterrows()])
    Y = np.asarray([_get_y(row_data) for (_, row_data) in product_df.iterrows()])
    return X, Y

def get_fitted_pricing_model_for_product_class(market_data_df, product_class_identifier):
    X, Y = generate_market_data_for_product_class(market_data_df, product_class_identifier)
    model = linear_model.LinearRegression()
    model = model.fit(X, Y)
    return model


# In[ ]:




# # Script
# This runs the program.

# In[139]:

# Read hard-coded data inputs from CSV
market_data_df = pd.read_csv("market_data.csv", header=0)
user_product_collection_df = pd.read_csv("user_product_collection_data.csv", header=0)


# In[106]:

market_data_df


# In[140]:

user_product_collection_df


# In[151]:




# In[161]:

@api_rest.route('/compute_portfolio/<budget>', methods=['GET'])
def knapsack(products, budget):
    n = len(products)

    profit_memo = [0 for i in range(budget + 1)] 
    product_memo = [[0 for i in range(n)] for j in range(budget + 1)]

    for i in range(budget + 1): 
        for j in range(n): 
            if (products[j].cost <= i):
                removed_product_index = i - int(products[j].cost)
                product_profit = profit_memo[removed_product_index] + products[j].price
                profit_memo[i] = max(profit_memo[i], product_profit)

                if product_profit == profit_memo[i]:
                    product_memo[i] = product_memo[removed_product_index]
                    product_memo[i][j] += 1

    return product_memo[budget], profit_memo[budget]


# In[166]:

product_class_identifier = "ring"
pricing_model = get_fitted_pricing_model_for_product_class(market_data_df, product_class_identifier="ring")
product_df = market_data_df[market_data_df['product_class'] == product_class_identifier]

products = []
for (_, row_data) in user_product_collection_df.iterrows():
    x = np.asarray(_get_x(row_data)).reshape((2)).reshape(1, 2)
    products.append(
        Product(jeweler=row_data['jeweler_name'],
                product_class=row_data['product_class'],
                price=pricing_model.predict(x)[0],
                cost=pricing_model.predict(x)[0] - _get_material_cost_from_row_data(row_data)))
    
print knapsack(products, budget=11)


# In[153]:

print products


# In[ ]:



