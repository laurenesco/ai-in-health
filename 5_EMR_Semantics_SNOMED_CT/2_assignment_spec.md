Generate a SQL tutorial using MIMIC-III or MIMIC-IV data.
You may not use demo data for this assignment.

## Learning Outcomes

After finishing this assignment, you should be able to say: 

        I know how EHR data can be structured in a database.
        I can write SQL queries to retrieve data points about EHR data. 
        I can explain the results of a query.

## Rationale

The goal of this assignment is to get familiar with the EHR data as a database and to use SQL queries to retrieve interesting data points or statistics. It is the next step to understanding data. This assignment will provide an opportunity for you to gain proficiency with important skills related to database and SQL query. 
Instructions

Develop 10 SQL queries. For full credit, these must include:

Basic:

1. 10 SQL queries, collectively using SELECT, JOIN, ON / USING,  WHERE and ORDER BY.

2. At least 3 of the queries also use row (scalar) functions: e.g.,

    UPPER, LEFT, TRIM, CAST, NULLIF, ROUND, YEAR, DATEDIFF, AGE



Aggregate:

1. At least 3 of the 10 SQL queries also use GROUP BY and an aggregate function: e.g.,

    COUNT, SUM, AVG, MIN, MAX, MEDIAN, STDDEV, PERCENTILE_CONT (WITHIN GROUP)



Advanced:

1. At least 3 of the 10 SQL queries also use one or more advanced SQL functions and commands: e.g.,

    - Conditional: CASE WHEN, IIF

    - Matching: LIKE, regular expressions (REGEXP, REGEXP_REPLACE)

    - Compound Joins: joins of three or more tables, nested/subqueries, WITH (CTE), USING

    - Outer Joins: LEFT, RIGHT, FULL OUTER, CROSS JOIN

    - Set operations: UNION, INTERSECT, MINUS / EXCEPT

    - Window functions: PARTITION OVER, RANK, LAG, LEAD

     

## Bonus 1 pt

Bonus: You use creativity to build queries that, together, tell an interesting and cohesive story.

For this assignment, we recommend setting up MIMIC-III or MIMIC-IV with Google BigQuery (see Tutorial_MIMIC3_BigQuery.pdf
), or you can load the databases to your local MySQL Workbench or other SQL database software you prefer (e.g., PostgreSQL, SQLite, DuckDB). If you do not already have access to the full MIMIC database, you may temporarily use the MIMIC-IV demo data or MIMIC-III demo data for initial development, which have the same field names and characteristics as the full datasets, then swap in the full datasets for your actual submission.

Please make your SQL queries interesting and meaningful. Consider the kinds of statistics that might be useful to someone who is doing healthcare research or working in quality improvement. 

Once you have built and executed your queries, create a slide deck with a description, your code, screenshots of the results, and an interpretation of the results for each one. 

If you can align your 10 queries into one cohesive story, you can get one bonus point. For example, telling a story of the descriptive statistics of a certain disease: the distribution of patients by gender, insurance, top medication prescribed, their length of stay range, readmission percentage, major lab tests, and so on.

## Submission

Slide Deck of 10 Queries
- Each query should include the following:
    - The meaning/description of the query
    - The SQL query
    - Screenshots of the results
    - A simple interpretation of the results
- Optional Bonus:
    - Additional slide telling the overall story of the queries.
    - Please highlight any work intended for bonus credit.
