#!/usr/bin/env python3

from faker import Faker
import pandas as pd 
import numpy as np
 
 
Faker.seed(96)
 
 
def generate_persons(num = 42):
    fake = Faker()
    rows = [{
                'person_id':fake.uuid4(),
                'first_name':fake.first_name(),
                'last_name':fake.last_name(),
                'address':fake.address(),
                'dob':fake.date_of_birth(minimum_age = 18, maximum_age = 75),
                'ssn':fake.ssn()
            }
            for x in range(num)]
    return pd.DataFrame(rows)
 
value = True
while (value):
	persons = generate_persons(60)
	print(persons)
