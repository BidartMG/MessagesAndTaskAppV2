-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 31-03-2021 a las 17:25:58
-- Versión del servidor: 10.1.37-MariaDB
-- Versión de PHP: 7.3.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `flaskmessages`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `assigned_messages`
--

CREATE TABLE `assigned_messages` (
  `id` int(11) NOT NULL,
  `message` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `sender` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `receiver` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `estado` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `assigned_messages`
--

INSERT INTO `assigned_messages` (`id`, `message`, `sender`, `receiver`, `date`, `time`, `estado`) VALUES
(102, 'fgh', '1156512729', '133', '2021-03-31', '15:15:00', 'OCUPADO'),
(104, 'PRUEBA 12', '1156512729', '45026015', '2021-03-28', '22:10:00', 'OCUPADO'),
(106, 'PRUEBA 14', '1156512729', '541145036015', '2021-03-28', '22:33:00', 'OCUPADO'),
(107, 'PRUEBA 14', '1156512729', '45033136', '2021-03-28', '22:35:00', 'OCUPADO'),
(110, 'PRUEBA 17', '1156512729', '133', '2021-03-30', '00:00:00', 'OCUPADO'),
(111, 'PRUEBA 18', '1156512729', '114', '2021-03-31', '00:00:00', 'OCUPADO'),
(112, 'PRUEBA 19', '1156512729', '114', '2021-03-31', '00:00:00', 'OCUPADO'),
(114, 'olALA', '1156512729', '114', '2021-03-31', '14:14:00', 'OCUPADO'),
(115, 'PRUEBA 100', '1156512729', '114', '2021-03-31', '00:00:00', 'OCUPADO'),
(119, 'This is a real message', '123456', '541145036015', '2021-03-27', '16:15:00', 'OCUPADO'),
(121, 'otto krause', '1156512730', '45033136', '2021-03-27', '16:25:00', 'OCUPADO'),
(122, 'PRUEBA 1', '1156512729', '114', '2021-03-27', '19:35:00', 'OCUPADO'),
(123, 'PRUEBA 2', '1156512729', '10000000000000000', '2021-03-27', '21:18:00', 'OCUPADO'),
(124, 'PRUEBA 3', '1156512729', '55555555555555555555555555555', '2021-03-27', '21:23:00', 'OCUPADO'),
(125, 'PRUEBA 4', '1156512729', '9999999999999999999999', '2021-03-27', '21:30:00', 'OCUPADO'),
(126, 'PRUEBA 5', '1156512729', '77777777777', '2021-03-27', '21:31:00', 'OCUPADO'),
(127, 'PRUEBA 6', '1156512729', '333333333333', '2021-03-27', '21:32:00', 'OCUPADO'),
(128, 'PRUEBA 7', '1156512729', '1111111111', '2021-03-27', '21:41:00', 'OCUPADO'),
(129, 'PRUEBA 8', '1156512729', '88888888888', '2021-03-27', '21:43:00', 'OCUPADO'),
(130, 'PRUEBA 9', '1156512729', '99999999', '2021-03-27', '21:45:00', 'OCUPADO'),
(131, 'PRUEBA 10', '1156512729', '114', '2021-03-13', '04:08:00', 'OCUPADO'),
(133, 'PRUEBA 11', '1156512729', '541145036015', '2021-03-27', '22:04:00', 'OCUPADO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `finished_tasks`
--

CREATE TABLE `finished_tasks` (
  `id` int(11) NOT NULL,
  `message` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `sender` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `receiver` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `estado` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `invalid_numbers`
--

CREATE TABLE `invalid_numbers` (
  `id_soy` int(11) NOT NULL,
  `soy` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `message` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `sender` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `receiver` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `date` datetime NOT NULL,
  `time` time NOT NULL,
  `estado` varchar(20) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'EN_ESPERA'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `messages`
--

INSERT INTO `messages` (`id`, `message`, `sender`, `receiver`, `date`, `time`, `estado`) VALUES
(103, 'PRUEBA 12', '1156512730', '45026015', '2021-03-31 09:54:00', '09:54:00', 'EN_ESPERA'),
(105, 'PRUEBA 13', '1156512730', '123,456,789', '2021-03-28 00:00:00', '22:12:00', 'EN_ESPERA'),
(113, 'PRUEBA 20', '1156512730', '133', '2021-03-30 00:00:00', '00:00:00', 'EN_ESPERA'),
(116, 'PRUEBA 101', '1156512729', '45026015', '2021-03-31 11:47:00', '00:00:00', 'EN_ESPERA'),
(117, 'PRUEBA 102', '1156512729', '101,102,103,104,105,106,107,108,109,110', '2021-03-31 12:19:00', '12:18:00', 'EN_ESPERA');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `assigned_messages`
--
ALTER TABLE `assigned_messages`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `invalid_numbers`
--
ALTER TABLE `invalid_numbers`
  ADD PRIMARY KEY (`id_soy`);

--
-- Indices de la tabla `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `invalid_numbers`
--
ALTER TABLE `invalid_numbers`
  MODIFY `id_soy` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=118;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
