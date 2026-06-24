
USE VetConnet;
GO

SELECT * FROM Persona;
SELECT * FROM Dueño;

select * from especie 
select * from Persona

INSERT INTO Persona (Nombre, Apellido, Telefono, Email) VALUES
('Carlos', 'Ramírez', '88889999', 'carlos.ramirez@email.com'),
('María', 'González', '77776666', 'maria.gonzalez@email.com'),
('José', 'Martínez', '55554444', 'jose.martinez@email.com'),
('Ana', 'Lopez', '99998888', 'ana.lopez@email.com'),
('Carla', 'Laurence', '86998788', 'Calra.Lau@email.com'),
('Luis', 'Torrez', '88887777', 'luis.torrez@email.com'),
('Valeria', 'Fernández', '77775555', 'valeria.fernandez@email.com'),
('Pablo', 'Pinzón', '66664444', 'pablo.pinzon@email.com'),
('Sonia', 'Martínez', '99997777', 'sonia.martinez@email.com'),
('Ricardo', 'Nuñez', '55553333', 'ricardo.nunez@email.com'),
('Elena', 'Rojas', '44442222', 'elena.rojas@email.com'),
('Fredy', 'Silva', '33331111', 'fredy.silva@email.com'),
('Lucía', 'Romero', '22220000', 'lucia.romero@email.com'),
('Noah', 'Brown', '11112222', 'noah.brown@email.com'),
('Patricia', 'Fernández', '10101010', 'patricia.fernandez@email.com'),
('Gabriel', 'Castro', '88881111', 'gabriel.castro@email.com'),
('Isabel', 'Mendoza', '77773333', 'isabel.mendoza@email.com'),
('Andrés', 'Vega', '66662222', 'andres.vega@email.com'),
('Claudia', 'Morales', '99994444', 'claudia.morales@email.com'),
('Fernando', 'Pérez', '55556666', 'fernando.perez@email.com'),
('Rosa', 'Jiménez', '44445555', 'rosa.jimenez@email.com'),
('Hugo', 'Salazar', '33332222', 'hugo.salazar@email.com'),
('Natalia', 'Campos', '22221111', 'natalia.campos@email.com'),
('Diego', 'Suárez', '11110000', 'diego.suarez@email.com'),
('Camila', 'Ortiz', '10101111', 'camila.ortiz@email.com'),
('Esteban', 'Reyes', '20202020', 'esteban.reyes@email.com'),
('Julieta', 'Navarro', '30303030', 'julieta.navarro@email.com'),
('Martín', 'Aguilar', '40404040', 'martin.aguilar@email.com'),
('Paola', 'Carrillo', '50505050', 'paola.carrillo@email.com'),
('Sebastián', 'Gómez', '60606060', 'sebastian.gomez@email.com'),
('Andrea', 'Herrera', '70707070', 'andrea.herrera@email.com'),
('Manuel', 'Domínguez', '80808080', 'manuel.dominguez@email.com'),
('Teresa', 'Fuentes', '90909090', 'teresa.fuentes@email.com'),
('Rodrigo', 'López', '12121212', 'rodrigo.lopez@email.com'),
('Carolina', 'Martín', '13131313', 'carolina.martin@email.com'),
('Carol', 'Martín', '14134414', 'carol.martin@email.com'),
('Cai', 'Marlin', '23232323', 'cai.marlin@email.com'),
('Sheldon', 'Cooper', '03957812', 'Shel.cooper@email.com'),
('Sai', 'Hamada', '45675780', 'sai.hamada@email.com');

