# Calculating-Population-Change-Over-Time

Calculating Population Change Over Time

You work at the UN in urban planning and are interested in tracking population growth across major metropolitan regions. 
You are hoping that by looking at historical population numbers that you can predict future growth and help your team make decisions about resourcing.
Use what you’ve learned about the basics of Python to calculate the population growth of Istanbul and print out a short report.

Creating Variables:
Step 1 :
Istanbul is the largest city in Turkey and the fifth largest city in the world. It has experienced enormous growth over the past 50 years and is one of the world’s 10 fastest growing metropolitan areas.

While the program that we will write can be used with data from any city, we’ll start by using data from Istanbul and saving our data to variables. Using variables will allow us to swap out the data in the future.

The following chart is an abbreviated list of the population size by year in Istanbul. Take a moment to read over the data — you will need to refer back to this chart as you complete certain tasks.
Year 	Population
1927 	691000
1950 	983000
2000 	8831800
2017 	15029231

Step 2:
First, create the variable city_name and set it equal to "Istanbul, Turkey".

Step 3:
The dataset starts with the population value for the year 1927 and ends with 2017.
Create the variable pop_1927. In the chart, find the population for 1927 and set it equal to the variable pop_1927.

Step 4:
Next, create the variable pop_2017. Find the population for 2017 and set its value equal to the variable pop_2017.

Using Variables to Perform Calculations:
Step 5:
Using the variables that we just created, we’re going to write a script that allows us to calculate the annual percentage growth rate. The annual percentage growth rate is the amount in which the population changes each year during a certain period.
First, create the variable pop_change. Calculate the change in population between 1927 and 2017 and save the result to the variable pop_change.

Step 6:
Before we calculate the annual percentage growth rate, we need to calculate the percentage growth rate. This is the percentage with which a population changes, but doesn’t account for period of time during which the change takes place.

We can calculate percentage growth rate using the following formula:

percentage_gr = ((pop_present - pop_past)/pop_past) * 100

Create the variable percentage_gr.

Using the variable pop_change, calculate the annual percentage growth rate between 1927 and 2017 and assign the result to the variable percentage_gr.

Step 7:
Now that we have the percentage growth rate, we can calculate the annual percentage growth. Create a variable for annual_gr.

To calculate the annual percentage growth, take the result of the variable percentage_gr and divide it by the number of years elapsed. Set the result equal to the variable annual_gr.

Write a Function:
Step 8:
It would be good to reuse this formula again. Let’s turn it into a function called population_growth. First, start by defining the function.

Step 9:
When we wrote our earlier program, we used a set of variables to do our equations. We’re going to take some of those variables and turn them into arguments.
Give the function the following arguments: year_one, year_two, population_one, population_two.

Step 10:
Now we’re going to reconstruct the formula for calculating the annual percentage growth rate and set it equal to the variable growth_rate.
First, declare the variable growth_rate.

Step 11:
Next, use the arguments to re-create the formula for annual percentage growth rate. 

Step 12:
Have the function return the value of the variable growth_rate.

Calling a Function:
Step 13:
Now that we’ve defined our function, let’s call the function with the same set of numbers we used (population values for 1927 and 2017) and see if we get the same result as the value of annual_gr.

First, print the value of annual_gr to the terminal.

Step 14:
Call the function population_growth and save it to the variable set_one and print the results to the console. Did you get the same result as when you printed annual_gr?

Step 15:
Let’s try it again with another set of numbers. During the second part of the 20th century, Istanbul experience rapid population growth due to the expansion of the city limits and migration to the city from eastern Turkey in the 1980s. Let’s look at how the rate of change between 1950-2000 compares to the previous rate.

Call the function population_growth and have it calculate the rate of population change between 1950 and 2000. Save the function call to set_two and print it to the console.

Report:
Step 16:
Now, write a sentence that explains the change in population from 1927 to 2017, making use of your variables and string interpolation. Be sure to include the variables for the 1927 and 2017 population data, the change of population, and the annual growth rate of population. If you want to challenge yourself, you can also include the results of the rate of change between 1950 and 2000. Also feel free to find your own dataset!

Save the sentence to a variable called report and print the sentence to the terminal. 

