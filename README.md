# Product API with flask and postgresSQL

This is a simple product API that can perform basic crud operations with flask.

## Getting started

### Basic configurations
* This APi was made with python and flask. So to run this applications you need to certify that you have this dependencies installed.

You can simple do that by running this command in the root folder of this project.

``` sh
$ pip install -r requirements.txt 
```

> **Note**: It's recommended to use a virtual envoirement, you can see more about that [here](https://virtualenv.pypa.io/en/latest/installation.html).

*  Next, you need to setup a postgres instace.

For this API i used a docker instace for postgres, you can se how to do that [here](https://hub.docker.com/_/postgres)

> **Note**: You need update the code to use your database credentials, you can do that by navigating to api/database/config.py and update it with your credentials.

For default the code will try to connect to database with these configutaions

``` python
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="password"
POSTGRES_HOST="localhost"
POSTGRES_PORT="5432"
```

And connect to a database called products.
> **Note**: You can change that with the same method listed above

### Running 
To running this API you can simple open your terminal and type this command in the root folder of this project.

``` sh
$ python3 app.py 
```
Now the project is alredy running, for default it will start on: http://127.0.0.1:5000/

## Documentation

This api use swagger as documentation, you can simple see that by navigating to this url: http://127.0.0.1:5000/swagger/
> **Note**: If you're not using the default url change this link to {your-url}/swagger

## Testing 

I wrote some basic tests to the api, and if you wanna running it folow the process bellow.

* **First:**

You need to certify that you're running the API. If not, you can simple do it by running this commnad in the root folder of the project.

``` sh
$ python3 app.py 
```

* **Second:**
Now you can run those tests with a simple command.

``` sh
$ python3 test/test.py 
```

> **Note**: If you want see the code navigate to test/test.py


