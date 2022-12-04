
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
    constructor(firstName, lastName, age, gpa, status){
        super(firstName, lastName, age);
        this.gpa=gpa;
        this.status=status;
    }

    part1 = () => {
        return this.fullName() + "("+this.gpa+")";
    }
}
const students = [ 
    new Student("Mike", "Smith", 21, 3.7, 4), 
    new Student("Larry", "Mushroom", 19, 2.1, 2),
    new Student("Marry", "Wolf", 22, 3.2, 4),
    new Student("Tommy", "Tree", 20, 3.5, 2),
    new Student("Laura", "Tall", 21, 3.1, 3),
    new Student("Amy", "Paris", 18, 3.9, 1)
]

status_count = {}
students.forEach(student => {
    if (!(student.status in status_count)){
        status_count[student.status] = 0;
    } 
    status_count[student.status]++;
    })
let output = "";
Object.keys(status_count)
    .sort((a,b)=> status_count[a]-status_count[b])
    .forEach(key => {
        if(key === "1"){
            output+="Freshman: "+status_count[key]+" ";
        }else if(key === "2") {
            output+="Sophomore: "+status_count[key]+" ";
        }
        else if(key === "3") {
            output+="Junior: "+status_count[key]+" ";
        } else{
            output+="Senior: "+status_count[key]+" ";
        }
    });
document.querySelector("#display1").innerHTML = output;