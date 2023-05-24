create database sailors;
use sailors;

create table sailors(SID numeric primary key,
                     sname varchar(20),
                     rating int,
                     age float);
                     
insert into sailors values(1,'Dustin',7,45.0),(2,'Brutus',1,33.0),(3,'Laura',8,55.5),
							(4,'Andy',8,25.5),(5,'Rusty',10,35.0),(6,'Horatio',7,55.0),(7,'Zelda',10,48.0)
                            ,(8,'Horatio',9,45.70),(9,'Amy',3,45.89),(10,'Bob',3,42.67);
                            
select sname,rating from sailors where rating > (select rating from sailors where sname = 'Dustin');
select sname from sailors where rating= all (select max(rating) from sailors);


create view expert_sailors as select * from sailors where rating > 7;
select * from expert_sailors;
drop view expert_sailors;

select * from sailors order by sname asc;
select * from sailors order by rating ,age desc;
select * from sailors order by rating ,age asc;
select rating,min(age) from sailors group by rating;
select rating,min(age) from sailors where age >= 18 group by rating;

select max(age) from sailors;
select avg(distinct age) from sailors;
select sum(rating) from sailors;
select  min(age) from sailors;

select * from sailors where sname like 'b_%';
select SID,sname,rating+100,age from sailors;
select rating+10 from sailors;

ALTER table sailors add(gender varchar(20));
alter table sailors drop gender;
alter table sailors modify gender varchar(10);
rename table sail to sailors;
truncate table sailors;

select * from sailors where rating = 3;
update sailors set  rating = 2 where SID = 2;
select * from sailors where rating <> 7;

select * from sailors;

create table boat(BID numeric unique,
                  sname varchar(20),
                  color varchar(20));
insert into boat values(1,'interlake','blue');
insert into boat values(2,'interlake','red');
insert into boat values(3,'clipper','green');
insert into boat values(4,'marine','red');
select *from boat;
select count(BID) from boat;

create table reserve(RID numeric unique,
                  SID numeric ,
                  BID numeric ,
                  rdate varchar(20),
                  duration int);
                  
insert into reserve values(1,1,1,'10-10-07','60');
insert into reserve values(2,1,1,'10-10-07','60');
insert into reserve values(3,1,1,'10-10-07','60');
insert into reserve values(4,5,1,'10-10-07','60');
insert into reserve values(5,3,1,'10-10-07','60');
insert into reserve values(6,6,1,'10-10-07','60');
insert into reserve values(7,5,6,'10-10-07','60');
insert into reserve values(8,6,1,'16-10-07','60');
insert into reserve values(9,7,6,'10-10-07','60');
insert into reserve values(10,2,1,'10-10-07','60');
insert into reserve values(12,10,9,'25-12-22',60);

select sname from sailors where SID IN (select SID from reserve where BID = 1);
SELECT sname FROM sailors where SID IN(select SID from reserve where BID=1 AND 2 AND 3 AND 4 );

update reserve set rdate = '26-12-22' where RID = 11;
delete from reserve where RID = 11;
select * from reserve;
select RID,SID,rdate from reserve;
delete from sailors where SID = 1;
select count(distinct BID ) from reserve;

select * from sailors where age>=35;
select * from sailors where rating<10 and rating>35;
select * from boat where color='red';