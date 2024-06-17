-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Cze 17, 2024 at 01:18 PM
-- Wersja serwera: 10.4.32-MariaDB
-- Wersja PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wypozyczalnia`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `car`
--

CREATE TABLE `car` (
  `VIN` varchar(17) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `model` varchar(255) NOT NULL,
  `version` varchar(255) NOT NULL,
  `production_year` int(11) NOT NULL,
  `engine` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `car`
--

INSERT INTO `car` (`VIN`, `brand`, `model`, `version`, `production_year`, `engine`, `color`) VALUES
('1HGCM82633A004352', 'Honda', 'Accord', 'LX', 2020, '2.0L I4', 'Black'),
('1FAFP404X1F138764', 'Ford', 'Mustang', 'GT', 2019, '5.0L V8', 'Red'),
('WBA3A5C57CF355450', 'BMW', '3 Series', '320i', 2021, '2.0L I4', 'White'),
('3N1AB7AP3KY273824', 'Nissan', 'Sentra', 'SR', 2022, '2.0L I4', 'Blue'),
('JHMFA36258S001945', 'Honda', 'Civic', 'EX', 2021, '1.8L I4', 'Silver'),
('WA1D7AFP5HA054385', 'Audi', 'Q5', 'Premium', 2020, '2.0L I4', 'Gray'),
('1HGCM82633A004353', 'Honda', 'Accord', 'Sport', 2022, '1.5L I4', 'White'),
('5J8TB4H52GL018754', 'Acura', 'RDX', 'SH-AWD', 2021, '3.5L V6', 'Black'),
('1HGCV1F3XJA234567', 'Honda', 'Accord', 'Touring', 2020, '2.0L I4', 'Red'),
('5XYZU3LB5EG142536', 'Hyundai', 'Santa Fe', 'Sport', 2019, '2.4L I4', 'Silver'),
('1FTEW1E48JKE54123', 'Ford', 'F-150', 'XLT', 2021, '3.5L V6', 'Blue'),
('2T1BURHE5GC714328', 'Toyota', 'Corolla', 'LE', 2020, '1.8L I4', 'Black'),
('1C4PJMCB7FW642379', 'Jeep', 'Cherokee', 'Latitude', 2019, '2.4L I4', 'White'),
('1N4AL3AP1JC224675', 'Nissan', 'Altima', 'SV', 2022, '2.5L I4', 'Gray'),
('JTHBE1BL1FA004567', 'Lexus', 'IS', '350', 2021, '3.5L V6', 'Red'),
('5J6RM4H74FL002145', 'Honda', 'CR-V', 'EX-L', 2020, '1.5L I4', 'Blue'),
('WA1B4AFY0J2012345', 'Audi', 'Q7', 'Premium Plus', 2021, '3.0L V6', 'Silver'),
('KM8J3CA28JU754321', 'Hyundai', 'Tucson', 'Limited', 2019, '2.0L I4', 'Black'),
('1HGCR2F3XHA123456', 'Honda', 'Accord', 'EX-L', 2021, '1.5L I4', 'White'),
('3FA6P0HR2JR123456', 'Ford', 'Fusion', 'SE', 2020, '2.0L I4', 'Gray'),
('1C4RJFBG3JC152768', 'Jeep', 'Grand Cherokee', 'Limited', 2021, '3.6L V6', 'Red'),
('1HGCV2F37JA123456', 'Honda', 'Accord', 'Sport 2.0T', 2022, '2.0L I4', 'Silver'),
('1G1ZD5ST6LF123456', 'Chevrolet', 'Malibu', 'LT', 2020, '1.5L I4', 'Blue'),
('3C4PDCBBXET123456', 'Dodge', 'Journey', 'SXT', 2019, '2.4L I4', 'Black'),
('1FMCU9G93JUC12345', 'Ford', 'Escape', 'SE', 2021, '1.5L I4', 'White'),
('4T1BF1FK0GU123456', 'Toyota', 'Camry', 'XSE', 2020, '2.5L I4', 'Gray'),
('5UXWX9C55H0T12345', 'BMW', 'X3', 'xDrive30i', 2021, '2.0L I4', 'Red'),
('1C6RR7LT9FS123456', 'Ram', '1500', 'Laramie', 2020, '5.7L V8', 'Silver'),
('2HGFC2F59GH123456', 'Honda', 'Civic', 'LX', 2019, '2.0L I4', 'Blue'),
('1FTFW1EF9JKE12345', 'Ford', 'F-150', 'Platinum', 2021, '5.0L V8', 'Black'),
('1J4AA2D10BL123456', 'Jeep', 'Wrangler', 'Sport', 2020, '3.6L V6', 'White'),
('1GNSKHKC0KR123456', 'Chevrolet', 'Tahoe', 'LT', 2019, '5.3L V8', 'Gray'),
('3N1AB7AP7JY123456', 'Nissan', 'Sentra', 'SV', 2021, '1.8L I4', 'Red'),
('5FNYF5H52JB123456', 'Honda', 'Pilot', 'EX', 2022, '3.5L V6', 'Silver'),
('1FM5K8D85KGB12345', 'Ford', 'Explorer', 'XLT', 2020, '2.3L I4', 'Blue'),
('1G1ZB5ST5KF123456', 'Chevrolet', 'Malibu', 'LS', 2019, '1.5L I4', 'Black'),
('5XYKT3A12EG123456', 'Kia', 'Sorento', 'LX', 2021, '2.4L I4', 'White'),
('3CZRU6H57HM123456', 'Honda', 'HR-V', 'EX', 2020, '1.8L I4', 'Gray'),
('1HGCV1F36JA123456', 'Honda', 'Accord', 'EX', 2019, '1.5L I4', 'Red'),
('1FTEW1EGXJFA12345', 'Ford', 'F-150', 'King Ranch', 2021, '3.5L V6', 'Silver'),
('3FA6P0HD2HR123456', 'Ford', 'Fusion', 'Titanium', 2020, '2.0L I4', 'Blue'),
('1C4PJLDB7JW123456', 'Jeep', 'Cherokee', 'Trailhawk', 2019, '3.2L V6', 'Black'),
('4S4BSAHC5J3223456', 'Subaru', 'Outback', 'Premium', 2021, '2.5L H4', 'White'),
('5YJ3E1EA5KF123456', 'Tesla', 'Model 3', 'Standard Range Plus', 2020, 'Electric', 'Gray'),
('WA1BNAFY8K2001234', 'Audi', 'Q5', 'Prestige', 2022, '3.0L V6', 'Red'),
('1HGCR2F89HA123456', 'Honda', 'Accord', 'Touring', 2021, '2.0L I4', 'Silver'),
('1FMCU9J96JUC12345', 'Ford', 'Escape', 'Titanium', 2020, '2.0L I4', 'Blue'),
('1G1ZE5ST4LF123456', 'Chevrolet', 'Malibu', 'Premier', 2019, '2.0L I4', 'Black'),
('3N1CE2CP3JL123456', 'Nissan', 'Versa', 'Note', 2021, '1.6L I4', 'White'),
('3CZRU5H32JM123456', 'Honda', 'HR-V', 'LX', 2020, '1.8L I4', 'Gray'),
('1FTFW1E53JFA12345', 'Ford', 'F-150', 'Raptor', 2021, '3.5L V6', 'Red'),
('2HGFC2F5XKH123456', 'Honda', 'Civic', 'Sport', 2022, '2.0L I4', 'Silver'),
('5XXGT4L32KG123456', 'Kia', 'Optima', 'EX', 2019, '2.4L I4', 'Blue'),
('1GNSKCKC5KR123456', 'Chevrolet', 'Tahoe', 'Premier', 2021, '6.2L V8', 'Black'),
('5XYZT3LB7EG123456', 'Hyundai', 'Santa Fe', 'Limited', 2020, '2.0L I4', 'White'),
('1FTEW1EG5JFA12345', 'Ford', 'F-150', 'Lariat', 2022, '3.5L V6', 'Gray'),
('1C4PJLDB0JD123456', 'Jeep', 'Cherokee', 'Overland', 2021, '3.2L V6', 'Red'),
('3CZRU6H53JG123456', 'Honda', 'HR-V', 'Touring', 2020, '1.8L I4', 'Silver'),
('1HGCR2F3XGA123456', 'Honda', 'Accord', 'EX-L', 2019, '1.5L I4', 'Blue'),
('1FA6P8CF8J5101234', 'Ford', 'Mustang', 'GT Premium', 2021, '5.0L V8', 'Black'),
('5FNYF6H59HB123456', 'Honda', 'Pilot', 'Touring', 2020, '3.5L V6', 'White'),
('WA1D7AFP5KB123456', 'Audi', 'Q5', 'Prestige', 2019, '2.0L I4', 'Gray'),
('1G1ZE5ST3JF123456', 'Chevrolet', 'Malibu', 'Premier', 2021, '2.0L I4', 'Red'),
('2HKRM4H79JH123456', 'Honda', 'CR-V', 'Touring', 2020, '1.5L I4', 'Silver'),
('5UXWX9C52H0T12345', 'BMW', 'X3', 'M40i', 2021, '3.0L I6', 'Blue'),
('4S4BSANC5K3267890', 'Subaru', 'Outback', 'Limited', 2022, '2.5L H4', 'Black'),
('1C6RR7KTXFS123456', 'Ram', '1500', 'Rebel', 2019, '5.7L V8', 'White'),
('1G1ZE5ST5KF123456', 'Chevrolet', 'Malibu', 'Premier', 2021, '2.0L I4', 'Gray'),
('3FA6P0K95JR123456', 'Ford', 'Fusion', 'Platinum', 2020, '2.0L I4', 'Red'),
('1HGCV1F35JA123456', 'Honda', 'Accord', 'Sport', 2022, '1.5L I4', 'Silver'),
('5J6RM4H74FL123456', 'Honda', 'CR-V', 'EX-L', 2021, '1.5L I4', 'Blue'),
('1HGCR2F57GA123456', 'Honda', 'Accord', 'EX-L', 2020, '2.4L I4', 'Black'),
('WA1BNAFY8L1012345', 'Audi', 'Q5', 'Premium Plus', 2021, '3.0L V6', 'White'),
('3CZRU6H55JG123456', 'Honda', 'HR-V', 'EX-L', 2020, '1.8L I4', 'Gray'),
('1FTEW1EG8JFC12345', 'Ford', 'F-150', 'Limited', 2021, '3.5L V6', 'Red'),
('2HGFC2F57KH123456', 'Honda', 'Civic', 'Sport', 2022, '2.0L I4', 'Silver'),
('1N4AL3AP5JC123456', 'Nissan', 'Altima', 'SV', 2021, '2.5L I4', 'Blue'),
('3FA6P0G73HR123456', 'Ford', 'Fusion', 'SE', 2020, '2.0L I4', 'Black'),
('1C4RJFAG6FC123456', 'Jeep', 'Grand Cherokee', 'Laredo', 2019, '3.6L V6', 'White'),
('1HGCR2F52GA123456', 'Honda', 'Accord', 'Sport', 2020, '2.4L I4', 'Gray'),
('WA1B4AFY5L1001234', 'Audi', 'Q5', 'Premium', 2021, '2.0L I4', 'Red'),
('5XYZU3LB6EG123456', 'Hyundai', 'Santa Fe', 'Sport', 2019, '2.4L I4', 'Silver'),
('1FA6P8CF4J5101234', 'Ford', 'Mustang', 'GT', 2021, '5.0L V8', 'Blue'),
('JTHBE1BL3FA123456', 'Lexus', 'IS', '350', 2020, '3.5L V6', 'Black'),
('1HGCV2F38JA123456', 'Honda', 'Accord', 'Sport 2.0T', 2022, '2.0L I4', 'White'),
('5J8TB4H52GL123456', 'Acura', 'RDX', 'SH-AWD', 2021, '3.5L V6', 'Gray'),
('3N1AB7AP8KY123456', 'Nissan', 'Sentra', 'SV', 2022, '2.0L I4', 'Red'),
('1C4RJFLG0JC123456', 'Jeep', 'Grand Cherokee', 'Summit', 2019, '5.7L V8', 'Silver'),
('5XXGT4L35KG123456', 'Kia', 'Optima', 'SX', 2021, '2.0L I4', 'Blue'),
('WA1BNAFY9K2012345', 'Audi', 'Q5', 'Prestige', 2022, '3.0L V6', 'Black'),
('2HKRM4H58FH123456', 'Honda', 'CR-V', 'EX', 2020, '1.5L I4', 'White'),
('1G1ZD5ST4LF123456', 'Chevrolet', 'Malibu', 'LT', 2021, '1.5L I4', 'Gray'),
('1FMCU9GD5JUA12345', 'Ford', 'Escape', 'SE', 2020, '1.5L I4', 'Red'),
('3CZRU6H58JM123456', 'Honda', 'HR-V', 'EX-L', 2021, '1.8L I4', 'Silver'),
('1HGCR2F37GA123456', 'Honda', 'Accord', 'EX', 2019, '1.5L I4', 'Blue'),
('5YJ3E1EA5JF123456', 'Tesla', 'Model 3', 'Standard Range Plus', 2020, 'Electric', 'Black'),
('4T1BF1FK4GU123456', 'Toyota', 'Camry', 'SE', 2021, '2.5L I4', 'White'),
('1FTFW1E41JFC12345', 'Ford', 'F-150', 'Platinum', 2022, '3.5L V6', 'Gray'),
('1HGCR2F57HA123456', 'Honda', 'Accord', 'Sport', 2020, '2.4L I4', 'Red'),
('3FA6P0G72HR123456', 'Ford', 'Fusion', 'SE', 2021, '2.0L I4', 'Silver'),
('1C4PJMDX6JD123456', 'Jeep', 'Cherokee', 'Limited', 2019, '3.2L V6', 'Blue'),
('WA1D7AFP0KB123456', 'Audi', 'Q5', 'Prestige', 2020, '2.0L I4', 'Black'),
('3N1AB7AP2KY123456', 'Nissan', 'Sentra', 'SV', 2021, '2.0L I4', 'White'),
('1GNSKHKC2JR123456', 'Chevrolet', 'Tahoe', 'LT', 2019, '5.3L V8', 'Gray'),
('5FNYF5H63JB123456', 'Honda', 'Pilot', 'EX', 2022, '3.5L V6', 'Red'),
('1HGCV1F35KA123456', 'Honda', 'Accord', 'EX', 2021, '1.5L I4', 'Silver'),
('5XYZT3LB2EG123456', 'Hyundai', 'Santa Fe', 'Limited', 2020, '2.0L I4', 'Blue'),
('1N4AL3AP4JC123456', 'Nissan', 'Altima', 'SL', 2019, '2.5L I4', 'Black'),
('3FA6P0H77JR123456', 'Ford', 'Fusion', 'SEL', 2021, '2.0L I4', 'White'),
('5XXGT4L38KG123456', 'Kia', 'Optima', 'SX', 2020, '2.0L I4', 'Gray'),
('1G1ZB5ST8LF123456', 'Chevrolet', 'Malibu', 'LS', 2021, '1.5L I4', 'Red'),
('3CZRU5H32JM123456', 'Honda', 'HR-V', 'LX', 2019, '1.8L I4', 'Silver'),
('1HGCR2F59HA123456', 'Honda', 'Accord', 'Sport', 2020, '2.4L I4', 'Blue'),
('5J8TB4H55GL123456', 'Acura', 'RDX', 'SH-AWD', 2021, '3.5L V6', 'Black'),
('WA1D7AFP3KB123456', 'Audi', 'Q5', 'Prestige', 2020, '2.0L I4', 'White'),
('5NPE34AF6KH123456', 'Hyundai', 'Sonata', 'SEL', 2021, '2.4L I4', 'Gray'),
('1C6RR7KTXFS123456', 'Ram', '1500', 'Rebel', 2019, '5.7L V8', 'Red'),
('5YJ3E1EA7JF123456', 'Tesla', 'Model 3', 'Standard Range Plus', 2020, 'Electric', 'Silver'),
('1HGCR2F57GA123456', 'Honda', 'Accord', 'EX-L', 2021, '2.4L I4', 'Blue'),
('2HKRM4H54FH123456', 'Honda', 'CR-V', 'EX', 2020, '1.5L I4', 'Black'),
('WA1B4AFY3L1001234', 'Audi', 'Q5', 'Premium Plus', 2021, '3.0L V6', 'White'),
('3FA6P0K95JR123456', 'Ford', 'Fusion', 'Platinum', 2020, '2.0L I4', 'Gray'),
('1N4AL3AP5JC123456', 'Nissan', 'Altima', 'SV', 2021, '2.5L I4', 'Red'),
('5J8TB4H54GL123456', 'Acura', 'RDX', 'SH-AWD', 2021, '3.5L V6', 'Silver'),
('1G1ZE5ST5JF123456', 'Chevrolet', 'Malibu', 'Premier', 2020, '2.0L I4', 'Blue');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `person`
--

CREATE TABLE `person` (
  `name` varchar(30) NOT NULL,
  `gender` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `person`
--

INSERT INTO `person` (`name`, `gender`) VALUES
('Adam', 'M'),
('Magda', 'F'),
('Monika', 'F'),
('Jakub', 'M'),
('Krzysztof', 'M'),
('Justyna', 'F'),
('Izabela', 'F'),
('Stanislaw', 'M'),
('Weronika', 'F'),
('Grzegorz', 'M');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `person_surname`
--

CREATE TABLE `person_surname` (
  `surname` varchar(30) NOT NULL,
  `gender` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `person_surname`
--

INSERT INTO `person_surname` (`surname`, `gender`) VALUES
('Nowak', 'M'),
('Nowak', 'F'),
('Kowalska', 'F'),
('Kowalski', 'M'),
('Cicha', 'F'),
('Cichy', 'M'),
('Bala', 'M'),
('Bala', 'F');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
