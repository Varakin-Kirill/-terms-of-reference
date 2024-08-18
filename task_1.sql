with users as (select dep.name, count(*) 
			   from emp left join dep on dep.id = emp.dep_id 
			   group by dep.name, emp.name having count(*) > 1
			  ) 
select name, sum(count) from users group by name;