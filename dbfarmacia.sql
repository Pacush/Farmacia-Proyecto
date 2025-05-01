-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: May 01, 2025 at 10:15 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbfarmacia`
--

-- --------------------------------------------------------

--
-- Table structure for table `articulos`
--

CREATE TABLE `articulos` (
  `articulo_id` int(10) NOT NULL,
  `descripcion` varchar(50) NOT NULL,
  `precio_unitario` int(10) NOT NULL,
  `precio_venta` int(10) NOT NULL,
  `existencia` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `articulos`
--

INSERT INTO `articulos` (`articulo_id`, `descripcion`, `precio_unitario`, `precio_venta`, `existencia`) VALUES
(1, 'asd', 12, 15, 0),
(2, 'Fanta', 12, 15, 0),
(3, 'Agua', 10, 15, 0);

-- --------------------------------------------------------

--
-- Table structure for table `clientes`
--

CREATE TABLE `clientes` (
  `cliente_id` int(10) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `direccion` varchar(20) NOT NULL,
  `rfc` varchar(20) NOT NULL,
  `usuario_id` int(10) DEFAULT NULL,
  `puntos` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `clientes`
--

INSERT INTO `clientes` (`cliente_id`, `nombre`, `direccion`, `rfc`, `usuario_id`, `puntos`) VALUES
(1, 'Diego', '1234', '1234', 1, 10);

-- --------------------------------------------------------

--
-- Table structure for table `compras`
--

CREATE TABLE `compras` (
  `folio` int(10) NOT NULL,
  `fecha` varchar(20) NOT NULL,
  `proveedor_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `compras`
--

INSERT INTO `compras` (`folio`, `fecha`, `proveedor_id`) VALUES
(1, 'sad', 2),
(2, '12.12.12', 1),
(3, '29.4.2225', 1),
(4, '1.1.1', 1),
(5, '77.77.77', 1);

-- --------------------------------------------------------

--
-- Table structure for table `det_articulo`
--

