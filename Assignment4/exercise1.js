
class Person{
    constructor(first, lastName, age){
        this.firstName=first;
        this.lastName=lastName;
        this.age=age;
    }

    fullName = () => {
        return this.firstName + " " + this.lastName;
    }
}

class Student extends Person{
    constructor(firstName, lastName, age, gpa, status, id){
        super(firstName, lastName, age);
        this.gpa=gpa;
        this.status=status;
        this.id=id;
    }

    part1 = () => {
        return this.fullName() + "("+this.gpa+")";
    }
}
const students = [ 
    new Student("Mike", "Smith", 21, 3.7, 4, 100), 
    new Student("Larry", "Mushroom", 19, 2.1, 2, 101),
    new Student("Marry", "Wolf", 22, 3.2, 4, 102),
    new Student("Tommy", "Tree", 20, 3.5, 2, 103),
    new Student("Laura", "Tall", 21, 3.1, 3, 104),
    new Student("Amy", "Paris", 18, 3.9, 1, 105)
]


function sort_student(students, field) {

    if(field === "name"){
    
    return students.sort(function(a, b){ return b.name - a.name});
    
    }else if(field === "gpa"){
    
    return students.sort(function(a, b){ return b.gpa - a.gpa});
    
    } else if(field === "id"){
    
    return students.sort(function(a, b){ return b.id - a.id});
    
    }
}


console.log(sort_student(students, "id"))
students.sort((a,b) => b.gpa - a.gpa);
// const displays = document.querySelector("#display");
// students.forEach(student => displays.innerHTML += student.part1()+" " );



