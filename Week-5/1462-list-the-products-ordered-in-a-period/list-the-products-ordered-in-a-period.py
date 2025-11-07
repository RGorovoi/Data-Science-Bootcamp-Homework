import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders['order_date'] = pd.to_datetime(orders['order_date'])
    
    feb_orders = orders[(orders['order_date'].dt.year == 2020) & (orders['order_date'].dt.month == 2)]
    monthly_sales = feb_orders.groupby('product_id')['unit'].sum().reset_index()
    high_sales = monthly_sales[monthly_sales['unit'] >= 100]
    
    result_df = high_sales.merge(products[['product_id', 'product_name']],on='product_id',how='inner')[['product_name', 'unit']]
    return result_df
