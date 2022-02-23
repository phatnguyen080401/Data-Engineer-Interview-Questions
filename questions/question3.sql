SELECT t.department, t.id, t.employee, t.salary
FROM (
      SELECT d.name as 'department', e.id, e.name as 'employee', e.salary,
             dense_rank() over(partition by e.departmentid order by salary desc) as nrank
      FROM Employee e
      JOIN Department d
      ON e.departmentid = d.id
) as t
WHERE t.nrank < 4