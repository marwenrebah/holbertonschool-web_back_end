# 📝 ES6 data manipulation

## 🚀 Functions Overview

### 1. `getListStudents()`
Returns a list of predefined students.
```javascript
export default function getListStudents() {
  const data = [
    { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
    { id: 2, firstName: 'James', location: 'Columbia' },
    { id: 5, firstName: 'Serena', location: 'San Francisco' },
  ];
  return data;
}
```

### 2. `getListStudentIds(students)`
Returns an array of student IDs from the provided student list.
```javascript
export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  return students.map((student) => student.id);
}
```

### 3. `getStudentsByLocation(students, city)`
Filters students by their location.
```javascript
export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }
  return students.filter((student) => student.location === city);
}
```
### 4. `getStudentIdsSum(students)`
Calculates the sum of all student IDs.
```javascript
export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return 0;
  }
  return students.reduce((sum, student) => sum + student.id, 0);
}

```
### 5. `getStudentsByLocation(students, city, newGrades)`
Filters students by location and updates their grades.
```javascript
export default function getStudentsByLocation(students, city, newGrades) {
  if (!Array.isArray(students) || !Array.isArray(newGrades)) {
    return [];
  }

  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const newGrade = newGrades.find((grade) => grade.studentId === student.id);
      return { ...student, grade: newGrade ? newGrade.grade : 'N/A' };
    });
}

```
### 6. `createInt8TypedArray(length, position, value)`
Creates an `Int8` typed array with a specific value at a given position.
```javascript
export default function createInt8TypedArray(length, position, value) {
  if (position >= length) throw new Error('Position outside range');
  const buffer = new DataView(new ArrayBuffer(length));
  buffer.setInt8(position, value);
  return buffer;
}

```
### 7. `setFromArray(array)`
Creates a set from an array.
```javascript
export default function setFromArray(array) {
  return new Set(array);
}

```
### 8. `hasValuesFromArray(set, array)`
Checks if all elements of an array are present in a set.
```javascript
export default function hasValuesFromArray(set, array) {
  const check = array.every((item) => set.has(item));
  return check;
}

```
### 9. `cleanSet(set, startString)`
Cleans a set by removing a specific start string from each element.
```javascript
export default function cleanSet(set, startString) {
  if (typeof set !== 'object' || typeof startString !== 'string' || startString.length === 0) {
    return '';
  }

  return [...set]
    .filter((item) => item.startsWith(startString))
    .map((item) => item.slice(startString.length))
    .join('-');
}

```
### 10. `groceriesList()`
Creates a map of grocery items with their quantities.
```javascript
export default function groceriesList() {
  const groceries = new Map();
  groceries.set('Apples', 10);
  groceries.set('Tomatoes', 10);
  groceries.set('Pasta', 1);
  groceries.set('Rice', 1);
  groceries.set('Banana', 5);

  return groceries;
}

```
### 11. `updateUniqueItems(map)`
Updates the values of unique items in a map to 100.
```javascript
export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw Error('Cannot process');
  }

  for (const [key] of map) {
    if (map.get(key) === 1) map.set(key, 100);
  }
  return map;
}
```

## 📂 Directory Structure

ES6_data_manipulation/
│
├── getListStudents.js
├── getListStudentIds.js
├── getStudentsByLocation.js
├── getStudentIdsSum.js
├── createInt8TypedArray.js
├── setFromArray.js
├── hasValuesFromArray.js
├── cleanSet.js
├── groceriesList.js
└── updateUniqueItems.js
├── README.md
└── package.json

## 👥 Author
🚀 Marwen Rebah<br>
📧 Email: 6863@holbertonstudents.com<br>
👻 Github: https://github.com/marwenrebah
