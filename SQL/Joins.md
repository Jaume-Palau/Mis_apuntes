## 🔥 Mini-resumen para memorizar:

- INNER JOIN → solo coincidencias
- LEFT JOIN → todo lo de la izquierda
- RIGHT JOIN → todo lo de la derecha
- FULL OUTER JOIN → todos (no existe en MySQL)
- CROSS JOIN → combinaciones de todo con todo
- IN → compara con una lista
- EXISTS → comprueba existencia (TRUE/FALSE)

## Joins:

| Operación             | Qué devuelve                                                                        | Uso típico                                                     | Sintaxis básica                                                                         |
| --------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **INNER JOIN (JOIN)** | Solo filas con coincidencia en ambas tablas                                         | Relacionar tablas cuando solo quieres lo que coincide          | `sql<br>SELECT ...<br>FROM t1<br>JOIN t2 ON t1.col = t2.col;<br>`                       |
| **LEFT JOIN**         | Todas las filas de la izquierda + coincidencias de la derecha (NULL si no coincide) | Mantener filas de la tabla principal aunque no tengan relación | `sql<br>SELECT ...<br>FROM t1<br>LEFT JOIN t2 ON t1.col = t2.col;<br>`                  |
| **RIGHT JOIN**        | Todas las filas de la derecha + coincidencias de la izquierda (NULL si no coincide) | Igual que LEFT JOIN, pero prioriza la tabla de la derecha      | `sql<br>SELECT ...<br>FROM t1<br>RIGHT JOIN t2 ON t1.col = t2.col;<br>`                 |
| **FULL OUTER JOIN**   | Todas las filas de ambas tablas, coincidan o no                                     | _MySQL NO lo soporta._ Se simula con LEFT + RIGHT + UNION      | `sql<br>-- NO existe en MySQL<br>-- Se simula con UNION<br>`                            |
| **CROSS JOIN**        | Producto cartesiano (todas las combinaciones posibles)                              | Casos muy específicos, rara vez útil                           | `sql<br>SELECT ...<br>FROM t1<br>CROSS JOIN t2;<br>`                                    |
| **IN**                | Filas donde un valor está dentro de una lista devuelta por una subconsulta          | Subconsulta simple que devuelve valores                        | `sql<br>WHERE t1.col IN (<br>  SELECT col FROM t2<br>);<br>`                            |
| **EXISTS**            | TRUE si la subconsulta devuelve al menos una fila                                   | Subconsulta dependiente; más eficiente que IN en muchos casos  | `sql<br>WHERE EXISTS (<br>  SELECT 1<br>  FROM t2<br>  WHERE t2.col = t1.col<br>);<br>` |

## Índices:

| Tipo de índice        | Sintaxis                                                                                                                    | Para qué sirve                                                                                     | Notas importantes                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **BTREE (el normal)** | `CREATE INDEX idx_nombre ON tabla(columna);`                                                                                | Búsquedas generales, comparaciones, `WHERE`, `ORDER BY`, `GROUP BY`, rangos (`>`, `<`, `BETWEEN`). | Es el índice por defecto en InnoDB. Ideal para búsquedas por rangos.                                    |
| **HASH**              | _En MySQL solo existe automáticamente en tablas MEMORY._<br>_No se crea manualmente._                                       | Búsquedas de igualdad exacta (`=`). Muy rápido para `=` pero no sirve para rangos.                 | InnoDB **NO** soporta `USING HASH`. Por eso a tu profe “no le funcionaba”.                              |
| **FULLTEXT**          | `CREATE FULLTEXT INDEX idx_texto ON tabla(columna1, columna2);`<br>`MATCH(col1, col2) AGAINST('palabras' IN BOOLEAN MODE);` | Búsqueda de texto grande: frases, artículos, texto natural, ranking por relevancia.                | `+palabra` → obligatoria<br>`-palabra` → excluida<br`palabra` → opcional. Solo funciona en TEXT/VARCHAR |
