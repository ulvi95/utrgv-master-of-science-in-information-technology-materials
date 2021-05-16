-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Ноя 04 2020 г., 01:47
-- Версия сервера: 8.0.19
-- Версия PHP: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `db_project`
--
CREATE DATABASE IF NOT EXISTS `db_project` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `db_project`;

-- --------------------------------------------------------

--
-- Структура таблицы `categories`
--

DROP TABLE IF EXISTS `categories`;
CREATE TABLE IF NOT EXISTS `categories` (
  `category` varchar(255) NOT NULL,
  PRIMARY KEY (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `categories`
--

INSERT INTO `categories` (`category`) VALUES
('SSSSSSS'),
('Test2'),
('Toy');

-- --------------------------------------------------------

--
-- Структура таблицы `comments`
--

DROP TABLE IF EXISTS `comments`;
CREATE TABLE IF NOT EXISTS `comments` (
  `id` int NOT NULL,
  `commentator_name` varchar(255) NOT NULL,
  `comment_text` varchar(1024) NOT NULL,
  `rating` enum('1','2','3','4','5') NOT NULL,
  KEY `fk_comments_items_idx` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `comments`
--

INSERT INTO `comments` (`id`, `commentator_name`, `comment_text`, `rating`) VALUES
(5, 'Johnny Doe', 'Somehow is OK', '5'),
(5, 'John', 'Something\\r\\n\\r\\n\\r\\n\\r\\nText', '5'),
(5, 'Johnny', 'Test this\r\n\r\nstring! &amp; write', '5'),
(5, 'Johnny 2', 'My test is\\r\\n\\r\\n&lt;good&gt;', '4'),
(5, 'Some', 'Some\\r\\n&amp;&lt;good&gt;\\r\\nIJ', '5'),
(31, 'Ulvi Bajarani', 'Poorly designed', '1'),
(31, 'John Doe', 'Ulvi is not right\\r\\n\\r\\n\\r\\n\\r\\nIt is good!', '5');

-- --------------------------------------------------------

--
-- Структура таблицы `items`
--

DROP TABLE IF EXISTS `items`;
CREATE TABLE IF NOT EXISTS `items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(1024) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `filepath` varchar(255) NOT NULL,
  `activation_status` enum('yes','no') NOT NULL DEFAULT 'yes',
  `item_count` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `items`
--

INSERT INTO `items` (`id`, `name`, `description`, `price`, `filepath`, `activation_status`, `item_count`) VALUES
(5, 'Test', 'ssss', '22.33', '', 'yes', 22),
(8, 'A', 'V', '0.20', '', 'yes', 9),
(10, 'ssss', 'ssss', '0.22', '', 'yes', 22),
(12, 'aladpfijp', 'ewiwfiowfo', '2.33', '', 'yes', 17),
(18, 'F', 'D', '22.00', '5f9f2b53a23aa_Class Hierarchy.jpg', 'yes', 44),
(21, 'Test', 'Test', '0.22', 'Tournaments.png', 'yes', 3),
(22, 'TTTTTTT', 'TTTTT', '0.22', '', 'no', 12),
(23, 'BBBB', 'BBBBB', '0.20', '', 'yes', 111),
(28, 'TEST', 'TEST', '0.22', '5f890c3a975c8_Class Hierarchy.jpg', 'yes', 12),
(29, 'UUUUU', 'UUUUU', '192.00', '', 'yes', 99),
(30, 'gjor', 'oguhweuor', '23.00', '5f8e205046a54_Class Hierarchy.jpg', 'yes', 17),
(31, 'Barbie (sale)', 'Plastic toy with sale!', '10.00', '5fa0bf74ebc65_Barbie2.jpg', 'yes', 48);

-- --------------------------------------------------------

--
-- Структура таблицы `items_and_categories`
--

DROP TABLE IF EXISTS `items_and_categories`;
CREATE TABLE IF NOT EXISTS `items_and_categories` (
  `id` int NOT NULL,
  `category` varchar(255) NOT NULL,
  KEY `fk_items_and_categories_items1_idx` (`id`),
  KEY `fk_items_and_categories_categories1_idx` (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `items_and_categories`
--

INSERT INTO `items_and_categories` (`id`, `category`) VALUES
(22, 'Test2'),
(29, 'SSSSSSS'),
(30, 'SSSSSSS'),
(29, 'Test2'),
(8, 'SSSSSSS'),
(31, 'Toy');

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

DROP TABLE IF EXISTS `orders`;
CREATE TABLE IF NOT EXISTS `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `order_price` decimal(6,2) DEFAULT NULL,
  `order_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `orders`
--

INSERT INTO `orders` (`order_id`, `order_price`, `order_time`) VALUES
(3, '89.90', '2020-10-21 02:38:02'),
(4, '92.72', '2020-10-26 23:44:22'),
(6, '11.65', '2020-10-26 23:46:58'),
(7, '23.00', '2020-10-26 23:48:43'),
(8, '23.00', '2020-10-26 23:49:40'),
(9, '23.00', '2020-10-26 23:53:09'),
(10, '99.00', '2020-11-03 02:38:41'),
(11, '30.00', '2020-11-03 02:43:45'),
(12, NULL, '2020-11-03 02:43:52'),
(13, '10.00', '2020-11-03 02:45:36'),
(14, '10.00', '2020-11-03 22:03:30'),
(15, '10.00', '2020-11-03 22:11:46'),
(16, '10.00', '2020-11-03 22:21:00'),
(17, '10.00', '2020-11-03 22:39:04'),
(18, '10.00', '2020-11-03 22:44:48');

-- --------------------------------------------------------

--
-- Структура таблицы `payments`
--

DROP TABLE IF EXISTS `payments`;
CREATE TABLE IF NOT EXISTS `payments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `txnid` varchar(20) NOT NULL,
  `payment_amount` decimal(7,2) NOT NULL,
  `payment_status` varchar(25) NOT NULL,
  `itemid` varchar(25) NOT NULL,
  `createdtime` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`,`username`,`password`,`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `users`
--

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `fk_comments_items` FOREIGN KEY (`id`) REFERENCES `items` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ограничения внешнего ключа таблицы `items_and_categories`
--
ALTER TABLE `items_and_categories`
  ADD CONSTRAINT `fk_items_and_categories_categories1` FOREIGN KEY (`category`) REFERENCES `categories` (`category`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_items_and_categories_items1` FOREIGN KEY (`id`) REFERENCES `items` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
