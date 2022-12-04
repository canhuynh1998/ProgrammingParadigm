function Person(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.fullname = `${firstName} ${lastName}`;
  }
  
  Person.prototype.initialize = function () {
    return `${this.firstName} ${this.lastName}`;
  };

function Student(firstName, lastName, age){
    Person.call(this, firstName, lastName, age);
};

Student.prototype = Object.create(Person.prototype);
Student.prototype.constructor = Student;


Student.prototype.learn = function(subject){
    return `${this.fullname} just learned ${subject}`
}

const student = new Student("Mike", "Smith", 21);
document.querySelector("#display1").innerHTML += student.learn("CS152");