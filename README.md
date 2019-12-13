Instructions to startup application and test

-- Requirement:
python 3.7

-- Install dependencies:
Under project root, issue below command

pip install -r requirements.txt

-- Install data and start up application
Put companies.json and people.json file under project root and run below commands in sequence

python data_cleanse.py 
python manage.py migrate
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py loaddata company_data.json
python manage.py loaddata people_data.json 
python manage.py runserver

-- Test
For testing, issue below command under project root directory

python manage.py test api/test/