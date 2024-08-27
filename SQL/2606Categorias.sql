select p.id, p.name
from categories c, products p
where p.id_categories = c.id
and c.name like 'super%'
