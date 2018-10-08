DELETE P1
FROM Person p1
JOIN Person p2 on p1.Email = p2.Email
AND p1.ID > p2.ID