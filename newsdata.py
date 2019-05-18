# !/usr/bin/env python3

import psycopg2


# connecting to database news
def connect_db(sql):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(sql)
    x = c.fetchall()
    db.close()
    return x

# query1: what are the most popular three articles of all time?
def no_articles():
    sql = """
    SELECT articles.title, count(*) as viewCount
    FROM log, articles 
    WHERE log.status='200 OK' and articles.slug = substr(log.path,10)
    GROUP by articles.title ORDER BY viewCount desc limit 3;"""
    x = connect_db(sql)
    return x

# query2: Who are the most popular article authors of all time?
def top_authors():
    sql = """
    SELECT authors.name, count(*) as viewCount
    FROM log, authors
    INNER JOIN articles on (articles.author = authors.id)
    WHERE log.status = '200 OK' and articles.slug = substr(log.path, 10)
    GROUP BY authors.name ORDER BY viewCount desc;
    """
    x = connect_db(sql)
    return x

# query3: On which days did more than 1% of requests lead to errors?

def error_per_day():
    sql = """
    SELECT time::date,
    round(sum(CASE WHEN status = '404 NOT FOUND' THEN 1.0 else 0.0 END) / COUNT(*)*100.0, 2) as percent 
    FROM log
    GROUP BY time::date
    HAVING round(sum(CASE WHEN status = '404 NOT FOUND' THEN 1.0 else 0.0 END) / COUNT(*)*100.0, 2) > 1.0
    ORDER BY time::date desc;
    """
    x = connect_db(sql)
    return x

# printing results
def result():
    task1 = no_articles()
    print("""\n the most read articles of all time  \n""")
    for title, num in task1:
        print(""" {} - {} views""".format(title, num))

    task2 = top_authors()
    print("""\n\n   the most popular article authors of all time :\n""")
    for name, num in task2:
        print(""" {} - {} views""".format(name, num))

    task3 = error_per_day()
    print("""\n   days did more than 1% of requests lead to errors :\n""")
    for day, percent in task3 :
        print(""" {0:%b %d, %Y} - {1:.2f} % errors""".format(day, percent))

if __name__ == '__main__':
      result()