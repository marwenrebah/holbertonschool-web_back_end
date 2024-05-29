export default function getStudentsByLocation(student, City) {
  if (!Array.isArray(student)) {
    return [];
  }
  return student.filter((student) => student.location === City);
}
