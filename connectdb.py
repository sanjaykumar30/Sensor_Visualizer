import psycopg2

def runquery(sql):
    try:
        connection=psycopg2.connect(user="ekfsynkqyqyoqn",password="94135c6e8449ec2bf3d09f85141b578f8d2d8325bc248f1fee7da15c33898266",host="ec2-52-71-69-66.compute-1.amazonaws.com",database="d74qkejpevt19a")
        cursor=connection.cursor()
        cursor.execute(sql)
        record=cursor.fetchall()
        return record
    except:
        print("errror while fetching data")
    finally:
        cursor.close()
        connection.close()