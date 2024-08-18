with sal as 
(select month, emp_id, sum(salary) over (partition by emp_id order by emp_id, month) 
  as running_total 
  from fin group by month, emp_id, salary)
  update fin set sum_salary = sal.running_total from sal where fin.emp_id = sal.emp_id and fin.month = sal.month;