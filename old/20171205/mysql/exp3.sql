use gradesystem;
delimiter //
create trigger trigger_modify before update on mark
for each row begin
	insert into modifymark(m_sid,m_cid,m_score,m_time) values(new.sid,new.cid,new.score,now());
end
//
create procedure math_proc()
begin
select cname,sname,score from student,course,mark where student.sid=mark.sid and course.cid=mark.cid and cname='math' order by score desc;
end
//
delimiter ;
update mark set score=score+3 where sid=(select sid from student where sname='Tom') and cid=(select cid from course where cname='chemistry');
create user 'testuser'@'localhost' identified by '123456';
grant select to 'testuser'@'localhost' on gradesystem.*;
