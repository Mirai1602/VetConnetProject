USE ProyectoV
Go

CREATE TABLE Mascota
(
	Id_Masco INT PRIMARY KEY IDENTITY,
	Nombre_Masco nchar(50) NOT NULL,
	Especie nchar(50) NOT NULL,-- Si es canino, felino, etc.
	Id_Dueño INT FOREIGN KEY REFERENCES Dueño(Id_Dueño),
	raza nchar(50), --Si es un Husky,labrador, etc.
	Genero nchar(10) NOT NULL, -- Si es macho o hembra
	Edad INT,
)

CREATE TABLE Persona
(
	Id_Persona INT PRIMARY KEY IDENTITY,
	Nombre_Persona nchar(50) NOT NULL,
	Apellido_Persona nchar(50) NOT NULL,
	Telefono nchar(15) NOT NULL,
	Rol nchar(20) NOT NULL -- Si es dueño, veterinario, etc.
)


CREATE TABLE Dueño
(
	Id_Dueño INT PRIMARY KEY IDENTITY,
	Nombre_Dueño nchar(50) NOT NULL,
	Apellido_Dueño nchar(50) NOT NULL,
	Telefono nchar(15) NOT NULL,
	rol_Dueño nchar(20) NOT NULL, -- Si es dueño, veterinario, etc.
	Id_Masco INT FOREIGN KEY REFERENCES Mascota(Id_Masco)
	
	
)

CREATE TABLE Veterinario
(
	Id_Veterinario INT PRIMARY KEY IDENTITY,
	Nombre_Veterinario nchar(50) NOT NULL,
	Apellido_Veterinario nchar(50) NOT NULL,
	Telefono nchar(15) NOT NULL,
	Especialidad nchar(50) NOT NULL, -- Si es especialista en caninos, felinos, etc.
	rol_Vet nchar(20) NOT NULL -- Si es veterinario, auxiliar, etc.
)

CREATE TABLE Clinica
(
	Id_Clinica INT PRIMARY KEY IDENTITY,
	Nombre_Clinica nchar(100) NOT NULL,
	Direccion nchar(200) NOT NULL,
	Telefono nchar(15) NOT NULL
	
)


CREATE TABLE Cita
(
	Id_Cita INT PRIMARY KEY IDENTITY,
	Id_Dueño INT FOREIGN KEY REFERENCES Dueño(Id_Dueño),
	Id_Veterinario INT FOREIGN KEY REFERENCES Veterinario(Id_Veterinario),
	Id_Clinica INT FOREIGN KEY REFERENCES Clinica(Id_Clinica),
	Fecha DATETIME NOT NULL,
	Motivo nchar(200) NOT NULL
)
