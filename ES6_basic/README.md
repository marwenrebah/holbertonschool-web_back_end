🚀 JavaScript Utility Functions 🛠️
This repository contains a collection of JavaScript utility functions for various tasks. Below is a brief overview of each function:

taskFirst()
Returns a string indicating a preference for using const when possible.


Copy code
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}
getLast()
Returns a string indicating that something is okay.


Copy code
export function getLast() {
  return ' is okay';
}
taskNext()
Combines a string with the result of getLast() function and returns the combination.


Copy code
export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
taskBlock(trueOrFalse)
Accepts a boolean argument and returns an array containing two boolean values based on the argument passed.


Copy code
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    // eslint-disable-next-line no-unused-vars, no-shadow
    const task = true;
    // eslint-disable-next-line no-unused-vars, no-shadow
    const task2 = false;
  }

  return [task, task2];
}
getNeighborhoodsList()
Defines a function to manage a list of San Francisco neighborhoods.


Copy code
export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  const self = this;
  this.addNeighborhood = (newNeighborhood) => {
    self.sanFranciscoNeighborhoods.push(newNeighborhood);
    return self.sanFranciscoNeighborhoods;
  };
}
getSumOfHoods(initialNumber, expansion1989, expansion2019)
Calculates the sum of initial number and two expansion values, with default values for the latter two.


Copy code
export default function getSumOfHoods(initialNumber, expansion1989 = 89, expansion2019 = 19) {
  return initialNumber + expansion1989 + expansion2019;
}
returnHowManyArguments(...args)
Returns the number of arguments passed to the function.


Copy code
export default function returnHowManyArguments(...args) {
  return args.length;
}
concatArrays(array1, array2, string)
Concatenates two arrays and a string and returns the result as a single array.


Copy code
export default function concatArrays(array1, array2, string) {
  return [...array1, ...array2, ...string];
}
getSanFranciscoDescription()
Returns a description of San Francisco's income, GDP, and GDP per capita based on data from 2017.


Copy code
export default function getSanFranciscoDescription() {
  const year = 2017;
  const budget = {
    income: '$119,868',
    gdp: '$154.2 billion',
    capita: '$178,479',
  };

  return `As of ${year}, it was the seventh-highest income county in the United States, with a per capita personal income of ${budget.income}. As of 2015, San Francisco proper had a GDP of ${budget.gdp}, and a GDP per capita of ${budget.capita}.`;
}
getBudgetObject(income, gdp, capita)
Creates and returns an object representing a budget with income, GDP, and capita properties.


Copy code
export default function getBudgetObject(income, gdp, capita) {
  const budget = {
    income,
    gdp,
    capita,
  };

  return budget;
}
getBudgetForCurrentYear(income, gdp, capita)
Creates and returns an object representing a budget for the current year, with income, GDP, and capita properties.


Copy code
import getBudgetObject from './7-getBudgetObject';

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {
    [`income-${getCurrentYear()}`]: income,
    [`gdp-${getCurrentYear()}`]: gdp,
    [`capita-${getCurrentYear()}`]: capita,
  };

  return budget;
}
getFullBudgetObject(income, gdp, capita)
Creates and returns an extended budget object with additional methods for formatting income.


Copy code
import getBudgetObject from './7-getBudgetObject';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    getIncomeInDollars(income) {
      return `$${income}`;
    },
    getIncomeInEuros(income) {
      return `${income} euros`;
    },
  };

  return fullBudget;
}
appendToEachArrayValue(array, appendString)
Appends a string to each value in an array and returns the new array.


Copy code
export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];
  for (const value of array) {
    newArray.push(appendString + value);
  }

  return newArray;
}
createEmployeesObject(departmentName, employees)
Creates and returns an object representing employees grouped by department.

Copy code
export default function createEmployeesObject(departmentName, employees) {
  return {
    [`${departmentName}`]: employees,
  };
}
createReportObject(employeesList)
Creates and returns a report object containing all employees and a method to get the number of departments.


Copy code
export default function createReportObject(employeesList) {
  return {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      return Object.keys(employeesList).length;
    },
  };
}
getCurrentYear()
Returns the current year using JavaScript's Date object.


Copy code
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}