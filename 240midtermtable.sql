create table courses (
    studentName text,
    courseTerm text,
    studentAddress text,
    courseName text,
    numCredits int,
    buildingRoom text,
    instructorName text,
    instructorOffice text,
    courseGrade text
);

insert into courses values 
( "Ned Nedson", "Fall 2023", "456 Ned Street", "Intro to DB", 3, "LA/202", "Master Ned", "SS/102", "F"),
( "Ted Tedson", "Fall 2023", "123 Ted Street", "OS and CMD line", 3, "SS/200", "Master Zed", "LA/101", "A"),
( "Ted Tedson", "Spring 2024", "123 Ted Street", "Python++", 3, "LA/201", "Master Zed", "LA/101", "B"),
( "Ned Nedson", "Fall 2024", "456 Ned Street", "Intro to DB", 3, "LA/202", "Master Ned", "SS/102", NULL),
( "Ted Tedson", "Fall 2024", "123 Ted Street", "Intro to DB", 3, "LA/202", "Master Ned", "SS/102", NULL);