INSERT INTO Dueño (IdPersona, Direccion) VALUES
(1, 'Colonia Centro, Managua'),
(2, 'Residencial Las Colinas, Managua'),
(3, 'Barrio San Juan, León'),
(4, 'Colonia Miraflores, Managua'),
(5, 'Residencial Villa Fontana, Managua'),
(6, 'Barrio El Carmen, Granada'),
(7, 'Colonia Altamira, Managua'),
(8, 'Residencial Las Mercedes, Managua'),
(9, 'Barrio La Fuente, León'),
(10, 'Colonia Bello Horizonte, Managua'),
(11, 'Residencial Los Robles, Managua'),
(12, 'Barrio San Antonio, Masaya'),
(13, 'Colonia Santa Clara, Managua'),
(14, 'Residencial Montecristo, Managua'),
(15, 'Barrio San Pedro, León'),
(16, 'Colonia San José, Managua'),
(17, 'Residencial Los Laureles, Managua'),
(18, 'Barrio San Pablo, Granada'),
(19, 'Colonia San Martín, Managua'),
(20, 'Residencial Villa Libertad, Managua'),
(21, 'Barrio La Esperanza, León'),
(22, 'Colonia San Miguel, Managua'),
(23, 'Residencial Los Pinos, Managua'),
(24, 'Barrio San Rafael, Masaya'),
(25, 'Colonia San Sebastián, Managua'),
(26, 'Residencial Villa Flor, Managua'),
(27, 'Barrio San Francisco, León'),
(28, 'Colonia San Antonio, Managua'),
(29, 'Residencial Los Ángeles, Managua'),
(30, 'Barrio San Marcos, Granada'),
(31, 'Colonia San Felipe, Managua'),
(32, 'Residencial Villa Sol, Managua'),
(33, 'Barrio San Nicolás, León'),
(34, 'Colonia San Pedro, Managua'),
(35, 'Residencial Los Cedros, Managua'),
(36, 'Barrio San Cristóbal, Masaya'),
(37, 'Colonia San Andrés, Managua'),
(38, 'Residencial Villa Serena, Managua'),
(39, 'Barrio San Mateo, León'),
(40, 'Colonia San Lucas, Managua'),
(41, 'Residencial Los Olivos, Managua'),
(42, 'Barrio San Gabriel, Granada'),
(43, 'Colonia San Isidro, Managua'),
(44, 'Residencial Villa Real, Managua'),
(45, 'Barrio San José, León'),
(46, 'Colonia San Juan, Managua'),
(47, 'Residencial Los Almendros, Managua'),
(48, 'Barrio San Miguel, Masaya'),
(49, 'Colonia San Carlos, Managua'),
(50, 'Residencial Villa Verde, Managua');

INSERT INTO Dueño (IdPersona, Direccion) VALUES
(51, 'Colonia San Pedro, Managua'),
(52, 'Residencial Los Robles, León'),
(53, 'Barrio San Antonio, Masaya'),
(54, 'Colonia Santa Clara, Managua'),
(55, 'Residencial Montecristo, Granada'),
(56, 'Barrio San Pablo, León'),
(57, 'Colonia San José, Managua'),
(58, 'Residencial Los Laureles, Managua'),
(59, 'Barrio San Rafael, Masaya'),
(60, 'Colonia San Sebastián, Managua'),
(61, 'Residencial Villa Flor, Managua'),
(62, 'Barrio San Francisco, León'),
(63, 'Colonia San Antonio, Managua'),
(64, 'Residencial Los Ángeles, Managua'),
(65, 'Barrio San Marcos, Granada'),
(66, 'Colonia San Felipe, Managua'),
(67, 'Residencial Villa Sol, Managua'),
(68, 'Barrio San Nicolás, León'),
(69, 'Colonia San Pedro, Managua'),
(70, 'Residencial Los Cedros, Managua'),
(71, 'Barrio San Cristóbal, Masaya'),
(72, 'Colonia San Andrés, Managua'),
(73, 'Residencial Villa Serena, Managua'),
(74, 'Barrio San Mateo, León'),
(75, 'Colonia San Lucas, Managua'),
(76, 'Residencial Los Olivos, Managua'),
(77, 'Barrio San Gabriel, Granada'),
(78, 'Colonia San Isidro, Managua'),
(79, 'Residencial Villa Real, Managua'),
(80, 'Barrio San José, León'),
(81, 'Colonia San Juan, Managua'),
(82, 'Residencial Los Almendros, Managua'),
(83, 'Barrio San Miguel, Masaya'),
(84, 'Colonia San Carlos, Managua'),
(85, 'Residencial Villa Verde, Managua'),
(86, 'Barrio San Pedro, León'),
(87, 'Colonia San Pablo, Managua'),
(88, 'Residencial Los Laureles, Granada'),
(89, 'Barrio San Rafael, León'),
(90, 'Colonia San Sebastián, Managua'),
(91, 'Residencial Villa Flor, Masaya'),
(92, 'Barrio San Francisco, Granada'),
(93, 'Colonia San Antonio, Managua'),
(94, 'Residencial Los Ángeles, León'),
(95, 'Barrio San Marcos, Masaya'),
(96, 'Colonia San Felipe, Managua'),
(97, 'Residencial Villa Sol, Granada'),
(98, 'Barrio San Nicolás, León'),
(99, 'Colonia San Pedro, Managua'),
(100, 'Residencial Los Cedros, Masaya'),
(101, 'Barrio San Cristóbal, León'),
(102, 'Colonia San Andrés, Managua'),
(103, 'Residencial Villa Serena, Masaya'),
(104, 'Barrio San Mateo, Granada'),
(105, 'Colonia San Lucas, Managua'),
(106, 'Residencial Los Olivos, León'),
(107, 'Barrio San Gabriel, Masaya'),
(108, 'Colonia San Isidro, Managua'),
(109, 'Residencial Villa Real, Granada'),
(110, 'Barrio San José, León');

