SELECT M.Name, M.Surname, D.OrderNumbers, D.Summary  FROM Docs D
JOIN Manager M on D.Manager = M.Number
WHERE doc_year = %s AND doc_month = %s;