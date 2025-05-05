import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Create a Streamlit dashboard
st.title('Blinkit Data Analysis')

# Load the dataset
df = pd.read_csv('blinkit_data.csv')

# Display the dataset
st.header('Data Overview')
st.dataframe(df)

# Data Cleaning
df['Item Fat Content'] = df['Item Fat Content'].replace({'LF': 'Low Fat', 'low fat': 'Low Fat', 'reg': "Regular"})

# Calculate and display KPIs
st.header('Sales Key Performance Indicators (KPIs)')
# Total Sales
total_sales = df['Sales'].sum()
# Average Sales
avg_sales = df['Sales'].mean()
# No of items sold
no_of_items_sold = df['Sales'].count()
# Average Rating
avg_rating = df['Rating'].mean()
# Display KPIs
st.write(f'Total Sales: ${total_sales: .2f}')
st.write(f'Average Sales: ${avg_sales: .2f}')
st.write(f'Total number of items sold: {no_of_items_sold: .0f}')
st.write(f'Average Rating: {avg_rating: .2f}')

# 1st insight
st.header('What is the affect of amount of fat present in food on sales?')
sales_by_fat = df.groupby('Item Fat Content')['Sales'].sum()

plt.figure(figsize = (4, 4))
plt.pie(sales_by_fat, labels = sales_by_fat.index, autopct = '%.2f%%', startangle = 90)
plt.title('Sales by Fat Content')
st.pyplot(plt)

st.write("The pie chart shows the distribution of sales based on the fat content of items. It indicates that 'Low Fat' items have a significant share of total sales, while 'Regular' items have a smaller share. This suggests that consumers may prefer low-fat options, which could be a valuable insight for product development and marketing strategies.")
st.subheader('Business Recommendation')
st.write('1. Consider expanding the range of Low Fat products or offering Low Fat alternatives to popular Regular items.')
st.write('2. Use this insight to target health-conscious marketing campaigns and promotions.')
st.write('3. Explore customer feedback or reviews for Regular products to understand potential barriers.')

# 2nd insight
st.header('Which item types generate the highest sales across all outlets?')
sales_by_item_type = df.groupby('Item Type')['Sales'].sum().sort_values(ascending = False)

plt.figure(figsize = (8, 4))
bars = plt.bar(sales_by_item_type.index, sales_by_item_type.values)
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.xlabel('Item Type')
plt.ylabel('Sales')
plt.title("Sales by Item Type")
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height(): .0f}', ha='center', va='bottom', fontsize=6.5)
st.pyplot(plt)

st.write('The bar chart shows the total sales for each item type. It indicates that "Fruits and Vegetables" generate the highest sales, followed by "Snack Foods" and "Household" items. This insight can help in inventory management and marketing strategies, focusing on high-selling categories.')
st.subheader('Business Recommendation')
st.write('1. Consider increasing inventory, promotions, or visibility for high-selling items to capitalize on demand.')
st.write('2. Investigate why certain categories like Seafood and Breakfast underperform — could be due to supply chain issues, price sensitivity, or customer preferences.')
st.write('3. Use high-performing items as anchor products for cross-selling lower-performing categories.')

# 3rd insight
st.header('How does item fat content affect sales across item types?')
grouped = df.groupby(['Item Type', 'Item Fat Content'])['Sales'].sum().unstack()

ax = grouped.plot(kind='bar', figsize=(8,5), title='Sales by Item Type and Fat Content')
plt.xlabel('Item Type')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.ylabel('Total Sales')
plt.legend(title='Item Fat Content')
plt.tight_layout()
st.pyplot(plt)

st.write('The bar chart shows the total sales for each item type, segmented by fat content. It indicates that "Low Fat" items generally outperform "Regular" items across most categories. This suggests a strong consumer preference for low-fat options, which could inform product development and marketing strategies.')
st.subheader('Business Recommendation')
st.write('1. Businesses should expand Low Fat offerings in high-performing categories.')
st.write('2. For categories with strong Regular sales (like Baking Goods), maintain product variety while experimenting with healthier options.')
st.write('3. Marketing campaigns should emphasize Low Fat benefits especially in household essentials and snacks.')

# 4th insight
st.header('Are newer outlets performing better or worse than older ones?')
establishment_sales = df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()

plt.figure(figsize = (8, 4))
sns.lineplot(x=df['Outlet Establishment Year'], y=establishment_sales, marker='o', markersize=8)
plt.xlabel('Outlet Establishment Year')
plt.ylabel('Sales')
plt.title('Total Sales by Outlet Establishment')
st.pyplot(plt)