INSERT INTO Dueño (IdPersona, Direccion) VALUES
(111, 'Colonia San Fernando, Managua'),
(112, 'Residencial Los Laureles, León'),
(113, 'Barrio San Miguel, Granada');



INSERT INTO Paciente (NombreMacota, Genero, FechaNacimiento, CodigoRaza, Peso) VALUES
('Firulais', 'Macho', '2020-05-10', 'LAB', 30.50),
('Luna', 'Hembra', '2021-08-22', 'BEA', 12.30),
('Michi', 'Macho', '2019-03-15', 'SIA', 5.20),
('Pelusa', 'Hembra', '2022-01-05', 'PERS', 4.80),
('Rocky', 'Macho', '2018-07-12', 'MESC', 18.40),
('Nala', 'Hembra', '2020-09-30', 'BICH', 10.10),
('Toby', 'Macho', '2021-11-11', 'CHI', 3.50),
('Kira', 'Hembra', '2019-02-20', 'LAB', 28.70),
('Simba', 'Macho', '2020-06-25', 'SIA', 6.00),
('Coco', 'Hembra', '2021-12-01', 'BEA', 11.90),
('Max', 'Macho', '2017-04-18', 'LAB', 32.00),
('Daisy', 'Hembra', '2022-03-14', 'PERS', 5.10),
('Zeus', 'Macho', '2019-08-09', 'MESC', 20.00),
('Molly', 'Hembra', '2020-10-05', 'CHI', 4.20),
('Leo', 'Macho', '2021-01-22', 'BICH', 9.80),
('Sasha', 'Hembra', '2018-12-12', 'LAB', 29.40),
('Tom', 'Macho', '2019-09-09', 'SIA', 5.50),
('Bella', 'Hembra', '2020-07-07', 'BEA', 12.00),
('Bruno', 'Macho', '2021-05-05', 'MESC', 19.30),
('Maya', 'Hembra', '2022-02-02', 'PERS', 4.90);


