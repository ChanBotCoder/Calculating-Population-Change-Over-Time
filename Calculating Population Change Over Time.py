pop_1927 = 691000
pop_2017 = 15029231
pop_1950 = 983000
pop_2000 = 8831800

city_name = ["Istanbul, Turkey"]

pop_change = pop_2017 - pop_1927

percentage_gr = ((pop_change)/pop_1927)*100

annual_gr = percentage_gr / (2017 - 1927)

def population_growth(year_one,year_two,population_one,population_two):
  pop_change = population_two - population_one
  percentage_gr = ((pop_change)/population_one)*100
  growth_rate = percentage_gr / (year_two - year_one)
  return growth_rate
print(annual_gr)

set_one = population_growth(1927,2017,pop_1927,pop_2017)
print(set_one)

set_two = population_growth(1950,2000,pop_1950,pop_2000)

report = ("The population grew from " +str(pop_1927)+ " to " +str(pop_2017)+ " with the total change of "+str(pop_change)+". The annual %gr was "+str(annual_gr))
print(report)
