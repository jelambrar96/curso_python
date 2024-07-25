# Consultas útiles Chinook

## Básico

1. Proporciona una consulta que muestre los Clientes (solo sus nombres completos, ID de cliente y país) que no están en los EE.UU.
```sql
select customerid, firstname, lastname, country
from customer
where not country = 'USA';
```

2. Proporciona una consulta que solo muestre los Clientes de Brasil.
```sql
select * from customer
where country = 'Brazil';
```

3. Proporciona una consulta que muestre las Facturas de clientes que son de Brasil. La tabla resultante debe mostrar el nombre completo del cliente, ID de factura, fecha de la factura y el país de facturación.
```sql
select c.firstname, c.lastname, i.invoiceid, i.invoicedate, i.billingcountry
from customer as c, invoice as i
where c.country = 'Brazil' and
c.customerid = i.customerid;
```

4. Proporciona una consulta que solo muestre los Empleados que son Agentes de Ventas.
```sql
select * from employee
where employee.title = 'Sales Support Agent';
```

5. Proporciona una consulta que muestre una lista única de países de facturación de la tabla de Facturas.
```sql
select distinct billingcountry from invoice;
```

6. Proporciona una consulta que muestre las facturas de clientes que son de Brasil.
```sql
select *
from customer as c, invoice as i
where c.country = 'Brazil' and
c.customerid = i.customerid;
```

## Intermedio


7. Proporciona una consulta que muestre las facturas asociadas con cada agente de ventas. La tabla resultante debe incluir el nombre completo del Agente de Ventas.
```sql
select e.firstname, e.lastname, i.invoiceid, i.customerid, i.invoicedate, i.billingaddress, i.billingcountry, i.billingpostalcode, i.total
from customer as c, invoice as i
on c.customerid = i.customerid
join employee as e
on e.employeeid = c.supportrepid
order by e.employeeid;
```

8. Proporciona una consulta que muestre el Total de la Factura, nombre del Cliente, País y nombre del Agente de Ventas para todas las facturas y clientes.
```sql
select e.firstname as 'employee first', e.lastname as 'employee last', c.firstname as 'customer first', c.lastname as 'customer last', c.country, i.total
from employee as e
	join customer as c on e.employeeid = c.supportrepid
	join invoice as i on c.customerid = i.customerid
```

9. ¿Cuántas Facturas hubo en 2009 y 2011? ¿Cuáles son las ventas totales respectivas para cada uno de esos años?
```sql
select count(i.invoiceid), sum(i.total)
from invoice as i
where i.invoicedate between datetime('2011-01-01 00:00:00') and datetime('2011-12-31 00:00:00');
```
```sql
select count(i.invoiceid), sum(i.total)
from invoice as i
where i.invoicedate between datetime('2009-01-01 00:00:00') and datetime('2009-12-31 00:00:00');
```

10. Mirando la tabla de InvoiceLine, proporciona una consulta que CUENTE el número de elementos de línea para la Factura ID 37.
```sql
select count(i.invoicelineid)
from invoiceline as i
where i.invoiceid = 37
```

