DROP DATABASE IF EXISTS gradesystem;
CREATE DATABASE gradesystem;
USE gradesystem;
CREATE TABLE student(
	sid int(10) AUTO_INCREMENT PRIMARY KEY,
	sname varchar(10),
	gender varchar(10)
);
INSERT INTO student values(1,'Tom','male'),(2,'Jack','male'),(3,'Rose','female');
CREATE TABLE course(
	cid int(10) AUTO_INCREMENT PRIMARY KEY,
	cname varchar(20),
	UNIQUE(cname)
);
INSERT INTO course values(1,'math'),(2,'physics'),(3,'chemistry');
CREATE TABLE mark(
	mid int(10) AUTO_INCREMENT PRIMARY KEY,
	sid int(10),
	cid int(10),
	score int(3),
	FOREIGN KEY (sid) REFERENCES student(sid),
	FOREIGN KEY (cid) REFERENCES course(cid)
);
INSERT INTO mark values(1,1,1,80),(2,2,1,85),(3,3,1,90),(4,1,2,60),(5,2,2,90),(6,3,2,75),(7,1,3,95),(8,2,3,75),(9,3,3,85);
