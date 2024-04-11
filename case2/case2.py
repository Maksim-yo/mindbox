from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, explode_outer

spark = SparkSession.builder.getOrCreate()
df_json = spark.read.option("multiline","true").json("data.json")

df_categories = df_json.select(explode('Categories').alias('Category')).select('Category.id', 'Category.name')

df_products = df_json.select(explode("Products").alias('Product')) \
    .select('Product.name', explode_outer('Product.categories').alias('category'))


products_with_category = df_products.join(df_categories, df_categories.id == df_products.category, how="inner")
products_without_category = df_products.join(df_categories, df_categories.id == df_products.category, how="left_anti")

products_with_category_df = products_with_category.select(df_products.name, df_categories.name)
products_without_category.show()
products_with_category_df.show()