11. Mirando la tabla de InvoiceLine, proporciona una consulta que CUENTE el número de elementos de línea para cada Factura. PISTA: [GROUP BY](http://www.sqlite.org/lang_select.html#resultset)
```sql
select invoiceid, count(invoicelineid)
from invoiceline
group by invoiceid
```

12. Proporciona una consulta que incluya el nombre de la pista con cada elemento de línea de factura.
```sql
select i.*, t.name
from invoiceline as i, track as t
on i.trackid = t.trackid
```

13. Proporciona una consulta que incluya el nombre de la pista comprada Y el nombre del artista con cada elemento de línea de factura.
```sql
select i.*, t.name as 'track', ar.name as 'artist'
from invoiceline as i
	join track as t on i.trackid = t.trackid
	join album as al on al.albumid = t.albumid
	join artist as ar on ar.artistid = al.artistid
```

14. Proporciona una consulta que muestre el número de facturas por país. PISTA: [GROUP BY](http://www.sqlite.org/lang_select.html#resultset)
```sql
select billingcountry, count(billingcountry) as '# of invoices'
from invoice
group by billingcountry
```

15. Proporciona una consulta que muestre el número total de pistas en cada lista de reproducción. El nombre de la lista de reproducción debe incluirse en la tabla resultante.
```sql
select *, count(trackid) as '# of tracks'
from playlisttrack, playlist
on playlisttrack.playlistid = playlist.playlistid
group by playlist.playlistid
```

16. Proporciona una consulta que muestre todas las Pistas, pero no muestre ningún ID. La tabla resultante debe incluir el nombre del Álbum, Tipo de Medio y Género.
```sql
select t.name as 'track', t.composer, t.milliseconds, t.bytes, t.unitprice, a.title as 'album', g.name as 'genre', m.name as 'media type'
from track as t
	join album as a on a.albumid = t.albumid
	join genre as g on g.genreid = t.genreid
	join mediatype as m on m.mediatypeid = t.mediatypeid
```

17. Proporciona una consulta que muestre todas las Facturas pero incluya el número de elementos de línea de factura.
```sql
select invoice.*, count(invoiceline.invoicelineid) as '# of line items'
from invoice, invoiceline
on invoice.invoiceid = invoiceline.invoiceid
group by invoice.invoiceid
```

## Avanzado


18. Proporciona una consulta que muestre las ventas totales realizadas por cada agente de ventas.
```sql
select e.*, count(i.invoiceid) as 'Total Number of Sales'
from employee as e
	join customer as c on e.employeeid = c.supportrepid
	join invoice as i on i.customerid = c.customerid
group by e.employeeid
```

19. ¿Qué agente de ventas realizó más ventas en 2009?
```sql
select *, max(total) from
(select e.*, sum(total) as 'Total'
from employee as e
	join customer as c on e.employeeid = c.supportrepid
	join invoice as i on i.customerid = c.customerid
where i.invoicedate between '2009-01-00' and '2009-12-31'
group by e.employeeid)
```

20. ¿Qué agente de ventas realizó más ventas en 2010?
```sql
select *, max(total) from
(select e.*, sum(total) as 'Total'
from employee as e
	join customer as c on e.employeeid = c.supportrepid
	join invoice as i on i.customerid = c.customerid
where i.invoicedate between '2010-01-00' and '2010-12-31'
group by e.employeeid)
```

21. ¿Qué agente de ventas realizó más ventas en general?
```sql
select *, max(total) from
(select e.*, sum(total) as 'Total'
from employee as e
	join customer as c on e.employeeid = c.supportrepid
	join invoice as i on i.customerid = c.customerid
group by e.employeeid)
```

22. Proporciona una consulta que muestre el número de clientes asignados a cada agente de ventas.
```sql
select e.*, count(c.customerid) as 'TotalCustomers'
from employee as e
	join customer as c on e.employeeid = c.supportrepid
group by e.employeeid
```

23. Proporciona una consulta que muestre las ventas totales por país. ¿Qué país gastó más?
```sql
select i.billingcountry, sum(total) as 'TotalSales'
from invoice as i
group by billingcountry
order by totalsales desc
```

24. Proporciona una consulta que muestre la pista más comprada de 2013.
```sql
select *, count(t.trackid) as count
from invoiceline as il
	join invoice as i on i.invoiceid = il.invoiceid
	join track as t on t.trackid = il.trackid
where i.invoicedate between '2013-01-01' and '2013-12-31'
group by t.trackid
order by count desc
```

25. Proporciona una consulta que muestre las 5 pistas más compradas en general.

26. Proporciona una consulta que muestre los 3 artistas más vendidos.

27. Proporciona una consulta que muestre el Tipo de Medio más comprado.

---

Sigue el perfil del creador de GPT en LinkedIn