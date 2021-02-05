from pyspark.sql.types import TimestampType, StringType
from pyspark.sql.functions import udf
import re

@udf(returnType = TimestampType())
def transform_timestamp_in_date(timestamp):
    from datetime import datetime
    return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S %z")

@udf(returnType = StringType())
def url_to_origin(url):
    return re.findall('(?:[-\w.]|(?:%[\da-fA-F]{2}))+',url)[1]

@udf(returnType = StringType())
def delete_unicode_char(description):
    string = description.replace("\n", "")
    string_encode = string.encode("ascii", "ignore")
    string_decode = string_encode.decode()
    return string_decode
