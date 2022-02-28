# url-short-api
Url shortner in restful APIs

## Approach
This Service has mainly 4 API endpoints for shortening the url, redirecting to original url, search based on keywords and metadata of url.
If for a particular url, entry alreday exists in db then we share the same and not create another duplicate entry.
I also added a cronjob that runs every hour to reset the hourly hit count.

Things which should be done next:
1. Add created and modified datetime column in table and periodically delete those entries which are not being modified in last 7 days to optimize db size.

## Quickstart

To work in a sandboxed Python environment it is recommended to install the app in a Python [virtualenv](https://pypi.python.org/pypi/virtualenv).

1. Clone and install dependencies

    ```bash
    $ git clone https://github.com/akanuragkumar/url-short-api.git
    $ cd url-short-api
    $ pip install -r requirements.txt
    ```   
2. Running app

   ```bash
   $ manage.py makemigrations 
   $ python manage.py migrate
   $ python manage.py crontab add
   $ python manage.py runserver
   ``` 
   
   
## API Documentation 

`https://documenter.getpostman.com/view/18135865/UVkqruNY` 

