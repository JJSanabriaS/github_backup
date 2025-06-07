from pyspark.ml.feature import StandardScaler
from pyspark.ml import Pipeline
from pyspark.ml.linalg import Vector
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator


spark=SparkSession.builder.appName("RegressionwithPySpark").getOrCreate()
location = "/FileStore/tables/linear_reg_dataset.csv"
file_type = "csv"
infer_schema = "true"
first_row_is_header = "true"
delimiter = ","
new_df = spark.read.format(file_type) \
.option("inferSchema", infer_schema) \
.option("header", first_row_is_header) \
.option("sep", delimiter) \
.load(file_location)
new_df=new_df.withColumnRenamed('output','label')
train_df, test_df = new_df.randomSplit([.75, .25])
features=['var_1', 'var_2', 'var_3', 'var_4', 'var_5']
stage_1 = VectorAssembler(inputCols=features, outputCol="out_
features")
stage_2 = StandardScaler(inputCol="out_features",
outputCol="features")
stage_3 = LinearRegression()
stages = [stage_1, stage_2, stage_3]
pipeline = Pipeline(stages=stages)
model = pipeline.fit(train_df)
pred_result= model.transform(test_df)
pred_result.show(5)
regeval = RegressionEvaluator(labelCol="label",
predictionCol="prediction", metricName="rmse")
acc = regeval.evaluate(pred_result, {regeval.metricName: "r2"})
print(acc)
rmse = regeval.evaluate(pred_result)
print(rmse)