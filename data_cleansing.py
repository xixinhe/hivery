import json

with open('./fruit_list.json') as fruit_list_json:
    fruits_list = json.load(fruit_list_json)

with open('companies.json', 'r') as companies_raw_json:
    companies_raw_data = json.load(companies_raw_json)
    companies_data = [{'model': 'api.company', 'pk': a['index'], 'fields': { 'name': a['company']}} for a in companies_raw_data]

with open('./api/fixtures/company_data.json', 'w') as companies_json:
    json.dump(companies_data, companies_json)

with open('people.json', 'r') as people_raw_json:
    people_raw_data = json.load(people_raw_json)

    people_data = []
    for people in people_raw_data:
        food = people['favouriteFood']
        fruit = [a for a in food if a in fruits_list]
        vegetable = [a for a in food if a not in fruit]
        friend=[a['index'] for a in people['friends']]
        people = {'model': 'api.people', 'pk': people['index'], 'fields': {
                    'has_died':people['has_died'],
                    'age':people['age'],
                    'eye_color':people['eyeColor'],
                    'name':people['name'],
                    'company_id':people['company_id'],
                    'vegetable':vegetable,
                    'fruit':fruit,
                    'address':people['address'],
                    'phone':people['phone'],
                    'friend':json.dumps(friend)
        }}
        people_data.append(people)

with open('./api/fixtures/people_data.json', 'w') as people_json:
    json.dump(people_data, people_json)