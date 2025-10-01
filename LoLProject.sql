-- MySQL dump 10.13  Distrib 8.0.43, for Linux (x86_64)
--
-- Host: localhost    Database: LoLProject
-- ------------------------------------------------------
-- Server version	8.0.43-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `active_skills`
--

DROP TABLE IF EXISTS `active_skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `active_skills` (
  `active_id` int NOT NULL,
  `requires_activation` tinyint(1) DEFAULT NULL,
  `champion_id` int DEFAULT NULL,
  PRIMARY KEY (`active_id`),
  KEY `champion_id` (`champion_id`),
  CONSTRAINT `active_skills_ibfk_1` FOREIGN KEY (`active_id`) REFERENCES `skills` (`id`),
  CONSTRAINT `active_skills_ibfk_2` FOREIGN KEY (`champion_id`) REFERENCES `skills` (`champ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `active_skills`
--

LOCK TABLES `active_skills` WRITE;
/*!40000 ALTER TABLE `active_skills` DISABLE KEYS */;
INSERT INTO `active_skills` VALUES (1,1,1),(2,1,2),(4,1,4);
/*!40000 ALTER TABLE `active_skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `champions`
--

DROP TABLE IF EXISTS `champions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `champions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `origin` text,
  `attack_style` text NOT NULL,
  `champ_class` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `champ_class` (`champ_class`),
  CONSTRAINT `champions_ibfk_1` FOREIGN KEY (`champ_class`) REFERENCES `class` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `champions`
--

LOCK TABLES `champions` WRITE;
/*!40000 ALTER TABLE `champions` DISABLE KEYS */;
INSERT INTO `champions` VALUES (1,'Jhin','Ionia','Ranged',1),(2,'Veigar','Bandle City','Skills',2),(3,'Teemo','Bandle City','Ranged',2),(4,'Sion','Noxus','Melee',3);
/*!40000 ALTER TABLE `champions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class` (
  `id` int NOT NULL AUTO_INCREMENT,
  `class_name` text,
  `lane` text,
  `build_style` text,
  `attack_style` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` VALUES (1,'Marksman','Bot lane','Attack Damage Items',NULL),(2,'Mage','Mid lane','Ability Power Items',NULL),(3,'Tank','Top lane','Durability Items',NULL),(4,'Brusier','Top lane','Attack damage and Durability Items',NULL);
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `id` int NOT NULL AUTO_INCREMENT,
  `attack_damage` int DEFAULT NULL,
  `ability_power` int DEFAULT NULL,
  `armor` int DEFAULT NULL,
  `item_name` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (1,45,NULL,NULL,'Kraken Slayer'),(2,NULL,120,NULL,'Rabadon\'s Deathcap'),(3,NULL,105,50,'Zhonya\'s Hourglass'),(4,NULL,NULL,75,'Randuin\'s Omen');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passive_skills`
--

DROP TABLE IF EXISTS `passive_skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passive_skills` (
  `passive_id` int NOT NULL,
  `requires_activation` tinyint(1) DEFAULT NULL,
  `champion_id` int DEFAULT NULL,
  PRIMARY KEY (`passive_id`),
  KEY `champion_id` (`champion_id`),
  CONSTRAINT `passive_skills_ibfk_1` FOREIGN KEY (`passive_id`) REFERENCES `skills` (`id`),
  CONSTRAINT `passive_skills_ibfk_2` FOREIGN KEY (`champion_id`) REFERENCES `skills` (`champ_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passive_skills`
--

LOCK TABLES `passive_skills` WRITE;
/*!40000 ALTER TABLE `passive_skills` DISABLE KEYS */;
INSERT INTO `passive_skills` VALUES (3,0,3);
/*!40000 ALTER TABLE `passive_skills` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pref_item`
--

DROP TABLE IF EXISTS `pref_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pref_item` (
  `item_id` int NOT NULL,
  `champion_id` int NOT NULL,
  PRIMARY KEY (`item_id`,`champion_id`),
  KEY `champion_id` (`champion_id`),
  CONSTRAINT `pref_item_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`),
  CONSTRAINT `pref_item_ibfk_2` FOREIGN KEY (`champion_id`) REFERENCES `champions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pref_item`
--

LOCK TABLES `pref_item` WRITE;
/*!40000 ALTER TABLE `pref_item` DISABLE KEYS */;
INSERT INTO `pref_item` VALUES (1,1),(3,1),(2,2),(3,2),(2,3),(3,3),(4,4);
/*!40000 ALTER TABLE `pref_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skills`
--

DROP TABLE IF EXISTS `skills`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skills` (
  `id` int NOT NULL AUTO_INCREMENT,
  `skill_name` text NOT NULL,
  `attack_percent` int DEFAULT NULL,
  `ap_percent` int DEFAULT NULL,
  `champ_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `champ_id` (`champ_id`),
  CONSTRAINT `skills_ibfk_1` FOREIGN KEY (`champ_id`) REFERENCES `champions` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skills`
--

LOCK TABLES `skills` WRITE;
/*!40000 ALTER TABLE `skills` DISABLE KEYS */;
INSERT INTO `skills` VALUES (1,'Dancing Grenade',74,60,1),(2,'Baleful Strike',NULL,70,2),(3,'Toxic Shot',NULL,30,3),(4,'Decimating Smash',80,NULL,4);
/*!40000 ALTER TABLE `skills` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-09-25 22:50:34
