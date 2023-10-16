# Population Growth Calculator

#Write the necessary code to display the total population count for the next 3 years (without a leap year).

#Here are the specifications:

#In the country we want to investigate:

# The current population is 380,123,456
# One person is born every 6 seconds
# One person dies every 12 seconds
# One person immigrates every 40 seconds

# Calculating seconds per year and assigning variable to the current tot pop
second_per_year = ((60*60)*24)*365
tot_pop = 380123456

# Calculating how many newborn, dead and immigrates per year
new_born_year = (second_per_year / 6)
dead_year = (second_per_year / 12)
welcome_year = (second_per_year / 40)

# Calculating yearly increases
year_increase = (tot_pop + (new_born_year + welcome_year - dead_year)) - tot_pop

# Printing results from current situation
print ("Year 0 = ", tot_pop)
print ("Year 1 = ", (int(tot_pop + year_increase)))
print ("Year 2 = ", (int(tot_pop + (2 * year_increase))))
print ("Year 3 = ", (int(tot_pop + (3 * year_increase))))