#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from matplotlib import pyplot as plt


# In[3]:


import pandas as pd


# In[42]:


#demand and supply for oil
quantity = [501.4, 306.5,184.9,148.9,11.4]
price_demand = [6, 15, 25, 35, 50]
price_supply = [50,35,25,15,6]

#plotting regression lines from scatter plots
plt.scatter(quantity,price_demand,linestyle='dotted', marker = '.',color='red')
plt.scatter(quantity,price_supply,linestyle='dotted', marker = '.',color='blue')

coefficients_1 = np.polyfit(quantity, price_demand, 1)
coefficients_2 = np.polyfit(quantity, price_supply, 1)
regression_line1 = np.polyval(coefficients_1, quantity)
regression_line2 = np.polyval(coefficients_2, quantity)

plt.legend(["Demand Curve","Supply Curve"])
plt.xlabel("Quantity of barrels")
plt.ylabel("Price per barrel(in millions USD)")
x_ticks = np.arange(0, 500, 50)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)

plt.title("Supply and Demand of Oil")

plt.plot(quantity, regression_line1, color='red')
plt.plot(quantity, regression_line2, color='blue')

#finding the point of intersection - Market Equilibrium
x_intersect = (coefficients_2[1] - coefficients_1[1]) / (coefficients_1[0] - coefficients_2[0])
y_intersect = coefficients_1[0] * x_intersect + coefficients_1[1]
plt.scatter(x_intersect, y_intersect, color='green', marker='o', label='Intersection')

print(x_intersect, y_intersect)

plt.show()


# In[43]:


eqm_quantity = x_intersect
eqm_price = y_intersect

print(eqm_quantity,eqm_price)


# In[44]:


#calculating total revenue generated in millions
eqm_revenue= eqm_price * eqm_quantity

print(eqm_revenue)


# In[58]:


#calculating ped
percent_change_quantity = (quantity[1] - quantity[0]) /quantity[0]
percent_change_price_demand = (price_demand[1] - price_demand[0]) / price_demand[0]

price_elasticity_demand = percent_change_quantity / percent_change_price_demand

print(price_elasticity_demand)


# In[40]:


#calculating pes
percent_change_quantity = (quantity[1] - quantity[0]) /quantity[0]
percent_change_price_supply = (price_supply[1] - price_supply[0]) / price_supply[0]

price_elasticity_supply = percent_change_quantity / percent_change_price_supply

print(price_elasticity_supply)


# In[49]:


#demand and supply for oil
quantity = [501.4, 306.5,184.9,148.9,11.4]
price_demand = [6, 15, 25, 35, 50]
price_demand_new = [11, 20, 30, 40, 55]
price_supply = [50,35,25,15,6]

#plotting regression lines from scatter plots
plt.scatter(quantity,price_demand,linestyle='dotted', marker = '.',color='red')
plt.scatter(quantity,price_supply,linestyle='dotted', marker = '.',color='blue')
plt.scatter(quantity,price_demand_new,linestyle='dotted', marker = '.',color='green')

coefficients_1 = np.polyfit(quantity, price_demand, 1)
coefficients_2 = np.polyfit(quantity, price_supply, 1)
coefficients_3 = np.polyfit(quantity, price_demand_new, 1)

regression_line1 = np.polyval(coefficients_1, quantity)
regression_line2 = np.polyval(coefficients_2, quantity)
regression_line3 = np.polyval(coefficients_3, quantity)

plt.legend(["Initial Demand Curve","Supply Curve","Final Demand Curve"])
plt.xlabel("Quantity of barrels")
plt.ylabel("Price per barrel(in millions USD)")
x_ticks = np.arange(0, 500, 50)  # Range from 2000 to 2022 with interval of 2
plt.xticks(x_ticks)

plt.title("Change in Demand for Oil")

plt.plot(quantity, regression_line1, color='red')
plt.plot(quantity, regression_line2, color='blue')
plt.plot(quantity, regression_line3, color='green')

#finding the point of intersection - Market Equilibrium
x_intersect_new = (coefficients_2[1] - coefficients_3[1]) / (coefficients_3[0] - coefficients_2[0])
y_intersect_new = coefficients_3[0] * x_intersect_new + coefficients_3[1]

plt.scatter(x_intersect_new, y_intersect_new , color='black', marker='o', label='New Equilibrium')

print(x_intersect_new, y_intersect_new)

plt.show()


# In[50]:


new_eqm_quantity = x_intersect_new
new_eqm_price = y_intersect_new

print(new_eqm_quantity,new_eqm_price)


# In[51]:


#calculating total revenue generated in millions
new_eqm_revenue= new_eqm_price * new_eqm_quantity

print(new_eqm_revenue)


# In[52]:


#change in total revenue due to change in demand

extraprofit = new_eqm_revenue - eqm_revenue

print(extraprofit)


# In[54]:


#calculating new PED
percent_change_quantity = (quantity[1] - quantity[0]) /quantity[0]
percent_change_price_demand_new = (price_demand_new[1] - price_demand_new[0]) / price_demand_new[0]

price_elasticity_demand_new = percent_change_quantity / percent_change_price_demand_new

print(price_elasticity_demand_new)


# In[59]:


#calculating change in PED

change_in_PED = abs(price_elasticity_demand_new) - abs(price_elasticity_demand)

print(change_in_PED)


# In[61]:


#change in quantity at new equillibrium

change_qty = new_eqm_quantity - eqm_quantity

print(change_qty)


# In[62]:


#change in price at new equillibrium

change_price = new_eqm_price - eqm_price

print(change_price)


# In[ ]:




