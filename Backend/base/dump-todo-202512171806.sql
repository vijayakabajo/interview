/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.13-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: todo
-- ------------------------------------------------------
-- Server version	10.11.13-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `todos`
--

DROP TABLE IF EXISTS `todos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `todos` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `title` varchar(64) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `is_done` tinyint(1) DEFAULT 0,
  `is_active` tinyint(1) DEFAULT 1,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_todos_user_id` (`user_id`),
  KEY `idx_todos_active` (`is_active`),
  KEY `idx_todos_done` (`is_done`),
  KEY `idx_todos_created_at` (`created_at`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `todos`
--

LOCK TABLES `todos` WRITE;
/*!40000 ALTER TABLE `todos` DISABLE KEYS */;
INSERT INTO `todos` VALUES
(1,1,'Vijay','mcknakndalncsksnsklakasc nacsljna',0,1,'2025-12-17 03:38:31','2025-12-17 03:38:31',NULL),
(2,1,'Vija  xxy','mcknakndalncsksnsklakasc nacsljna',0,0,'2025-12-17 03:38:36','2025-12-17 09:25:51','2025-12-17 03:55:51'),
(3,2,'Vija  xxy','mcknakndalncsksnsklakasc nacsljna',0,1,'2025-12-17 04:03:18','2025-12-17 04:03:18',NULL),
(4,2,'Vija  xxy','mcknakndalncsksnsklakasc nacsljna',0,1,'2025-12-17 04:03:20','2025-12-17 04:03:20',NULL),
(5,2,'Vija  xxy','mcknakndalncsksnsklakasc nacsljna',0,1,'2025-12-17 04:03:49','2025-12-17 04:03:49',NULL),
(6,2,'Vija  xxy','mcknakndalncsksnsklakasc nacsljna',0,1,'2025-12-17 04:03:52','2025-12-17 04:03:52',NULL),
(7,2,'tstststts','tststststtstst',0,1,'2025-12-17 04:38:26','2025-12-17 10:11:35',NULL);
/*!40000 ALTER TABLE `todos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `full_name` varchar(128) DEFAULT NULL,
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_active` tinyint(1) DEFAULT 0,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `deleted_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES
(1,'Vijay','vijayakabajo@gmail.com','pbkdf2_sha256$1200000$MWZ6Hif14HliU7V7SlwTot$ww54pwHIQcRIoBhZ3xq5wMMjmeSEi2DGl4rW+H+D5ec=',1,'2025-12-17 03:28:57','2025-12-17 03:28:57',NULL),
(2,'Vijay','vijayakabajo2@gmail.com','pbkdf2_sha256$1200000$7pHKRPhafQAh04vveqAktE$i4/C8pUBammio1eDFbclpqihepa/oq60Loxi0jdMjYs=',1,'2025-12-17 04:01:54','2025-12-17 04:01:54',NULL),
(3,'Vijay','vijayakabajo3@gmail.com','pbkdf2_sha256$1200000$HqNwXMc7mLd9Q9VwWO2sS9$omoufbDaQYbyceh/lMw1ov8+Hgh+nGpOP/cDoWq/Tf4=',1,'2025-12-17 04:34:16','2025-12-17 04:34:16',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'todo'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-17 18:06:45
