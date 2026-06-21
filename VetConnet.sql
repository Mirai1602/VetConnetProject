USE PetConnect
GO

CREATE TABLE Especie(
CodigoEspecie NCHAR(50) PRIMARY KEY,
NombreEspecie nchar(50) NOT NULL
);


CREATE TABLE Raza(
CodigoRaza nchar(50) PRIMARY KEY,
NombreRaza nchar(50) NOT NULL,
Caracteristicas NVARCHAR(100),
CodigoEspecie NCHAR(50) FOREIGN KEY REFERENCES Especie(CodigoEspecie)
); 


CREATE TABLE Paciente(
IdMacota INT PRIMARY KEY IDENTITY(1,1),
NombreMacota nchar(50) NOT NULL,
Genero nchar(10) NOT NULL,
FechaNacimiento DATE,
CodigoRaza NCHAR(50) FOREIGN KEY REFERENCES Raza(CodigoRaza),
Peso DECIMAL(5,2),

);


CREATE TABLE Persona(
IdPersona INT PRIMARY KEY IDENTITY(1,1),
Nombre NVARCHAR(50),
Apellido NVARCHAR(50),
Telefono NVARCHAR(15),
Email NVARCHAR(100)
);

CREATE TABLE Dueño(
IdDueño INT PRIMARY KEY IDENTITY(1,1),
IdPersona INT FOREIGN KEY REFERENCES Persona(IdPersona),
Direccion NVARCHAR(100)
);

CREATE TABLE Veterinario(
IdVeterinario INT PRIMARY KEY IDENTITY(1,1),
IdPersona INT FOREIGN KEY REFERENCES Persona(IdPersona),
Especialidad NVARCHAR(50),
);

CREATE TABLE Cita(
IdCita INT PRIMARY KEY IDENTITY(1,1),
IdMacota INT FOREIGN KEY REFERENCES Paciente(IdMacota),
IdVeterinario INT FOREIGN KEY REFERENCES Veterinario(IdVeterinario),
IdDueño INT FOREIGN KEY REFERENCES Dueño(IdDueño),
FechaCita DATETIME,
Motivo NVARCHAR(300)

);

CREATE TABLE Diagnostico(
IdDiagnostico INT PRIMARY KEY IDENTITY(1,1),
IdCita INT FOREIGN KEY REFERENCES Cita(IdCita),
IdVeterinario INT FOREIGN KEY REFERENCES Veterinario(IdVeterinario),
IdMacota INT FOREIGN KEY REFERENCES Paciente(IdMacota),
Descripcion NVARCHAR(300),
); 

INSERT INTO Especie (CodigoEspecie, NombreEspecie) VALUES
('CAN', 'Canino'),
('FEL', 'Felino');

INSERT INTO Raza (CodigoRaza, NombreRaza, Caracteristicas, CodigoEspecie) VALUES
('LAB', 'Labrador Retriever', 'Perro de raza grande con pelaje largo y de color naranja', 'CAN'),
('BEA', 'Beagle', 'Perro de raza mediana-baja de pelaje blanco con manchas cafes y negras', 'CAN'),
('SIA', 'Siamés', 'Gato de ojos grandes, generalmente con clores de pelaje blanco con cafe', 'FEL'),
('PERS', 'Persa', 'Gato de pelaje largo con colores como: Blanco, naranja y blanco + gris', 'FEL'),
('MESC', 'Mestizo', 'Perros de raza mestiza o x','CAN'),
('BICH','Bichon Habanero','Perro de raza mediana, con colores de pelaje: Blanco con manchas cafes y negro en las orejas','CAN'),
('CHI','Chihuahua','Perro de raza pequeña con colores variados','CAN');



