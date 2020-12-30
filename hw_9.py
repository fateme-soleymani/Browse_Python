import psycopg2

from hw_2 import ExtendedList
from hw_4 import iris_lst

for j in range(1, len(iris_lst)):
    iter_iris = ExtendedList.next_val(iris_lst[j])
    list_value = []
    while True:
        try:
            num = next(iter_iris)
            list_value.append(num)
        except ValueError:
            pass
        except StopIteration:
            break
    print(list_value)

conn = psycopg2.connect(
    host="localhost",
    database="iris",
    user="postgres",
    password="FSD@9740")
cursor = conn.cursor()
select_query2 = "insert into irislist(sepal_length,sepal_width,petal_length,petal_width,variety) values ???"
cursor.execute(select_query2)
conn.commit()
select_query = "select * from irislist"
cursor.execute(select_query)
role_records = cursor.fetchall()
print(role_records)