INSERT INTO Paciente (NombreMacota, Genero, FechaNacimiento, CodigoRaza, Peso) VALUES
('Rex', 'Macho', '2018-01-10', 'LAB', 31.20),
('Lola', 'Hembra', '2019-02-15', 'BEA', 13.00),
('Garfield', 'Macho', '2020-03-20', 'SIA', 6.10),
('Nieve', 'Hembra', '2021-04-25', 'PERS', 5.00),
('Boby', 'Macho', '2017-05-30', 'MESC', 22.50),
('Chispa', 'Hembra', '2018-06-05', 'CHI', 3.80),
('Thor', 'Macho', '2019-07-12', 'LAB', 29.90),
('Mimi', 'Hembra', '2020-08-18', 'BICH', 9.70),
('Felix', 'Macho', '2021-09-22', 'SIA', 5.40),
('Katy', 'Hembra', '2022-10-28', 'BEA', 12.50),
('Jack', 'Macho', '2018-11-11', 'LAB', 30.00),
('Sofi', 'Hembra', '2019-12-12', 'PERS', 4.70),
('Lucky', 'Macho', '2020-01-01', 'MESC', 19.80),
('Chiqui', 'Hembra', '2021-02-02', 'CHI', 4.10),
('Otto', 'Macho', '2022-03-03', 'BICH', 10.20),
('Tina', 'Hembra', '2017-04-04', 'LAB', 28.60),
('Simón', 'Macho', '2018-05-05', 'SIA', 6.00),
('Estrella', 'Hembra', '2019-06-06', 'BEA', 11.70),
('Brisa', 'Hembra', '2020-07-07', 'PERS', 5.30),
('Rambo', 'Macho', '2021-08-08', 'MESC', 20.40),
('Candy', 'Hembra', '2022-09-09', 'CHI', 3.90),
('Apolo', 'Macho', '2018-10-10', 'LAB', 32.10),
('Nina', 'Hembra', '2019-11-11', 'BICH', 9.60),
('Tommy', 'Macho', '2020-12-12', 'SIA', 5.80),
('Luz', 'Hembra', '2021-01-13', 'BEA', 12.20),
('Pancho', 'Macho', '2022-02-14', 'LAB', 29.50),
('Mora', 'Hembra', '2017-03-15', 'PERS', 4.90),
('Chester', 'Macho', '2018-04-16', 'MESC', 21.00),
('Kiara', 'Hembra', '2019-05-17', 'CHI', 4.30),
('Zeusito', 'Macho', '2020-06-18', 'BICH', 10.00),
('Princesa', 'Hembra', '2021-07-19', 'LAB', 30.40),
('Tiger', 'Macho', '2022-08-20', 'SIA', 6.20),
('Lili', 'Hembra', '2018-09-21', 'BEA', 11.80),
('Cleo', 'Hembra', '2019-10-22', 'PERS', 5.40),
('Rufus', 'Macho', '2020-11-23', 'MESC', 19.90),
('Chispi', 'Hembra', '2021-12-24', 'CHI', 4.00),
('Balto', 'Macho', '2022-01-25', 'LAB', 31.00),
('Nube', 'Hembra', '2017-02-26', 'BICH', 9.50),
('Zorro', 'Macho', '2018-03-27', 'SIA', 5.70),
('Perla', 'Hembra', '2019-04-28', 'BEA', 12.10),
('Rocko', 'Macho', '2020-05-29', 'LAB', 30.80),
('Menta', 'Hembra', '2021-06-30', 'PERS', 5.00),
('Bolt', 'Macho', '2022-07-01', 'MESC', 20.30),
('Chiquita', 'Hembra', '2018-08-02', 'CHI', 4.40),
('Sam', 'Macho', '2019-09-03', 'BICH', 9.90),
('Duna', 'Hembra', '2020-10-04', 'LAB', 29.70),
('Gato', 'Macho', '2021-11-05', 'SIA', 6.30),
('Sol', 'Hembra', '2022-12-06', 'BEA', 12.40),
('Ringo', 'Macho', '2017-01-07', 'LAB', 31.50),
('Miel', 'Hembra', '2018-02-08', 'PERS', 5.20),
('Pipo', 'Macho', '2019-03-09', 'MESC', 19.70),
('Chisguete', 'Hembra', '2020-04-10', 'CHI', 4.10),
('Nico', 'Macho', '2021-05-11', 'BICH', 9.80),
('Toby Jr', 'Macho', '2022-06-12', 'LAB', 30.20),
('Luzia', 'Hembra', '2018-07-13', 'SIA', 5.90),
('Estrella Jr', 'Hembra', '2019-08-14', 'BEA', 12.00),
('Pecas', 'Hembra', '2020-09-15', 'PERS', 5.10),
('Rexito', 'Macho', '2021-10-16', 'MESC', 20.10),
('Chiqui Jr', 'Hembra', '2022-11-17', 'CHI', 4.30),
('Thor Jr', 'Macho', '2017-12-18', 'LAB', 31.80),
('Mimi Jr', 'Hembra', '2018-01-19', 'BICH', 9.70),
('Felix Jr', 'Macho', '2019-02-20', 'SIA', 5.60),
('Katy Jr', 'Hembra', '2020-03-21', 'BEA', 12.30);


