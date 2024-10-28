-- >>> Relate Stadium with games <<<

-- Five Cities with greatest amount of Stadiums

select city, count(*) as occurrence
from venue
group by city
order by occurrence desc
limit 5

-- Top five Stadium by Capacity
-- Could get the team associated also

select * from venue
order by capacity desc
limit 5

-- Top five smallest

select * from venue
order by capacity
limit 5

-- Average Capacity

select AVG(capacity) from venue

-- Pizza Chart showing number of stadiums per surface type

select distinct surface, count(surface) from venue
group by surface

-- Removing nulls

delete from venue
where name = '0'
or address = '0'
or city = '0'
or country = '0'
or capacity = 0
or surface = '0'
or image = '0'

-- Join estádio e jogos
-- Verificar quais estádios tem mais jogos, etc


-- Capacidades 
SELECT * FROM public.venue
ORDER BY capacity ASC