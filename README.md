# Log-Analysis-Udacity-Nanodegree

# Project Overview
An internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Introduction
Program is created in Python and connect to the PostgreSQL database that would already have the datababase schema "news" loaded.  It would try to answer the following questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Quickstart
* [Installing the Virtual Machine Instruction ](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0?contentVersion=5.0.0&contentLocale=en-us) tools called Vagrant and VirtualBox to manage the VM needed to run this project python code against the database for log analysis.
* Step 1:  [Install VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).  VirtualBox is the software that actually runs the virtual machine.  Install the platform package for your operatuing system.  Vagrant will use VirtualBox to launch VM.
* Step 2:  [Install Vagrant](https://www.vagrantup.com/downloads.html).  Vagrant is the software that configures the VM and lets you share files between host computer and VM filesystem via folder '/vagrant/'
* Step 3:  [Download the VM configuration for Vagrant](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).  This will contain the directory `vagrant` which contains the `VagrantFile`.
  Alternatively, it is possible to use Github to fork or clone the repository
  [https://github.com/udacity/fullstatck-nanodegree-vm](https://github.com/udacity/fullstatck-nanodegree-vm)
* Step 4:  Start the Virtual Machine, change directory using `cd` into the `/vagrant` directory and use the command `vagrant up`, then log into it with with `vagrant ssh`

### Load Data into Local Database
[Download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).  Unzip the file 'newsdata.sql' and put this file into 'vagrant' directory that is shared with the vagrant virtual machine.

Load the data into local database using command:
```
psql -d news -f newsdata.sql
```

Break-down of what the command does:
* `psql` -- the PostgreSQL command line Program
* `-d news` -- connect to the database named "news" with preload data from "newsdata.sql"
* `-f newsdata.sql` -- run the SQL statements in the file "newsdata.sql"

### Run the Log analysis
In the `vagrant` directory in virtual machine, copy in the file `LogAnalysisProject.py` and run the command:

```
python LogAnalysisProject.py
```

The result output will match the text in `output.txt` file.