INSERT INTO Paciente (NombreMacota, Genero, FechaNacimiento, CodigoRaza, Peso) VALUES
('Firulais', 'Macho', '2020-05-10', 'LAB', 30.50),
('Luna', 'Hembra', '2021-08-22', 'BEA', 12.30),
('Michi', 'Macho', '2019-03-15', 'SIA', 5.20),
('Pelusa', 'Hembra', '2022-01-05', 'PERS', 4.80),
('Rocky', 'Macho', '2018-07-12', 'MESC', 18.40),
('Nala', 'Hembra', '2020-09-30', 'BICH', 10.10),
('Toby', 'Macho', '2021-11-11', 'CHI', 3.50),
('Kira', 'Hembra', '2019-02-20', 'LAB', 28.70),
('Simba', 'Macho', '2020-06-25', 'SIA', 6.00),
('Coco', 'Hembra', '2021-12-01', 'BEA', 11.90),
('Max', 'Macho', '2017-04-18', 'LAB', 32.00),
('Daisy', 'Hembra', '2022-03-14', 'PERS', 5.10),
('Zeus', 'Macho', '2019-08-09', 'MESC', 20.00),
('Molly', 'Hembra', '2020-10-05', 'CHI', 4.20),
('Leo', 'Macho', '2021-01-22', 'BICH', 9.80),
('Sasha', 'Hembra', '2018-12-12', 'LAB', 29.40),
('Tom', 'Macho', '2019-09-09', 'SIA', 5.50),
('Bella', 'Hembra', '2020-07-07', 'BEA', 12.00),
('Bruno', 'Macho', '2021-05-05', 'MESC', 19.30),
('Maya', 'Hembra', '2022-02-02', 'PERS', 4.90);

