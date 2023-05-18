![GA workflow](https://github.com/koitoror/ClosestPair/actions/workflows/django-test-action.yml/badge.svg)


## Closest Points
Django application with an API that receives a set of points on a grid as semicolon separated values. And then it finds the points that are closest to each other. Store the received set of points and the closest points on a DB.


An example input would look like this:
2,2;-1,30;20,11;4,5

And then in this case the result would be:
2,2;4,5


ADDITIONALLY : admin interface for viewing values stored on the DB.


## API Installation

### Prerequisites

In order to install and run this project locally, you would need to have the following installed on you local machine.

* [**Python 3+**](https://www.python.org/downloads/release/python-368/)
* [**Django 4+**](https://www.djangoproject.com/download/) 
* [**Django Rest Framework 3+**](https://www.django-rest-framework.org/) 
* [**MySQL**](https://www.mysql.com/downloads/)



1. Clone this repository into a folder of your choice:
```
git clone https://github.com/koitoror/ClosestPair.git
```

2. Install the dependencies/packages.
```
pip install -r requirements.txt
```

3. Run database migration:
```python manage.py makemigrations & migrate ```

4. Start the Django development server:
```python manage.py runserver```

NB:// To set up The API, make sure that you have python3, postman and pip installed.

Use [virtualenv](http://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv) for an isolated working environment.

Set environment variables for:
> `SECRET_KEY` is your secret key

> `DJANGO_ENV` is the enviroment you are running on. Should be either `Production`, `Development` or `Testing`. NOTE: its case sensitive

> `DB_HOST` which is localhost

> `DB_PORT`  the default port for postgresql service which 5432

> `DB_USER` is the postgresql user

> `DB_PASSWORD` is the postgresql password for the user created

> `DB_NAME` the name of the app database

### Using Docker 
Build image

`docker build -t koa_app .` 



## Usage - REST Endpoints
To test endpoints manually fire up postman and run the following endpoints

**EndPoint** | **Functionality**
--- | ---
GET  `/api/v1/admin` | admin interface for viewing values stored on the DB.
POST  `/api/v1/closest` | closest points from given points

## Example  API Spec
The preferred JSON object to be returned by the API should be structured as follows:

**Request Payload**: Content-Type: application/json

```source-json
{
  "points": "2,2;-1,30;20,11;4,5"
}
```

**Response**
HTTP/1.1 200 OK

```

{
    "closest_points": "2,2;4,5"
}
```
  

## API Unit Tests

To run your tests use

```bash
$ python manage.py test or
$ pytest --cov
```

