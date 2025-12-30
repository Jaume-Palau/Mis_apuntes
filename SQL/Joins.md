## 🔥 Mini-resumen para memorizar:

- INNER JOIN → solo coincidencias
- LEFT JOIN → todo lo de la izquierda
- RIGHT JOIN → todo lo de la derecha
- FULL OUTER JOIN → todos (no existe en MySQL)
- CROSS JOIN → combinaciones de todo con todo
- IN → compara con una lista
- EXISTS → comprueba existencia (TRUE/FALSE)

## Joins:

| Operación       | Qué devuelve                                                                        | Uso típico                                                     | Sintaxis básica                                        |
| --------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------ |
| INNER JOIN      | Solo filas con coincidencia en ambas tablas                                         | Relacionar tablas cuando solo interesa lo que coincide         | SELECT ... FROM t1 JOIN t2 ON t1.col = t2.col;         |
| LEFT JOIN       | Todas las filas de la izquierda + coincidencias de la derecha (NULL si no coincide) | Mantener filas de la tabla principal aunque no tengan relación | SELECT ... FROM t1 LEFT JOIN t2 ON t1.col = t2.col;    |
| RIGHT JOIN      | Todas las filas de la derecha + coincidencias de la izquierda                       | Igual que LEFT pero prioriza la tabla de la derecha            | SELECT ... FROM t1 RIGHT JOIN t2 ON t1.col = t2.col;   |
| FULL OUTER JOIN | Todas las filas de ambas tablas, coincidan o no                                     | MySQL NO lo soporta                                            | Se simula con LEFT JOIN + RIGHT JOIN + UNION           |
| CROSS JOIN      | Producto cartesiano (todas las combinaciones posibles)                              | Casos raros, generar combinaciones                             | SELECT ... FROM t1 CROSS JOIN t2;                      |
| IN              | Valores que existen en una lista o subconsulta                                      | Subconsultas simples                                           | WHERE t1.col IN (SELECT col FROM t2);                  |
| EXISTS          | TRUE si la subconsulta devuelve filas                                               | Subconsultas dependientes, más eficiente que IN                | WHERE EXISTS (SELECT 1 FROM t2 WHERE t2.col = t1.col); |

## Índices:

| Tipo de índice | Sintaxis                                                                                                             | Para qué sirve                                         | Notas importantes                                          |
| -------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------- |
| BTREE (normal) | CREATE INDEX idx_nombre ON tabla(columna);                                                                           | Búsquedas generales, WHERE, ORDER BY, GROUP BY, rangos | Índice por defecto en InnoDB. Ideal para rangos            |
| HASH           | No se crea en InnoDB; solo automático en tablas MEMORY                                                               | Búsquedas por igualdad (=)                             | No soporta USING HASH en InnoDB                            |
| FULLTEXT       | CREATE FULLTEXT INDEX idx_texto ON tabla(columna1, columna2); MATCH(col1, col2) AGAINST('palabras' IN BOOLEAN MODE); | Búsqueda de texto largo                                | +palabra obligatoria, -palabra excluida, solo TEXT/VARCHAR |