st.write('The line chart shows the total sales for each outlet establishment year. It indicates that newer outlets (established in 2010 and later) generally outperform older ones, suggesting that newer locations may be better positioned to meet customer needs or have more effective marketing strategies.')
st.subheader('Business Recommendation') 
st.write('1. While newer outlets (2010–2015) didn’t outperform older ones, outlets opened after 2015 did significantly better, which might point to recent strategic improvements.')
st.write('2. Investigate what changed in 2020 (e.g., product mix, store size, location strategy, consumer trends')

# 5th insight
st.header('How does outlet type or size influence sales performance?')
establishment_size_sales = df.groupby('Outlet Size')['Sales'].sum()

plt.figure(figsize=(6,6))
plt.pie(establishment_size_sales, labels=establishment_size_sales.index, colors=sns.color_palette('pastel'), autopct='%.1f%%', startangle=90)
plt.title('Sales by Outlet Size')
plt.legend(establishment_size_sales.index)
st.pyplot(plt)

st.write('The pie chart shows the distribution of sales based on outlet size. It indicates that "Medium" and "Small" outlets have a significant share of total sales, while "High" outlets have a smaller share. This suggests that smaller outlets may be more effective in certain markets or product categories.')
st.subheader('Business Recommendation')
st.write('Consider expanding the number of Medium and Small outlets in high-performing areas.')


outlet_type_sales = df.groupby('Outlet Type')['Sales'].sum()

plt.figure(figsize=(8,5))
plt.pie(outlet_type_sales, labels=outlet_type_sales.index, autopct='%.2f%%', startangle=90)
plt.title('Sales by Outlet Type')
st.pyplot(plt)

st.write('The pie chart shows the distribution of sales based on outlet type. It indicates that "Supermarket Type1" generates the highest sales, followed by "Grocery Store" and "Supermarket Type3". This insight can help in inventory management and marketing strategies, focusing on high-selling outlet types.')
st.subheader('Business Recommendation') 
st.write('1. Consider increasing inventory, promotions, or visibility for high-selling outlet types to capitalize on demand.')
st.write('2. Investigate why certain outlet types underperform — could be due to location, product mix, or customer preferences.')
st.write('3. Use high-performing outlet types as anchor locations for cross-selling lower-performing types.')

# 6th insight
st.header('Do certain outlet locations (Tier 1, Tier 2, Tier 3) see higher average sales?')
location_sales = df.groupby('Outlet Location Type')['Sales'].sum()

plt.figure(figsize=(8,5))
plt.pie(location_sales, labels=location_sales.index, autopct='%.2f%%', startangle=90)
plt.title('Sales by Outlet Location')
st.pyplot(plt)

st.write('The pie chart shows the distribution of sales based on outlet location type. It indicates that "Tier 3" locations generate the highest sales, followed by "Tier 2" and "Tier 1". This insight can help in inventory management and marketing strategies, focusing on high-selling outlet locations.')
st.subheader('Business Recommendation')
st.write('1. Consider increasing inventory, promotions, or visibility for high-selling outlet locations to capitalize on demand.')
st.write('2. Investigate why certain outlet locations underperform — could be due to location, product mix, or customer preferences.') 
st.write('3. Use high-performing outlet locations as anchor locations for cross-selling lower-performing locations.')

# 7th insight
st.header('Does item weight have any correlation with sales?')
item_weight_sales_correlation = df[['Item Weight', 'Sales']].corr().iloc[0, 1]
st.markdown(f'Correlation between Item Weight and Sales: **{item_weight_sales_correlation:.2f}**')
st.write('The correlation coefficient indicates a weak positive correlation between item weight and sales, suggesting that heavier items may not necessarily lead to higher sales. This insight can inform product development and marketing strategies.')

# 8th insight
st.header('Which combination of outlet size and type yields the best sales results?')
outlet_sales = df.groupby(['Outlet Size', 'Outlet Type'])['Sales'].sum().reset_index()
outlet_sales_sorted = outlet_sales.sort_values(by='Sales', ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x='Sales', y='Outlet Type', hue='Outlet Size', data=outlet_sales_sorted, palette='viridis')
plt.title('Best Sales by Outlet Size and Type')
plt.xlabel('Total Sales')
plt.ylabel('Outlet Type')
st.pyplot(plt)

st.write('The bar chart shows the total sales for each outlet type, segmented by outlet size. It indicates that "Supermarket Type1" and "Medium" outlets generate the highest sales, while "Supermarket Type3" and "Small" outlets have lower sales. This suggests that certain combinations of outlet type and size may be more effective in driving sales.')