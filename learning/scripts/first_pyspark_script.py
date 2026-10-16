"""First local PySpark script: transform a tiny orders dataset."""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main() -> None:
    # `local[*]` runs Spark on this computer using all available CPU cores.
    # Databricks notebooks provide a Spark session for their attached cluster,
    # so you would use that existing `spark` session there instead.
    spark = (
        SparkSession.builder
        .appName("first-pyspark-script")
        .master("local[*]")
        .getOrCreate()
    )

    orders = spark.createDataFrame(
        [
            (1001, "Asha", "books", 24.50, "complete"),
            (1002, "Ravi", "equipment", 89.00, "complete"),
            (1003, "Asha", "books", 15.00, "cancelled"),
            (1004, "Mina", "equipment", 42.00, "complete"),
            (1005, "Ravi", "books", 32.00, "complete"),
        ],
        ["order_id", "customer", "category", "amount", "status"],
    )

    print("Input orders")
    orders.show()

    completed_by_category = (
        orders
        .filter(F.col("status") == "complete")
        .groupBy("category")
        .agg(
            F.count("*").alias("order_count"),
            F.round(F.sum("amount"), 2).alias("revenue"),
        )
        .orderBy(F.col("revenue").desc())
    )

    print("Completed orders by category")
    completed_by_category.show()

    print("Execution plan")
    completed_by_category.explain()

    print(f"\nSpark UI: {spark.sparkContext.uiWebUrl}")
    try:
        input("Inspect the Spark UI, then press Enter here to stop Spark... ")
    finally:
        spark.stop()


if __name__ == "__main__":
    main()
