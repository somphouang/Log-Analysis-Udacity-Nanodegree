#!/usr/bin/env python
#
# news_analysis.py -- Log analysis project
#
import psycopg2


def print_resultset(resultset):
    for row in resultset:
        print('\t* \" ' + str(row[0]) + '\" ---- ' + str(row[2]) + ' views')


# Database that this project will connect to for analysis
DATABASE_NAME = "news"
db = psycopg2.connect(database=DATABASE_NAME)
c = db.cursor()

# Question 1:  What are the most popular three articles of all time?
query1 = """
    select title, count(*) as views, author
    from log, articles
    where log.path like concat('%',articles.slug)
    group by articles.title, articles.author
    order by views desc limit 3
    """
c.execute(query1)
result1 = c.fetchall()

# Print answer 1
print('\n\t1.  What are the most popullar three articles of all time?')
for row in result1:
    print('\t* \"' + str(row[0]) + '\" ---- ' + str(row[1]) + ' views')

# Question 2:  Who are the most popular article authors of all time?
query2 = """
    select name, sum(views) as sums
    from
        (
        select title, count(*) as views, author
        from log, articles
        where log.path like concat('%',articles.slug)
        group by articles.title, articles.author
        )
        as popular_authors, authors
        where authors.id = popular_authors.author
        group by name
        order by sums desc
    """
c.execute(query2)
result2 = c.fetchall()

# Print answer 2
print('\n\n\t2.  Who are the most popular article authors of all time?')
for row in result2:
    print('\t* ' + str(row[0]) + ' ---- ' + str(row[1]) + ' views')


# Question 3:  On which days did more than 1% of requests lead to errors
query3 = """
    select day, total, error, round(error*100.0/total, 2) as err_percent
    from
        (
        select date(time) as day,
        count(log.status) as total,
        sum(case when log.status != '200 OK' then 1 else 0 end) as error
        from log
        group by day
        )
    as log_error
    order by err_percent desc
    limit 1
    """

c.execute(query3)
result3 = c.fetchall()

# Print answer 3
print('\n\n\t3.  On which days did more than 1% of requests lead to errors')
for row in result3:
    print('\t* ' + str(row[0]) + ' ---- ' + str(row[3]) + ' % errors')

# Close the Database connection, all query are done
db.close()