CREATE TABLE `det_articulo` (
  `det_id` int(10) NOT NULL,
  `proveedor_id` int(10) NOT NULL,
  `articulo_id` int(10) NOT NULL,
  `existencia` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `det_articulo`
--

INSERT INTO `det_articulo` (`det_id`, `proveedor_id`, `articulo_id`, `existencia`) VALUES
(1, 1, 1, 160),
(3, 2, 1, 20),
(4, 1, 2, 50),
(6, 2, 2, 100),
(7, 1, 3, 50),
(8, 2, 3, 20);

-- --------------------------------------------------------

--
-- Table structure for table `det_compra`
--

CREATE TABLE `det_compra` (
  `det_id` int(10) NOT NULL,
  `folio` int(10) NOT NULL,
  `cantidad` int(10) NOT NULL,
  `articulo_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `det_compra`
--

INSERT INTO `det_compra` (`det_id`, `folio`, `cantidad`, `articulo_id`) VALUES
(1, 1, 20, 1),
(2, 1, 20, 2),
(4, 2, 10, 1),
(5, 2, 25, 2),
(8, 3, 11, 1),
(9, 3, 7, 2),
(10, 4, 10, 3),
(11, 5, 20, 3);

-- --------------------------------------------------------

--
-- Table structure for table `det_venta`
--

CREATE TABLE `det_venta` (
  `det_id` int(10) NOT NULL,
  `folio` int(10) NOT NULL,
  `articulo_id` int(10) NOT NULL,
  `cantidad` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `det_venta`
--

INSERT INTO `det_venta` (`det_id`, `folio`, `articulo_id`, `cantidad`) VALUES
(1, 1, 2, 2),
(3, 2, 2, 4),
(4, 2, 1, 3),
(5, 3, 2, 5),
(6, 3, 1, 3),
(7, 4, 2, 4),
(8, 5, 2, 5),
(9, 6, 1, 6),
(10, 7, 2, 7),
(11, 8, 2, 8);

-- --------------------------------------------------------

--
-- Table structure for table `proveedores`
--

CREATE TABLE `proveedores` (
  `proveedor_id` int(10) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `empresa` varchar(20) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `existencias` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `proveedores`
--

INSERT INTO `proveedores` (`proveedor_id`, `nombre`, `empresa`, `telefono`, `existencias`) VALUES
(1, 'Coca', 'Coca', '123454', 50),
(2, 'Pepsi', 'Pepsi', '12354', 50);

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `usuario_id` int(10) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `perfil` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`usuario_id`, `nombre`, `telefono`, `username`, `password`, `perfil`) VALUES
(1, 'joss', '3333333333', 'joss', '1234', 'Administrador');

-- --------------------------------------------------------

--
-- Table structure for table `ventas`
--

CREATE TABLE `ventas` (
  `folio` int(10) NOT NULL,
  `fecha` varchar(20) NOT NULL,
  `cliente_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ventas`
--

INSERT INTO `ventas` (`folio`, `fecha`, `cliente_id`) VALUES
(1, '1', 1),
(2, '2.2.2', 1),
(3, '3.3.3', 1),
(4, '4.4.4', 1),
(5, '5', 1),
(6, '666', 1),
(7, '777', 1),
(8, '888', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `articulos`
--
ALTER TABLE `articulos`
  ADD PRIMARY KEY (`articulo_id`);

--
-- Indexes for table `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`cliente_id`),
  ADD KEY `cliente_usuarioid_fk` (`usuario_id`);

--
-- Indexes for table `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`folio`),
  ADD KEY `compra_proveedor_fk` (`proveedor_id`);

--
-- Indexes for table `det_articulo`
--
ALTER TABLE `det_articulo`
  ADD PRIMARY KEY (`det_id`),
  ADD KEY `detalle_proveedor_fk` (`proveedor_id`),
  ADD KEY `detalle_articulo_fk` (`articulo_id`);

--
-- Indexes for table `det_compra`
--
ALTER TABLE `det_compra`
  ADD PRIMARY KEY (`det_id`),
  ADD KEY `detalle_foliocompras_id` (`folio`),
  ADD KEY `detalle_articulos_fk` (`articulo_id`);

--
-- Indexes for table `det_venta`
--
ALTER TABLE `det_venta`
  ADD PRIMARY KEY (`det_id`),
  ADD KEY `detalleventa_articulos_fk` (`articulo_id`),
  ADD KEY `detalle_folio_fk` (`folio`);

--
-- Indexes for table `proveedores`
--
ALTER TABLE `proveedores`
  ADD PRIMARY KEY (`proveedor_id`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`usuario_id`);

--
-- Indexes for table `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`folio`),
  ADD KEY `ventas_cliente_fk` (`cliente_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `cliente_usuarioid_fk` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`);

--
-- Constraints for table `compras`
--
ALTER TABLE `compras`
  ADD CONSTRAINT `compra_proveedor_fk` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedores` (`proveedor_id`) ON DELETE CASCADE;

--
-- Constraints for table `det_articulo`
--
ALTER TABLE `det_articulo`
  ADD CONSTRAINT `detalle_articulo_fk` FOREIGN KEY (`articulo_id`) REFERENCES `articulos` (`articulo_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `detalle_proveedor_fk` FOREIGN KEY (`proveedor_id`) REFERENCES `proveedores` (`proveedor_id`) ON DELETE CASCADE;

--
-- Constraints for table `det_compra`
--
ALTER TABLE `det_compra`
  ADD CONSTRAINT `detalle_articulos_fk` FOREIGN KEY (`articulo_id`) REFERENCES `articulos` (`articulo_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `detalle_foliocompras_id` FOREIGN KEY (`folio`) REFERENCES `compras` (`folio`) ON DELETE CASCADE;

--
-- Constraints for table `det_venta`
--
ALTER TABLE `det_venta`
  ADD CONSTRAINT `detalle_folio_fk` FOREIGN KEY (`folio`) REFERENCES `ventas` (`folio`) ON DELETE CASCADE,
  ADD CONSTRAINT `detalleventa_articulos_fk` FOREIGN KEY (`articulo_id`) REFERENCES `articulos` (`articulo_id`) ON DELETE CASCADE;

--
-- Constraints for table `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `ventas_cliente_fk` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`cliente_id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
