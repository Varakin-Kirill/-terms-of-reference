delete from dep2 a using dep2 b 
where a.ctid < b.ctid 
and a.id=b.id