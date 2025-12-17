-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 17, 2025 at 03:39 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_vending`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, '123456', '2482'),
(2, '12345', '12345'),
(3, 'admin', '0192023a7bbd73250516f069df18b500');

-- --------------------------------------------------------

--
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `harga` decimal(65,0) NOT NULL,
  `nama_file` varchar(255) NOT NULL,
  `stok` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`id`, `nama`, `harga`, `nama_file`, `stok`) VALUES
(2, 'nescafe', 7000, 'nescafe.png', 999),
(3, 'pepsi', 6000, 'pepsi.png', 999),
(4, 'pillows', 2000, 'pillows.png', 999),
(5, 'chikibalss', 3000, 'chikiballs.png', 999),
(6, 'chitato', 4000, 'chitato.png', 999),
(7, 'fanta', 5000, 'fanta.png', 999),
(8, 'wallens', 5000, 'walens.png', 999),
(9, 'cheetos', 1000, 'cheetos.png', 999),
(10, 'Permen Yupi', 7500, 'yupi.png', 999),
(11, 'Fruittea', 4500, 'fruittea.png', 999),
(12, 'le mineral', 3000, 'air.png', 999),
(13, 'nescafe', 7000, 'nescafe.png', 999),
(14, 'pepsi', 6000, 'pepsi.png', 999),
(15, 'pillows', 2000, 'pillows.png', 999),
(16, 'chikibalss', 3000, 'chikiballs.png', 999),
(17, 'chitato', 4000, 'chitato.png', 999),
(18, 'fanta', 5000, 'fanta.png', 999),
(19, 'wallens', 5000, 'walens.png', 999),
(20, 'cheetos', 1000, 'cheetos.png', 999),
(21, 'Permen Yupi', 7500, 'yupi.png', 999),
(22, 'Fruittea', 4500, 'fruittea.png', 999),
(24, 'Momogi', 3500, 'momogi.png', 0),
(25, 'Floridina', 4000, 'floridina.png', 0),
(27, 'air', 3000, 'air.png', 0),
(28, 'air', 4000, 'air.png', 0),
(29, 'wek wek', 2, 'beng beng.png', 0),
(30, 'ngok', 222, 'fanta.png', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `barang`
--
ALTER TABLE `barang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
