import collections
from sklearn import linear_model
import numpy as np
import pandas as pd
import time
from tqdm import tqdm


#
# Hard-coded constants
#
MATERIAL_COSTS = {'carat_9k': 14.62, 'carat_10k': 15.70, 'carat_14k': 21.75}

#
# Data Structures
#
MaterialProfile = collections.namedtuple("MaterialProfile", field_names=['weight', 'unit_cost'])
Product = collections.namedtuple("Product", field_names=['jeweler', 'product_class', 'price', 'cost'])

#
# Helpers
#
def material_cost(material):
    """Return material cost."""
    return material.weight * material.unit_cost
    
#
# Inference
#
# This section contains code for inferring relevant parameters based on market data.
# This is the machine learning component of the app.
# 

class MarketParameters:
    """Struct containing regression parameters for inferring pricing algorithm."""
    def __init__(self, alpha_likes, alpha_followers, alpha_constant):
        self.alpha_likes = alpha_likes
        self.alpha_followers = alpha_followers
        self.alpha_constant = alpha_constant      


def _get_material_cost_from_row_data(row_data):
    m = MaterialProfile(unit_cost=MATERIAL_COSTS[row_data['carat']], 
                        weight=row_data['weight'])
    return material_cost(m)
       

def _get_x(row_data):
    """Return features (x) for single training example in dataframe."""
    return [row_data['likes'], row_data['followers']]


def _get_y(row_data):
    """Return response (y) for single training example in dataframe."""
    return row_data['price'] - _get_material_cost_from_row_data(row_data)


def generate_market_data_for_product_class(market_data_df, product_class_identifier):
    """Infer market parameters based on product class.
    
    :param market_data: dataframe of jewelery market
    :param product_class: type of product class for filter condition
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


def train_model(market_data_df):
    # for i in tqdm(range(10000), desc="training_model"): time.sleep(0.0005)
    return get_fitted_pricing_model_for_product_class(market_data_df, product_class_identifier="ring")

#
# Optimization
# 
def knapsack(products, budget):
    """Implement knapsack algorithm for portfolio optimization."""
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


def generate_pricing_using_model(user_data, model):
    """Generate pricing data.

    :param user_data: dataframe containing user product collection
    :param model: pricing model (ML)
    """
    products = []

    # populate product prices
    for (_, row_data) in user_data.iterrows():
        x = np.asarray(_get_x(row_data)).reshape((2)).reshape(1, 2)

        influence_corrected_price = model.predict(x)[0]
        baseline_cost = _get_material_cost_from_row_data(row_data)
        recommended_price = influence_corrected_price + baseline_cost

        products.append(
            Product(jeweler=row_data['jeweler_name'],
                    product_class=row_data['product_class'],
                    price=recommended_price,
                    cost=baseline_cost))

    return products


def display_hackathon_results(products, optimized_portfolio):
    """For demo purposes."""

    print "\n AI-generated pricing model...\n"
    for idx, p in enumerate(products):
        print "{} Product[{}]({}), Baseline Cost: {}, AI-recommended price: {}".format(p.jeweler, idx, p.product_class, p.cost, p.price)
    
    optimal_index_allocation, _ = optimized_portfolio
    total_cost = sum([number*products[i].cost for (i, number) in enumerate(optimal_index_allocation)])
    total_revenue = sum([number*products[i].price for (i, number) in enumerate(optimal_index_allocation)])
    total_profit = total_revenue - total_cost

    print "\n Optimized Portfolio...\n"
    for idx, number_of_products in enumerate(optimal_index_allocation):
        print "{} Product[{}]({}): {} items".format(p.jeweler, idx, p.product_class, number_of_products)
    print "\n"
    print "Total Budget: {}".format(total_cost)
    print "Total Revenue: {}".format(total_revenue)
    print "Total Profit: {}".format(total_profit)
    print "\n"



def main():
    """Example of how to run code."""

    # Load market data
    market_data_df = pd.read_csv("jewlery_marketplace_data.csv", header=0)
    user_product_collection_df = pd.read_csv("nathalie_marketplace_data.csv", header=0)
    product_class_identifier = "ring"

    # Machine learning for pricing model
    model = train_model(market_data_df)
    products = generate_pricing_using_model(user_product_collection_df, model)

    # Optimize portfolio of jewlery offerings
    optimized_portfolio = knapsack(products, budget=300)

    # Product demo
    display_hackathon_results(products, optimized_portfolio)


if __name__ == "__main__":
    main()
