# PostgreSQL Database Agent

## Application Running  
```
python3 main.py 
```

## Application Response
```
(venv) shraman@shramans-mbp database-agent % python3 main.py
/Users/shraman/Projects/GIT/database-agent/venv/lib/python3.13/site-packages/langsmith/client.py:277: LangSmithMissingAPIKeyWarning: API key must be provided when using hosted LangSmith API
  warnings.warn(
INFO:core.config:['dialect', 'top_k']
INFO:core.config:Database connection established successfully.
================================ Human Message =================================

Which City has more number of people at age equal to 35 ?
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
================================== Ai Message ==================================
Tool Calls:
  sql_db_list_tables (call_5W1QjNJWycG4JekZ7fP8FmEK)
 Call ID: call_5W1QjNJWycG4JekZ7fP8FmEK
  Args:
================================= Tool Message =================================
Name: sql_db_list_tables

users
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
================================== Ai Message ==================================
Tool Calls:
  sql_db_schema (call_6dPMXpxufIm5zThv79XLvZwU)
 Call ID: call_6dPMXpxufIm5zThv79XLvZwU
  Args:
    table_names: users
================================= Tool Message =================================
Name: sql_db_schema


CREATE TABLE users (
        id SERIAL NOT NULL, 
        name VARCHAR(100) NOT NULL, 
        email VARCHAR(150) NOT NULL, 
        age INTEGER, 
        city VARCHAR(100), 
        state VARCHAR(100), 
        created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
        CONSTRAINT users_pkey PRIMARY KEY (id), 
        CONSTRAINT users_email_key UNIQUE (email), 
        CONSTRAINT users_age_check CHECK (age > 0)
)

/*
3 rows from users table:
id      name    email   age     city    state   created_at
1       Alice Johnson   alice@example.com       30      New York        NY      2025-03-30 20:10:27.533959
2       Bob Smith       bob@example.com 25      Los Angeles     CA      2025-03-30 20:10:27.533959
3       Charlie Brown   charlie@example.com     35      Chicago IL      2025-03-30 20:10:27.533959
*/
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
================================== Ai Message ==================================
Tool Calls:
  sql_db_query (call_EDozSKxfA09oHzkC4FpRnNkJ)
 Call ID: call_EDozSKxfA09oHzkC4FpRnNkJ
  Args:
    query: SELECT city, COUNT(*) as count FROM users WHERE age = 35 GROUP BY city ORDER BY count DESC
================================= Tool Message =================================
Name: sql_db_query

[('Chicago', 1)]
INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
================================== Ai Message ==================================

The city with the most number of people at the age of 35 is Chicago, with 1 person.
```
