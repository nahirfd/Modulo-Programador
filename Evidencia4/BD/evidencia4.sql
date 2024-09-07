-- MOSTRAR Listado de bases de datos------------------------------------------------------------------------
-- SHOW DATABASES;

-- USO de bases de dato------------------------------------------------------------------------------------
-- USE evidencia4;

-- CREAR TABLAS---------------------------------------------------------------------------------------------
-- CREATE TABLE aspiradora_inalámbrica(
-- aspiradora_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
-- nombre VARCHAR(45) NOT NULL,
-- modelo VARCHAR(45) NOT NULL,
-- potencia VARCHAR(45) NOT NULL,
-- color VARCHAR(45) NOT NULL,
-- id_marca INT NOT NULL,
-- FOREIGN KEY(`id_marca`) REFERENCES `marcas`(`id_marca`)
-- );

-- ALTER TABLE aspiradora_inalámbrica
-- ADD COLUMN precio INT NOT NULL;

-- AGREGAR VALORES EN TABLA aspiradora ---------------------------------------------------------------------------------------------
-- INSERT INTO aspiradora_inalámbrica (nombre, modelo, potencia, color, id_marca, precio)
-- VALUES 
-- ('aspiradora de mano', 'AS-7654', '94W', 'gris', 1, 60000),
-- ('Aspiradora Trineo Con Bolsa Ultracomb ', 'AS-4201', '1400W', 'negro', 3, 300000),
-- ('Aspiradora Robot Sin Bolsa', 'AS-8080', 'AS-3000', 'plateado', 2, 193000 );

-- SELECT * FROM aspiradora_inalámbrica;

-- UPDATE aspiradora_inalámbrica
-- SET potencia = '2000W'
-- WHERE aspiradora_id = 3;

-- UPDATE aspiradora_inalámbrica
-- SET precio = 90500
-- WHERE aspiradora_id = 2;

-- CREATE TABLE `marcas`(
--  `id_marca` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
-- 	`nombre` VARCHAR(30) NOT NULL,
--  `id_fabricante` INT NOT NULL,
-- 	FOREIGN KEY (id_fabricante) REFERENCES fabricantes(id_fabricante)
-- );

-- AGREGAR VALORES EN TABLA marcas ---------------------------------------------------------------------------------------------
-- INSERT INTO `marcas` (nombre, id_fabricante)
-- VALUES 
-- ('ATMA',1), 
-- ('Samsung',2), 
-- ('Ultracomb',3);

	
--  CREATE TABLE `fabricantes`(
--  `id_fabricante` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
-- 	`nombre` VARCHAR(30) NOT NULL,
--  `pais` VARCHAR(30) NOT NULL
-- );

-- AGREGAR VALORES EN TABLA fabricantes---------------------------------------------------------------------------------------------
-- INSERT INTO `fabricantes` (nombre, pais)
-- VALUES 
-- ('ATMA','Argentina'), 
-- ('Samsung','Corea del Sur'), 
-- ('Ultracomb','Argentina');


-- SELECT * FROM fabricantes;

-- UPDATE fabricantes
-- SET nombre = 'Newsan'
-- WHERE id_fabricante = 1;

-- SELECT CONCAT(nombre, ': $', precio) AS lista_precios FROM aspiradora_inalámbrica;
-- SELECT * FROM marcas LIMIT 2;
-- SELECT * FROM fabricantes WHERE pais = 'Argentina';
-- SELECT * FROM aspiradora_inalámbrica WHERE precio < 100000;
-- SELECT * FROM aspiradora_inalámbrica WHERE color = 'negro';
-- SELECT nombre FROM marcas;


-- Mostrar valores con Where y between
-- SELECT nombre FROM fabricantes WHERE id_fabricante between 1 and 2;

-- Mostrar valores con Where y limit
-- Select * FROM aspiradora_inalámbrica WHERE aspiradora_id = 1 LIMIT 2;


-- Mostrar información completa de las aspiradoras junto con la marca y el fabricante
-- SELECT ai.aspiradora_id, ai.nombre AS nombre_aspiradora, ai.modelo, ai.potencia, ai.color, ai.precio,
--        m.nombre AS nombre_marca, f.nombre AS nombre_fabricante, f.pais
-- FROM aspiradora_inalámbrica ai
-- INNER JOIN marcas m ON ai.id_marca = m.id_marca
-- INNER JOIN fabricantes f ON m.id_fabricante = f.id_fabricante;

-- Mostrar información completa de las aspiradoras cuyo fabricante sea del pais Argentina
-- SELECT ai.aspiradora_id, ai.nombre AS nombre_aspiradora, ai.modelo, ai.potencia, ai.color, ai.precio,
--        m.nombre AS nombre_marca, f.nombre AS nombre_fabricante, f.pais
-- FROM aspiradora_inalámbrica ai
-- INNER JOIN marcas m ON ai.id_marca = m.id_marca
-- INNER JOIN fabricantes f ON m.id_fabricante = f.id_fabricante
-- WHERE f.pais = 'Argentina';

-- Mostrar solo la columna nombre de las tablas aspiradoras y marcas.
-- SELECT ai.nombre AS nombre_aspiradora, m.nombre AS nombre_marca
-- FROM aspiradora_inalámbrica AS ai
-- INNER JOIN marcas AS m ON ai.id_marca = m.id_marca;
