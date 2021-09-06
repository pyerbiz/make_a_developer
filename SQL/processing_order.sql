-- FROM
-- WHERE
-- GROUP BY
-- HAVING
-- SELECT
-- ORDER BY
-- PAGING

select * from staff;
select 'SQL is fun' from staff;
select *, 'SQL is fun' from staff;


-- forced join order, type chiastic order

 select *
  	from public.animals a
 	left join  vaccinations v
 	inner join public.persons p on p.email = v.email
 	inner join public.staff_assignments sa on sa.email = p.email
 	on a."name" =v."name" and a.species =v.species;
