SELECT 
    COUNT(Mes) as qtd_mes,
    SUM(CASE WHEN CAST(Quantitativo AS INT) < 300 THEN 1 ELSE 0 END) as soma_quantitativo_menores_300,
    UTCNOW()
    FROM S3Object
    WHERE CAST(Quantitativo AS INT) >= 250 AND Mes <> 'Janeiro' AND CHAR_LENGTH(Mes) > 4