INSERT INTO Paciente (NombreMacota, Genero, FechaNacimiento, CodigoRaza, Peso) VALUES
('Rex', 'Macho', '2018-01-10', 'LAB', 31.20),
('Lola', 'Hembra', '2019-02-15', 'BEA', 13.00),
('Garfield', 'Macho', '2020-03-20', 'SIA', 6.10),
('Nieve', 'Hembra', '2021-04-25', 'PERS', 5.00),
('Boby', 'Macho', '2017-05-30', 'MESC', 22.50),
('Chispa', 'Hembra', '2018-06-05', 'CHI', 3.80),
('Thor', 'Macho', '2019-07-12', 'LAB', 29.90),
('Mimi', 'Hembra', '2020-08-18', 'BICH', 9.70),
('Felix', 'Macho', '2021-09-22', 'SIA', 5.40),
('Katy', 'Hembra', '2022-10-28', 'BEA', 12.50),
('Jack', 'Macho', '2018-11-11', 'LAB', 30.00),
('Sofi', 'Hembra', '2019-12-12', 'PERS', 4.70),
('Lucky', 'Macho', '2020-01-01', 'MESC', 19.80),
('Chiqui', 'Hembra', '2021-02-02', 'CHI', 4.10),
('Otto', 'Macho', '2022-03-03', 'BICH', 10.20),
('Tina', 'Hembra', '2017-04-04', 'LAB', 28.60),
('Simón', 'Macho', '2018-05-05', 'SIA', 6.00),
('Estrella', 'Hembra', '2019-06-06', 'BEA', 11.70),
('Brisa', 'Hembra', '2020-07-07', 'PERS', 5.30),
('Rambo', 'Macho', '2021-08-08', 'MESC', 20.40),
('Candy', 'Hembra', '2022-09-09', 'CHI', 3.90),
('Apolo', 'Macho', '2018-10-10', 'LAB', 32.10),
('Nina', 'Hembra', '2019-11-11', 'BICH', 9.60),
('Tommy', 'Macho', '2020-12-12', 'SIA', 5.80),
('Luz', 'Hembra', '2021-01-13', 'BEA', 12.20),
('Pancho', 'Macho', '2022-02-14', 'LAB', 29.50),
('Mora', 'Hembra', '2017-03-15', 'PERS', 4.90),
('Chester', 'Macho', '2018-04-16', 'MESC', 21.00),
('Kiara', 'Hembra', '2019-05-17', 'CHI', 4.30),
('Zeusito', 'Macho', '2020-06-18', 'BICH', 10.00),
('Princesa', 'Hembra', '2021-07-19', 'LAB', 30.40),
('Tiger', 'Macho', '2022-08-20', 'SIA', 6.20),
('Lili', 'Hembra', '2018-09-21', 'BEA', 11.80),
('Cleo', 'Hembra', '2019-10-22', 'PERS', 5.40),
('Rufus', 'Macho', '2020-11-23', 'MESC', 19.90),
('Chispi', 'Hembra', '2021-12-24', 'CHI', 4.00),
('Balto', 'Macho', '2022-01-25', 'LAB', 31.00),
('Nube', 'Hembra', '2017-02-26', 'BICH', 9.50),
('Zorro', 'Macho', '2018-03-27', 'SIA', 5.70),
('Perla', 'Hembra', '2019-04-28', 'BEA', 12.10),
('Rocko', 'Macho', '2020-05-29', 'LAB', 30.80),
('Menta', 'Hembra', '2021-06-30', 'PERS', 5.00),
('Bolt', 'Macho', '2022-07-01', 'MESC', 20.30),
('Chiquita', 'Hembra', '2018-08-02', 'CHI', 4.40),
('Sam', 'Macho', '2019-09-03', 'BICH', 9.90),
('Duna', 'Hembra', '2020-10-04', 'LAB', 29.70),
('Gato', 'Macho', '2021-11-05', 'SIA', 6.30),
('Sol', 'Hembra', '2022-12-06', 'BEA', 12.40),
('Ringo', 'Macho', '2017-01-07', 'LAB', 31.50),
('Miel', 'Hembra', '2018-02-08', 'PERS', 5.20),
('Pipo', 'Macho', '2019-03-09', 'MESC', 19.70),
('Chisguete', 'Hembra', '2020-04-10', 'CHI', 4.10),
('Nico', 'Macho', '2021-05-11', 'BICH', 9.80),
('Toby Jr', 'Macho', '2022-06-12', 'LAB', 30.20),
('Luzia', 'Hembra', '2018-07-13', 'SIA', 5.90),
('Estrella Jr', 'Hembra', '2019-08-14', 'BEA', 12.00),
('Pecas', 'Hembra', '2020-09-15', 'PERS', 5.10),
('Rexito', 'Macho', '2021-10-16', 'MESC', 20.10),
('Chiqui Jr', 'Hembra', '2022-11-17', 'CHI', 4.30),
('Thor Jr', 'Macho', '2017-12-18', 'LAB', 31.80),
('Mimi Jr', 'Hembra', '2018-01-19', 'BICH', 9.70),
('Felix Jr', 'Macho', '2019-02-20', 'SIA', 5.60),
('Katy Jr', 'Hembra', '2020-03-21', 'BEA', 12.30);

INSERT INTO Veterinario (IdPersona, Especialidad) VALUES
(85, 'Medicina General'),
(86, 'Cirugía Veterinaria'),
(87, 'Dermatología'),
(88, 'Oftalmología'),
(89, 'Cardiología'),
(90, 'Neurología'),
(91, 'Oncología'),
(92, 'Odontología'),
(93, 'Ortopedia'),
(94, 'Nutrición'),
(95, 'Rehabilitación'),
(96, 'Medicina Interna'),
(97, 'Anestesiología'),
(98, 'Medicina Preventiva'),
(99, 'Urgencias');


INSERT INTO Veterinario (IdPersona, Especialidad) VALUES
(100, 'Medicina General'),
(101, 'Cirugía Veterinaria'),
(102, 'Dermatología'),
(103, 'Oftalmología'),
(104, 'Cardiología'),
(105, 'Neurología'),
(106, 'Oncología'),
(107, 'Odontología'),
(108, 'Ortopedia'),
(109, 'Nutrición');


INSERT INTO Veterinario (IdPersona, Especialidad) VALUES
(111, 'Medicina General'),
(112, 'Cirugía Veterinaria'),
(113, 'Dermatología');

