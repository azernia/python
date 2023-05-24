import mysql.connector as connector

my_db = connector.connect(
    host="gsmpdb-dev.clnv8hcwth8v.ap-southeast-1.rds.amazonaws.com",
    user="rui.yu",
    password="H3x!ArPw4Zinu#BL",
    database="GSMPDEV"
)

my_cursor = my_db.cursor()
my_cursor.execute("""
select cl.Id, cl.InstallationDate, cl.WarrantyCoverage, cl.WarrantyEffectiveDate, cl.WarrantyExpiryDate 
from client_LocationAsset cl 
where cl.Id = 866550
""")
result = my_cursor.fetchall()
for item in result:
    print(item)