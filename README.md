# Product API with flask and postgresSQL

This is a simple product API that can perform basic crud operations with flask.

## Getting started

### Basic configurations
* This APi was made with python and flask. So to run this applications you need to certify that you have this dependencies installed.

You can simple do that by running this command in the root folder of this project.

``` sh
$ pip install -r requirements.txt 
```

> **Note**: It's recommended to use a virtual environment, you can see more about that [here](https://virtualenv.pypa.io/en/latest/installation.html).

*  Next, you need to setup a postgres instace.

For this API i used a docker instace for postgres, you can se how to do that [here](https://hub.docker.com/_/postgres)

> **Note**: You need change the code to use your database credentials, you can do that by navigating to api/database/config.py and update it with your credentials.

For default the app will try to connect to database with these configurations

``` python
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="password"
POSTGRES_HOST="localhost"
POSTGRES_PORT="5432"
```

And connect to a database called "products".
> **Note**: You can change that with the same method listed above and update the variable called "POSTGRES_DB".

### Running 
To execute this API you can simple open your terminal and type this command in the root folder of this project.

``` sh
$ python3 app.py 
```
Now the project is alredy running, and for default it will start on: http://127.0.0.1:5000/

## Documentation

This api use swagger as documentation, you can simple see that by navigating to this url: http://127.0.0.1:5000/swagger/
> **Note**: If you're not using the default url change this link to {your-url}/swagger

## Testing 

I wrote some unit tests to this api, and if you want to run it, folow the process bellow.

* **First:**

You need to certify that the API is running. If not, you can simple do it by typing this commnad in the root folder of this project.

``` sh
$ python3 app.py 
```

* **Second:**
Now, open another terminal, and run this tests with a simple command in the root folder of this project.

``` sh
$ python3 test/test.py 
```

> **Note**: If you want see more about those tests navigate to test/test.py


