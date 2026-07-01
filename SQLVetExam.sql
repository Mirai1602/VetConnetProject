SELECT *
from Cita a Inner Join Paciente b On b.idMacota = a.idMacota


SELECT * from paciente 
 

SELECT  FORMAT(FechaCita ,'yyyyMM') AS MesCita, NombreEspecie, 
SUM (CASE WHEN Estado = 'Hecha' THEN 1 ELSE 0 END) AS CitasHechas, 
SUM (CASE WHEN Estado = 'Pendiente' THEN 1 ELSE 0 END) AS CitasPendientes 
from Cita a Inner Join Paciente b On b.idMacota = a.idMacota
Inner Join Raza c on b.CodigoRaza = c.CodigoRaza
Inner Join Especie d ON c.CodigoEspecie = d.CodigoEspecie
WHERE Estado IS NOT  NULL
group by  FORMAT(FechaCita ,'yyyyMM') , NombreEspecie
ORDER BY 2, 1 




