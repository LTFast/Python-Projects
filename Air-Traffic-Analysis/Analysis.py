"""
Various analytics questions for air traffic analysis
"""
import pandas as pd

# Read and preview the air traffic data
airTrafficData = pd.read_csv("Cleaned_2018_Flights.csv")

# Preview the first 5 rows
# print(airTrafficData.head())

# Display the available fields
print("Available Columns")
print(list(airTrafficData.columns))

"""
   1. Display the top 3 companies with the highest averaged ticket prices
"""
# # Subset the dataframe
# company_price_data = airTrafficData[['AirlineCompany','PricePerTicket']]
# # Group prices as the mean price per Airline Company
# group_prices_per_company = company_price_data.groupby(['AirlineCompany']).mean()
# # Find the top 3 companies with the highest mean ticket prices
# top_3_mean_ticket_prices = group_prices_per_company.nlargest(3, 'PricePerTicket')
# # Format the prices
# top_3_mean_ticket_prices['PricePerTicket'] = top_3_mean_ticket_prices['PricePerTicket'].map('${:,.2f}'.format)
# print(top_3_mean_ticket_prices)

"""
Output:

AirlineCompany               
HA                    $309.56
UA                    $286.16
AA                    $274.18
"""

"""
   2. Find the most frequented routes (Departure -> Destination)
"""
# # Subset the data to contain only origin and destination
# arrival_dest_data = airTrafficData[['Origin','Dest']]
# # Group counts by Origin, Destination pair
# arrival_dest_data = arrival_dest_data.groupby(['Origin', 'Dest']).Dest.agg('count').to_frame('Count').reset_index()
#
# highest_count = arrival_dest_data['Count'].max()
# print("Route with the highest number of flights")
# print(arrival_dest_data[arrival_dest_data['Count'] == highest_count])
"""
Output: 

     Origin Dest  Count
4017    LAX  JFK  26232
"""

"""
   3. Quarter with the most number of most coupons in the market
"""
# Subset the data frame to contain Quart and Market Coupon fields
coupon_quarter_data = airTrafficData[['Quarter', 'MktCoupons']]
# Number of Market Coupons each Quarter
coupon_sum_per_company = coupon_quarter_data.groupby(['Quarter']).sum()

print("Quarter with the most coupons in the market:")
print(coupon_sum_per_company.loc[coupon_sum_per_company['MktCoupons']==coupon_sum_per_company['MktCoupons'].max()])
"""
Output
Quarter  MktCoupons 
4           2626683
"""











