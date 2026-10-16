from pyspark.sql import SparkSession
from pyspark.sql import functions as F 
def main():
    spark=SparkSession.builder.appName("test_app").master("local[2]").getOrCreate()
    print(f"\nSpark UI: {spark.sparkContext.uiWebUrl}")
    try:
        input("Inspect the Spark UI, then press Enter here to stop Spark... ")
    finally:
        spark.stop()
if __name__ == "__main__":
    main()