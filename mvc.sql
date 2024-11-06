SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `CEDULA` varchar(12) NOT NULL,
  `NOMBRE` varchar(80) NOT NULL,
  `ROL` varchar(15) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=32 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

INSERT INTO `usuario` (`ID`, `CEDULA`, `NOMBRE`, `ROL`) VALUES
(1, '1234567890', 'Juan Pérez', 'Admin'),
(2, '2345678901', 'María Gómez', 'User'),
(3, '3456789012', 'Carlos López', 'User'),
(4, '4567890123', 'Ana Martínez', 'Admin'),
(5, '5678901234', 'Luis Rodríguez', 'User'),
(6, '6789012345', 'Laura Fernández', 'User'),
(7, '7890123456', 'Pedro Sánchez', 'Admin'),
(8, '8901234567', 'Marta Díaz', 'User'),
(9, '9012345678', 'Jorge Ramírez', 'User'),
(10, '0123456789', 'Sofía Torres', 'Admin'),
(11, '1123456789', 'Andrés Morales', 'User'),
(12, '2123456789', 'Elena Castillo', 'User'),
(13, '3123456789', 'Ricardo Herrera', 'Admin'),
(14, '4123456789', 'Patricia Jiménez', 'User'),
(15, '5123456789', 'Fernando Ruiz', 'User'),
(16, '6123456789', 'Gabriela Vega', 'Admin'),
(17, '7123456789', 'Alberto Cruz', 'User'),
(18, '8123456789', 'Isabel Ortiz', 'User'),
(19, '9123456789', 'Miguel Silva', 'Admin'),
(20, '1023456789', 'Natalia Ríos', 'User'),
(21, '2023456789', 'Javier Peña', 'User'),
(22, '3023456789', 'Claudia Soto', 'Admin'),
(23, '4023456789', 'Héctor Mendoza', 'User'),
(24, '5023456789', 'Verónica Vargas', 'User'),
(25, '6023456789', 'Diego Castro', 'Admin'),
(26, '7023456789', 'Rosa Navarro', 'User'),
(27, '8023456789', 'Daniela Paredes', 'User'),
(28, '9023456789', 'Francisco León', 'Admin'),
(29, '1034567890', 'Silvia Reyes', 'User'),
(30, '2034567890', 'Esteban Flores', 'User'),
(31, '123454321', 'César Penilla', 'User');
COMMIT;
