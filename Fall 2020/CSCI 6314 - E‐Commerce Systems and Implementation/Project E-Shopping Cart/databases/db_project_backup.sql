-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Окт 25 2020 г., 02:30
-- Версия сервера: 8.0.19
-- Версия PHP: 7.4.5

SET FOREIGN_KEY_CHECKS=0;
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
-- Создание: Сен 09 2020 г., 17:07
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
('Test2');

-- --------------------------------------------------------

--
-- Структура таблицы `comments`
--
-- Создание: Сен 09 2020 г., 17:07
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
(3, 'Tester', 'Tester', '5'),
(2, 'Ulvi', 'Very Very good!', '5'),
(3, 'Someone', 'very poor product', '1'),
(2, 'Ulvi2', 'Not so good', '1'),
(2, 'Ulvi', 'VeryVery Goood!\\r\\n\\r\\n\\r\\nOK', '5'),
(5, 'Johnny Doe', 'Somehow is OK', '5'),
(5, 'John', 'Something\\r\\n\\r\\n\\r\\n\\r\\nText', '5'),
(5, 'Johnny', 'Test this\r\n\r\nstring! &amp; write', '5'),
(5, 'Johnny 2', 'My test is\\r\\n\\r\\n&lt;good&gt;', '4'),
(5, 'Some', 'Some\\r\\n&amp;&lt;good&gt;\\r\\nIJ', '5');

-- --------------------------------------------------------

--
-- Структура таблицы `items`
--
-- Создание: Окт 03 2020 г., 16:35
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
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `items`
--

INSERT INTO `items` (`id`, `name`, `description`, `price`, `filepath`, `activation_status`, `item_count`) VALUES
(2, 'Test2', 'Es', '8.99', '', 'yes', 372),
(3, 'Teeee', 'tiitpo43poi', '92.30', '', 'yes', 28),
(5, 'Test', 'ssss', '22.33', '', 'yes', 22),
(8, 'A', 'V', '0.20', '', 'yes', 10),
(10, 'ssss', 'ssss', '0.22', '', 'yes', 22),
(12, 'aladpfijp', 'ewiwfiowfo', '2.33', '', 'yes', 22),
(18, 'f', 'd', '0.22', 'Class Hierarchy My Classes.jpg', 'yes', 4),
(21, 'Test', 'Test', '0.22', 'Tournaments.png', 'yes', 4),
(22, 'TTTTTTT', 'TTTTT', '0.22', '', 'no', 12),
(23, 'BBBB', 'BBBBB', '0.20', '', 'yes', 111),
(28, 'TEST', 'TEST', '0.22', '5f890c3a975c8_Class Hierarchy.jpg', 'yes', 12),
(29, 'UUUUU', 'UUUUU', '192.00', '', 'yes', 99),
(30, 'gjor', 'oguhweuor', '23.00', '5f8e205046a54_Class Hierarchy.jpg', 'yes', 23);

-- --------------------------------------------------------

--
-- Структура таблицы `items_and_categories`
--
-- Создание: Сен 09 2020 г., 17:07
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
(8, 'SSSSSSS');

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--
-- Создание: Окт 21 2020 г., 02:24
--

DROP TABLE IF EXISTS `orders`;
CREATE TABLE IF NOT EXISTS `orders` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `order_price` decimal(6,2) DEFAULT NULL,
  `order_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `orders`
--

INSERT INTO `orders` (`order_id`, `order_price`, `order_time`) VALUES
(2, '18.18', '2020-10-21 02:26:26'),
(3, '89.90', '2020-10-21 02:38:02');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--
-- Создание: Окт 14 2020 г., 18:14
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
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
