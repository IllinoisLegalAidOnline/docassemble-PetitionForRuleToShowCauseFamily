def name_with_age(person):
  name_age_string = person.name_full()
  name_age_string += " (age  "
  name_age_string += str(int(person.age.years))
  name_age_string += ")"
  return name_age_string