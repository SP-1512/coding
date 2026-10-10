/* Write your PL/SQL query statement below */
select p.firstname,p.lastname,a.city,a.state from
person p
left join 
Address a
on p.personid=a.personid
order by p.firstname;