import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import corr
from pyspark.ml.linalg import Vector
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression


spark=SparkSession.builder.appName("RegressionwithPySpark").getOrCreate()
location = "/FileStore/tables/linear_reg_dataset.csv"
file_type = "csv"
infer_schema = "true"
first_row_is_header = "true"
delimiter = ","
df = spark.read.format(file_type) \
.option("inferSchema", infer_schema) \
.option("header", first_row_is_header) \
.option("sep", delimiter) \
.load(file_location)
display(df)
#statistic from data
df.describe().show(3,False)
df.select(corr('var_1','label')).show()
vec_assmebler=VectorAssembler(inputCols=['var_1','var_2','var_3','var_4','var_5'],outputCol='features')
features_df=vec_assmebler.transform(df)
features_df.printSchema()
 model_df=features_df.select('features','label')
#We split it in 75/25 ratio and train our
#model on 70% of the dataset. We can print the shape of train and test data to validate the size:
train_df,test_df=model_df.randomSplit([0.75,0.25])
lin_Reg=LinearRegression(labelCol='label')
lr_model=lin_Reg.fit(train_df)
print(lr_model.coefficients)
print(lr_model.intercept)
training_predictions=lr_model.evaluate(train_df)
print(training_predictions.r2)

#evaluation
test_results=lr_model.evaluate(test_df)
print(test_results.r2)
print(test_results.rootMeanSquaredError)