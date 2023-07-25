SELECT client.last_name
FROM view
JOIN client ON client.id = view.client_id
JOIN apartment ON apartment.id = view.apartment_id
WHERE apartment.rooms >= 3
GROUP BY client.last_name
HAVING COUNT(DISTINCT view.apartment_id) >= 2;