import boto3
from io import BytesIO
import pandas as pd


s3 = boto3.client("s3")
BUCKET = ""

def upload_to_s3(df , s3_key):

    buffer = BytesIO()
    df.to_parquet(buffer , index = False)
    s3.put_object(Bucket = BUCKET , key = s3_key , Body = buffer.getvalue())
    print(f"Uploaded : {s3_key}")



def ingest_partitioned(filepath , s3_folder , timestamp_col):
    df = pd.read_csv(filepath)
    df["year"]
    df["month"]
    
    pass



def ingest_flat(filepath , s3_folder):
    pass



# --- Partitioned ingestions ---
ingest_partitioned("archive/olist_orders_dataset.csv",        "orders",       "order_purchase_timestamp")
ingest_partitioned("archive/olist_order_reviews_dataset.csv", "order_reviews","review_creation_date")
ingest_partitioned("archive/olist_order_items_dataset.csv",   "order_items",  "shipping_limit_date")

# --- Flat ingestions ---
ingest_flat("archive/olist_customers_dataset.csv",              "customers")
ingest_flat("archive/olist_sellers_dataset.csv",                "sellers")
ingest_flat("archive/olist_products_dataset.csv",               "products")
ingest_flat("archive/olist_order_payments_dataset.csv",         "order_payments")
ingest_flat("archive/olist_geolocation_dataset.csv",            "geolocation")
ingest_flat("archive/product_category_name_translation.csv",    "product_category_translation")