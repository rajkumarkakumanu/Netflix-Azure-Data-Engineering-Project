# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

df = spark.read.format("delta")\
         .option("header", True)\
        .option("inferSchema", True)\
        .load("abfss://bronze@netflixadlsraj.dfs.core.windows.net/netflix_titles")

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.fillna({"duration_minutes":0, "duration_seasons":1})
df.display()

# COMMAND ----------

df = df.withColumn("duration_minutes", col("duration_minutes").cast(IntegerType()))\
       .withColumn("duration_seasons", col("duration_seasons").cast(IntegerType()))
df.display()

# COMMAND ----------

df = df.withColumn("shorttitle", split(col("title"), ":")[0])\
      .withColumn("rating", split(col("rating"),"-")[0])
df.display()

# COMMAND ----------

df = df.drop("diuration_minutes", "dirution_seasons")

# COMMAND ----------

df =df.withColumn("flag", when(col("type")=="Movie",1) .when(col("type")=="TV Show",2).otherwise(0))

# COMMAND ----------

from pyspark.sql.window import *

# COMMAND ----------

df = df.withColumn("duration_ranking", dense_rank().over(Window.orderBy(col("duration_minutes").desc())))

# COMMAND ----------

df.display()    

# COMMAND ----------

df_vis= df.groupBy("type").agg(count('*').alias("total_count"))


# COMMAND ----------

df_vis.display()

# COMMAND ----------

df.write.format("delta")\
    .mode("overwrite")\
    .option("path", "abfss://silver@netflixadlsraj.dfs.core.windows.net/netflix_titles")\
    .save()
