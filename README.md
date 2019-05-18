# Logs Analysis Project :

    Logs Analysis is one of the Udacity's Full Stack Web Developer Nanodegree projects, this project is a reporting tool that prints out reports based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

# Technology used :
    This project was done on Windows 10 using :

        1. Vagrant and VirtualBox,
        2. Python DB-API,
        3. psycopg2 module.

    The repoting tool gives an answer to the following questions and prints out reports on:

        1. What are the most popular three articles of all time?,
        2. Who are the most popular article authors of all time?,
        3. which days did more than 1% of requests lead to errors?

# Database used :
    The database is called `news` and has three tables :

        1. (authors) table has information about the authors of the articles,
        2. (articles) table has the articles itself,
        3. (log) table has every entry for each time a user has accessed the site.

# Steps Required : 

        1. Install Virtual Machine,
        2. Install Vagrant,
        3. Download FSND Virtual Machine Configuration and unZip the file,
        5. Change terminal to the vagrant directory `cd /vagrant`
        6. Run `vagrant up` command to open the VM,
        7. Run `vagrant ssh` command to log into the VM,
        8. Connect and load the data using `-d news` into the `psql` command line,
        9. Run `python newsdata.py` to run the reporting tool.

# Links used :

        1. [Virtual Machine](https://www.virtualbox.org/wiki/Downloads),
        2. [Vagrant](https://www.vagrantup.com/),
        3. [VM Configuration](Udacity Tutorial videos).