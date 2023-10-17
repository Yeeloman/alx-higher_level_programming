# 0x0D. SQL - Introduction

The following project focuses on SQL, it works as an introduction.

## Requirements:

  * [MySQL](https://www.mysql.com/fr/)
    * Install MySQL:

    ```
    >_ sudo apt update
    >_ sudo apt install mysql-server
    ...
    >_ mysql --version
    mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
    >_
    ```
    * Connect to mysql server:

    ```
    >_ sudo mysql
    Enter password:
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 19
    Server version: 10.11.4-MariaDB-1 Debian 12

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    >_
    ```
## Usage:

all the scripts can be used as the following example:
```>_ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p```

## Tasks:

  * task 0:
    * a script that lists all databases of your MySQL server.
    * File: [0-list_databases.sql](./0-list_databases.sql)
  * task 1:
    * a script that creates the database `hbtn_0c_0` in your MySQL server.
    * File: [0-list_databases.sql](./0-list_databases.sql)
  * task 2:
    * a script that deletes the database `hbtn_0c_0` in your MySQL server.
    * File: [2-remove_database.sql](./2-remove_database.sql)
  * task 3:
    * a script that lists all the tables of a database in your MySQL server.
    * File: [3-list_tables.sql](./3-list_tables.sql)
  * task 4:
    * a script that creates a table called `first_table` in the current database in your MySQL server.
    * File: [4-first_table.sql](./4-first_table.sql)
  * task 5:
    * a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
    * File: [5-full_table.sql](./5-full_table.sql)
  * task 6:
    * a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
    * File: [6-list_values.sql](./6-list_values.sql)
  * task 7:
    * a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
    * File: [7-insert_value.sql](./7-insert_value.sql)
  * task 8:
    * a script that displays the number of records with id = 89 in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.
    * File: [8-count_89.sql](./8-count_89.sql)
  * task 9:
    * a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.
    * File: [9-full_creation.sql](./9-full_creation.sql)
  * task 10:
    * a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
    * File: [10-top_score.sql](./10-top_score.sql)
  * task 11:
  * task 12:
  * task 13:
  * task 14:
  * task 15:
  * task 16:
  * task 17:
  * task 18:
  * task 19:
  * task 20:
