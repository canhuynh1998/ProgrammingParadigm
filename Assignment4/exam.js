
class Person{
    constructor(name, age){
        this.name=name;
        this.age=age;
    }

    print_info = () => {
        return this.name + " " + this.age;
    }
}

class Artist extends Person{
    constructor(name, age, specialty){
        super(name, age);
        this.specialty=specialty;
    }

    artist_info = () => {
        return this.name + " " + this.age+" "+this.specialty ;
    }
}


const artists = [new Artist ("Test Artist 1", 21,"singing"), new Artist ("Test Artist 2", 29 , "singing" ), new Artist ("Test Artist 3", 22 , "dancing" ) ]

artists.forEach(artist => console.log(artist.artist_info()));

function sort_student(students, field) {

    if(field === "name"){
    
    return students.sort(function(a, b){ return b.name - a.name});
    
    }else if(field === "gpa"){
    
    return students.sort(function(a, b){ return b.gpa - a.gpa});
    
    } else if(field === "id"){
    
    return students.sort(function(a, b){ return b.id - a.id});
    
    }
}