INSERT INTO Cita (IdMacota, IdVeterinario, IdDueño, FechaCita, Motivo) VALUES
(51, 5, 51, '2026-07-24 09:00:00', 'Chequeo general'),
(52, 6, 52, '2026-07-24 11:00:00', 'Vacunación anual'),
(53, 7, 53, '2026-07-24 14:00:00', 'Consulta por alergias'),
(54, 8, 54, '2026-07-25 09:30:00', 'Revisión de piel'),
(55, 9, 55, '2026-07-25 13:00:00', 'Control de peso'),
(56, 10, 56, '2026-07-25 16:00:00', 'Chequeo dental'),
(57, 11, 57, '2026-07-26 08:00:00', 'Consulta preventiva'),
(58, 12, 58, '2026-07-26 11:30:00', 'Revisión cardiológica'),
(59, 13, 59, '2026-07-26 15:00:00', 'Consulta por tos'),
(60, 14, 60, '2026-07-27 09:00:00', 'Chequeo nutricional'),
(61, 15, 61, '2026-07-27 11:00:00', 'Revisión de fractura'),
(62, 1, 62, '2026-07-27 14:00:00', 'Consulta de comportamiento'),
(63, 2, 63, '2026-07-28 09:00:00', 'Chequeo post-cirugía'),
(64, 3, 64, '2026-07-28 11:30:00', 'Consulta preventiva'),
(65, 4, 65, '2026-07-28 15:00:00', 'Revisión de ojos'),
(66, 5, 66, '2026-07-29 09:00:00', 'Vacunación antirrábica'),
(67, 6, 67, '2026-07-29 11:00:00', 'Chequeo por caída de pelo'),
(68, 7, 68, '2026-07-29 13:00:00', 'Consulta digestiva'),
(69, 8, 69, '2026-07-30 08:30:00', 'Chequeo general'),
(70, 9, 70, '2026-07-30 11:30:00', 'Consulta por alergias');

INSERT INTO Cita (IdMacota, IdVeterinario, IdDueño, FechaCita, Motivo) VALUES
(31, 1, 31, '2026-07-24 09:00:00', 'Chequeo general'),
(32, 2, 32, '2026-07-24 11:00:00', 'Vacunación anual'),
(33, 3, 33, '2026-07-24 14:00:00', 'Consulta por alergias'),
(34, 4, 34, '2026-07-25 09:30:00', 'Revisión de piel'),
(35, 5, 35, '2026-07-25 13:00:00', 'Control de peso'),
(36, 6, 36, '2026-07-25 16:00:00', 'Chequeo dental'),
(37, 7, 37, '2026-07-26 08:00:00', 'Consulta preventiva'),
(38, 8, 38, '2026-07-26 11:30:00', 'Revisión cardiológica'),
(39, 9, 39, '2026-07-26 15:00:00', 'Consulta por tos'),
(40, 10, 40, '2026-07-27 09:00:00', 'Chequeo nutricional');

SELECT IdVeterinario, IdPersona, Especialidad FROM Veterinario;
SELECT IdVeterinario FROM Veterinario;

SELECT * FROM Dueño

USE VetConnet;
GO

-- Para ver todos tus Dueños
SELECT * FROM Dueño;

-- Para ver todas tus Mascotas/Pacientes
SELECT * FROM Paciente;

-- Para ver tus Personas registradas
SELECT * FROM Persona;

INSERT INTO Cita (IdMacota, IdVeterinario, IdDueño, FechaCita, Motivo) -- <-- Corrige estos nombres según tu Paso 1
VALUES
(41, 2, 41, '2026-07-24 09:00:00', 'Chequeo general'),
(42, 3, 42, '2026-07-24 11:00:00', 'Vacunación anual'),
(43, 4, 43, '2026-07-24 14:00:00', 'Consulta por alergias'),
(44, 5, 44, '2026-07-25 09:00:00', 'Revisión de piel'),
(50, 6, 50, '2026-07-27 09:00:00', 'Chequeo nutricional');


