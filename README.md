# Instructions to startup application and test

### Requirement:
python 3.7

### Install dependencies:
- Under project root, issue below command

```
pip install -r requirements.txt
```

### Install data and start up application
- Put companies.json and people.json file under project root and run below commands in sequence

```
python data_cleanse.py  
python manage.py migrate  
python manage.py makemigrations  
python manage.py migrate --run-syncdb  
python manage.py loaddata company_data.json  
python manage.py loaddata people_data.json  
python manage.py runserver  
```

### Test
- For testing, issue below command under project root directory

```
python manage.py test api/test/
```

### API endpoints
**Note: company_index, people_index are the index field from companies.json and people.json accordingly**

Your API must provides these end points:
- Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.

http://127.0.0.1:8000/api/all_employee?company_id={company_index}

eg.

<http://127.0.0.1:8000/api/all_employee?company_id=34>

- Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.

http://127.0.0.1:8000/api/common_friends?people_id={people_index}&people_id={people_index}

eg.

<http://127.0.0.1:8000/api/common_friends?people_id=20&people_id=21>

- Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: `{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`

http://127.0.0.1:8000/api/people_details?people_id={people_index}

eg.

<http://127.0.0.1:8000/api/people_details?people_id=23>


