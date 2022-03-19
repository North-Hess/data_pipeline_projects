import pymysql, csv, boto3, configparser

# grab connection parameters from config file
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
hostname = parser.get("mysql_config", "hostname")
port = parser.get("mysql_config", "port")
username = parser.get("mysql_config", "username")
password = parser.get("mysql_config", "password")
dbname = parser.get("mysql_config", "database")

# establish connection with variables
conn = pymysql.connect(host=hostname,
    user=username,
    password=password,
    db=dbname,
    port=int(port))

# check connection
if conn is None:
    print("Error connecting to the MySQL database")
else:
    print("MySQL connection established!")