INSERT INTO Diagnostico (IdCita, IdVeterinario, IdMacota, Descripcion) VALUES
(41, 2, 41, 'Diagnóstico: control rutinario, sin hallazgos'),
(42, 3, 42, 'Diagnóstico: vacunación aplicada correctamente'),
(43, 4, 43, 'Diagnóstico: alergia leve tratada con antihistamínicos'),
(44, 5, 44, 'Diagnóstico: dermatitis, se prescribe tratamiento tópico'),
(45, 6, 45, 'Diagnóstico: sobrepeso, se recomienda dieta especial'),
(46, 2, 46, 'Diagnóstico: limpieza dental realizada'),
(47, 3, 47, 'Diagnóstico: revisión preventiva, todo normal'),
(48, 4, 48, 'Diagnóstico: soplo cardíaco leve, seguimiento necesario'),
(49, 5, 49, 'Diagnóstico: tos persistente, posible bronquitis'),
(50, 6, 50, 'Diagnóstico: nutrición adecuada, sin problemas');


--Citas con datos del paciente y veterinario-
SELECT 
    C.IdCita,
    Pa.IdMacota,
    V.IdVeterinario,
    V.Especialidad,
    C.FechaCita,
    C.Motivo
FROM Cita C
INNER JOIN Paciente Pa ON C.IdMacota = Pa.IdMacota
INNER JOIN Veterinario V ON C.IdVeterinario = V.IdVeterinario;


---Mostrar diagnósticos con información completa
SELECT 
    D.IdDiagnostico,
    C.FechaCita,
    Pa.IdMacota,
    V.IdVeterinario,
    V.Especialidad,
    D.Descripcion
FROM Diagnostico D
INNER JOIN Cita C ON D.IdCita = C.IdCita
INNER JOIN Paciente Pa ON D.IdMacota = Pa.IdMacota
INNER JOIN Veterinario V ON D.IdVeterinario = V.IdVeterinario
ORDER BY C.FechaCita DESC;


---Contar cuántas citas tiene cada veterinario

SELECT 
    V.IdVeterinario,
    V.Especialidad,
    COUNT(C.IdCita) AS TotalCitas
FROM Veterinario V
LEFT JOIN Cita C ON V.IdVeterinario = C.IdVeterinario
GROUP BY V.IdVeterinario, V.Especialidad
ORDER BY TotalCitas DESC;


---Pacientes con más de una cita
SELECT
    Pa.IdMacota,
    COUNT(C.IdCita) AS NumeroCitas
FROM Paciente Pa
INNER JOIN Cita C ON Pa.IdMacota = C.IdMacota
GROUP BY Pa.IdMacota
HAVING COUNT(C.IdCita) > 1;

INSERT INTO Cita (IdMacota, IdVeterinario, IdDueño, FechaCita, Motivo)
VALUES (41, 2, 41, '2026-07-24 09:00:00', 'Chequeo general');

INSERT INTO Cita (IdMacota, IdVeterinario, IdDueño, FechaCita, Motivo)
VALUES (41, 3, 41, '2026-07-25 10:00:00', 'Vacunación anual');


--Historial de un paciente específico (ejemplo: IdMacota = 41)

SELECT 
    C.IdCita,
    C.FechaCita,
    C.Motivo,
    D.Descripcion AS Diagnostico,
    V.Especialidad AS Veterinario
FROM Cita C
INNER JOIN Diagnostico D ON C.IdCita = D.IdCita
INNER JOIN Veterinario V ON C.IdVeterinario = V.IdVeterinario
WHERE C.IdMacota = 41
ORDER BY C.FechaCita DESC;



--num citas por dia

SELECT 
    CAST(FechaCita AS DATE) AS Dia,
    COUNT(*) AS TotalCitas
FROM Cita
GROUP BY CAST(FechaCita AS DATE)
ORDER BY Dia;


-- pacientes con registro pero que no volieron a su cita

SELECT 
    Pa.IdMacota,
    MAX(C.FechaCita) AS UltimaCita
FROM Paciente Pa
INNER JOIN Cita C ON Pa.IdMacota = C.IdMacota
INNER JOIN Diagnostico D ON C.IdCita = D.IdCita
GROUP BY Pa.IdMacota
HAVING COUNT(C.IdCita) = 1;


