class Person:
    def __init__(self,name,age,favorite_foods):
        self.name = name
        self.age = age
        self.favorite_foods = favorite_foods
    def __str__(self):
        return 'Name: {} Age: {} Favorite food: {}'.format(self.name,self.age,self.favorite_foods[0])
    def birth_year(self):
        return 2021 - self.age

people = [Person('Ed',11,['hotdogs','jawbrakers']),
          Person('Edd',13,['Brocolli']),
          Person('Eddy',12,['chunkyy puffs','jawbrakers'])]

age_sum = 0
year_sum = 0
for person in people:
    age_sum = age_sum + person.age
    year_sum = year_sum +person.birth_year()

print('The average age is: '+ str(age_sum/len(people)))
print('The average birth year is:' + str(int(year_sum / len(people))))
for person in people:
    print(person)
