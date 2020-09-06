# trending-repos/GitHub-API-v3

## Table of contents:

* [Description](./README.md#description)
  * [Task](./README.md#task)
* [Setup](./README.md#setup)
* [Running the app](./README.md#running-the-app)

## Description

Simple python file list the top languages used by the 100 trending public repos on GitHub.

## Task



Develop a REST microservice that list the languages used by the 100 trending public repos on GitHub.
- For every language, you need to calculate the attributes below point_down:
  - Number of repos using this language
  - The list of repos using the language

## Setup

1. Make a copy of .env.example and rename the new copy to .env

2. Create a token on your github account

3. Add the token to your newly created .env file

## Running the app

4. Simply run the python file

    ```python main.py```

5. Please note that this file is writen in python 3. if your system have python 2 and 3, you will need to run the file using the following command instead

    ```python3 main.py```

6. To run servise using new GitHub API v4 -GraphQl-

    ```python main-graphql.py```
    ```python3 main-graphql.py```
