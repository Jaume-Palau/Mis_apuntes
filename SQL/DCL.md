# DATA CONTROL LANGUAGE (DCL)

**Gestiona usuarios, permisos y seguridad de la base de datos.**

## Creacion de usuarios

| Comando       | Descripción                             | Ejemplo                                                |
| ------------- | --------------------------------------- | ------------------------------------------------------ |
| `CREATE USER` | Crea un nuevo usuario en MySQL.         | `CREATE USER 'juan'@'localhost' IDENTIFIED BY '1234';` |
| `DROP USER`   | Elimina un usuario.                     | `DROP USER 'juan'@'localhost';`                        |
| `ALTER USER`  | Modifica un usuario (contraseña, etc.). | `ALTER USER 'juan'@'localhost' IDENTIFIED BY 'abcd';`  |


# Privilegios y permisos

## Privilegios a nivel GLOBAL

| Comando  | Descripción                               | Ejemplo                                                 |
| -------- | ----------------------------------------- | ------------------------------------------------------- |
| `GRANT`  | Otorga privilegios globales a un usuario. | `GRANT ALL PRIVILEGES ON *.* TO 'juan'@'localhost';`    |
| `REVOKE` | Revoca privilegios globales a un usuario. | `REVOKE ALL PRIVILEGES ON *.* FROM 'juan'@'localhost';` |


## Privilegios a nivel BASE DE DATOS

| Comando  | Descripción                              | Ejemplo                                                   |
| -------- | ---------------------------------------- | --------------------------------------------------------- |
| `GRANT`  | Otorga permisos sobre una base de datos. | `GRANT SELECT, INSERT ON tienda.* TO 'juan'@'localhost';` |
| `REVOKE` | Revoca permisos sobre una base de datos. | `REVOKE INSERT ON tienda.* FROM 'juan'@'localhost';`      |


## Privilegios a nivel TABLA

| Comando  | Descripción                               | Ejemplo                                                     |
| -------- | ----------------------------------------- | ----------------------------------------------------------- |
| `GRANT`  | Otorga permisos sobre una tabla concreta. | `GRANT SELECT ON tienda.clientes TO 'juan'@'localhost';`    |
| `REVOKE` | Revoca permisos sobre una tabla concreta. | `REVOKE SELECT ON tienda.clientes FROM 'juan'@'localhost';` |


## Privilegios a nivel COLUMNA

| Comando  | Descripción                               | Ejemplo                                                                |
| -------- | ----------------------------------------- | ---------------------------------------------------------------------- |
| `GRANT`  | Otorga permisos sobre columnas concretas. | `GRANT SELECT(nombre, edad) ON tienda.clientes TO 'juan'@'localhost';` |
| `REVOKE` | Revoca permisos sobre columnas concretas. | `REVOKE SELECT(nombre) ON tienda.clientes FROM 'juan'@'localhost';`    |


## Privilegios sobre PROCEDIMIENTOS y FUNCIONES

| Comando  | Descripción                                       | Ejemplo                                                                  |
| -------- | ------------------------------------------------- | ------------------------------------------------------------------------ |
| `GRANT`  | Otorga permisos sobre procedimientos o funciones. | `GRANT EXECUTE ON PROCEDURE tienda.calc_total TO 'juan'@'localhost';`    |
| `REVOKE` | Revoca permisos sobre procedimientos o funciones. | `REVOKE EXECUTE ON PROCEDURE tienda.calc_total FROM 'juan'@'localhost';` |


## Roles

| Comando                  | Descripción                                             | Ejemplo                                                 |
| ------------------------ | ------------------------------------------------------- | ------------------------------------------------------- |
| `CREATE ROLE`            | Crea un nuevo rol.                                      | `CREATE ROLE 'rol_lectura';`                            |
| `GRANT` (permisos a rol) | Asigna permisos a un rol.                               | `GRANT SELECT ON tienda.* TO 'rol_lectura';`            |
| `GRANT` (rol a usuario)  | Asigna un rol a un usuario.                             | `GRANT 'rol_lectura' TO 'juan'@'localhost';`            |
| `SET DEFAULT ROLE`       | Define qué rol se activa por defecto al iniciar sesión. | `SET DEFAULT ROLE 'rol_lectura' TO 'juan'@'localhost';` |
| `REVOKE`                 | Quita un rol a un usuario.                              | `REVOKE 'rol_lectura' FROM 'juan'@'localhost';`         |
| `DROP ROLE`              | Elimina un rol.                                         | `DROP ROLE 'rol_lectura';`                              |

