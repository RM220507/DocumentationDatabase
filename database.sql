-- phpMyAdmin SQL Dump
-- version 5.0.4deb2+deb11u1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 14, 2023 at 09:11 AM
-- Server version: 10.5.19-MariaDB-0+deb11u2
-- PHP Version: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `documentation`
--

-- --------------------------------------------------------

--
-- Table structure for table `Languages`
--

CREATE TABLE `Languages` (
  `LangID` int(11) NOT NULL,
  `LangName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Languages`
--

INSERT INTO `Languages` (`LangID`, `LangName`) VALUES
(5, 'CSS'),
(4, 'HTML'),
(6, 'JavaScript'),
(1, 'N/A'),
(3, 'PHP'),
(2, 'Python'),
(7, 'SQL');

-- --------------------------------------------------------

--
-- Table structure for table `Links`
--

CREATE TABLE `Links` (
  `LinkID` int(11) NOT NULL,
  `LinkName` varchar(255) NOT NULL,
  `URL` varchar(255) NOT NULL,
  `TypeID` int(11) NOT NULL,
  `LangID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Links`
--

INSERT INTO `Links` (`LinkID`, `LinkName`, `URL`, `TypeID`, `LangID`) VALUES
(1, 'Python MySQL', 'https://www.w3schools.com/python/python_mysql_getstarted.asp', 2, 2),
(2, 'Clear Frame Tkinter', 'https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame', 1, 2),
(3, 'Pygame', 'https://www.pygame.org/docs/', 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `Types`
--

CREATE TABLE `Types` (
  `TypeID` int(11) NOT NULL,
  `TypeName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `Types`
--

INSERT INTO `Types` (`TypeID`, `TypeName`) VALUES
(3, 'Datasheet'),
(1, 'Documentation'),
(4, 'Purchase Link'),
(2, 'Tutorial');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Languages`
--
ALTER TABLE `Languages`
  ADD PRIMARY KEY (`LangID`),
  ADD UNIQUE KEY `LangName` (`LangName`);

--
-- Indexes for table `Links`
--
ALTER TABLE `Links`
  ADD PRIMARY KEY (`LinkID`),
  ADD KEY `LangID` (`LangID`),
  ADD KEY `TypeID` (`TypeID`);

--
-- Indexes for table `Types`
--
ALTER TABLE `Types`
  ADD PRIMARY KEY (`TypeID`),
  ADD UNIQUE KEY `TypeName` (`TypeName`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Languages`
--
ALTER TABLE `Languages`
  MODIFY `LangID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `Links`
--
ALTER TABLE `Links`
  MODIFY `LinkID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `Types`
--
ALTER TABLE `Types`
  MODIFY `TypeID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Links`
--
ALTER TABLE `Links`
  ADD CONSTRAINT `LangID` FOREIGN KEY (`LangID`) REFERENCES `Languages` (`LangID`) ON UPDATE CASCADE,
  ADD CONSTRAINT `TypeID` FOREIGN KEY (`TypeID`) REFERENCES `Types` (`TypeID`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
