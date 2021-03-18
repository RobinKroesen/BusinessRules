import psycopg2
import random
con = psycopg2.connect(
    host='localhost',
    database='DocumentStore',
    user='postgres',
    password='Robinson1',
     port=5433
)

cur = con.cursor()

def select_product(product_id):
    """functie waarbij product uit de database gehaald wordt om recommendations voor te maken(In de front end op een product klikken)."""

    product_nummer = product_id
    query = "SELECT * FROM product where product_id=%s"
    cur.execute(query, [product_nummer])
    product = cur.fetchall()
    con.commit()
    return product

def content_filtering(product):
    """Een vergelijking van de het gender en de sub-categorie van een product met de andere producten in de tabel 'product'.
    Er worden 5 willekeurige producten in dezelfde sub-categorie en het omgekeerde gender gegeven als recommendation."""
    gender = product[0][3]
    sub_category = product[0][5]
    mogelijke_genders = ['Man', 'Vrouw']
    if gender in mogelijke_genders:
        index = mogelijke_genders.index(gender)
        query = "SELECT product_id FROM product WHERE sub_category=%s AND gender=%s ORDER BY RANDOM() LIMIT 5"
        cur.execute(query, [sub_category, mogelijke_genders[index-1]])
        output = cur.fetchall()
        con.commit()
        create_table_query = """DROP TABLE if EXISTS content_filter CASCADE;
                                CREATE TABLE content_filter(
                                content_filter_id varchar(255),
                                product_id varchar(255),
                                recommended_product_id varchar(255),
                                PRIMARY KEY (content_filter_id),
                                FOREIGN KEY (product_id)
                                    REFERENCES product(product_id)
                                );"""
        cur.execute(create_table_query)
        con.commit()
        for i in range(len(output)):
            insert_query = "INSERT INTO content_filter(content_filter_id, product_id, recommended_product_id) VALUES (%s,%s,%s)"
            cur.execute(insert_query, [i, product[0][0], output[i][0]])
            con.commit()
    else:
        output = 'Dit product heeft geen recommendation voor je partner'
    cur.close()
    con.close()
    return output

def collaborative_filtering(profile):
    """functie die op basis van het gedrag van de klant producten koppelt van klanten het hetzelfde gedrag vertoonden."""
    profile_query = "SELECT segment from profile WHERE profile_id = %s"
    cur.execute(profile_query, [profile])
    output_profile = cur.fetchall()
    gedrag = output_profile[0][0]
    con.commit()
    print(gedrag)
    select_query = "SELECT viewed_before FROM profile WHERE segment=%s ORDER BY RANDOM() LIMIT 50"
    cur.execute(select_query, [gedrag])
    output = cur.fetchall()
    con.commit()
    print(output)
    viewed_before = []
    for list in output:
        for items in list:
            for item in items:
                viewed_before.append(item)
    amount_of_recommendations = 5
    recommendations_collaborative = []
    for i in range(amount_of_recommendations):
        recommendations_collaborative.append(random.choice(viewed_before))
    print(recommendations_collaborative)

    create_table_query = """DROP TABLE IF EXISTS collab_filter CASCADE;
                            CREATE TABLE collab_filter(
                            collab_filter_id varchar(255),
                            profile_id varchar(255),
                            collab_product_id varchar(255),
                            PRIMARY KEY (collab_filter_id),
                            FOREIGN KEY (profile_id)
                                REFERENCES profile(profile_id)
                            );"""
    cur.execute(create_table_query)
    con.commit()
    for i in range(len(recommendations_collaborative)):
        insert_query = "INSERT INTO collab_filter(collab_filter_id, profile_id, collab_product_id) VALUES (%s,%s,%s)"
        cur.execute(insert_query, [i, profile, recommendations_collaborative[i]])
        con.commit()
    cur.close()
    con.close()


#content_filtering(select_product('3896'))
#collaborative_filtering('5a393d68ed295900010384ca')