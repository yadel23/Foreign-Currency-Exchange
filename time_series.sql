-- MariaDB dump 10.17  Distrib 10.4.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: history
-- ------------------------------------------------------
-- Server version	10.4.8-MariaDB-1:10.4.8+maria~bionic-log

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
-- Table structure for table `currency_history`
--

DROP TABLE IF EXISTS `currency_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `currency_history` (
  `usd` text DEFAULT NULL,
  `Day` text DEFAULT NULL,
  `Rate` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `currency_history`
--

LOCK TABLES `currency_history` WRITE;
/*!40000 ALTER TABLE `currency_history` DISABLE KEYS */;
INSERT INTO `currency_history` VALUES ('usd','2020-03-21',1.0657),('usd','2020-03-22',1.0657),('usd','2020-03-23',1.0694),('usd','2020-03-24',1.0765),('usd','2020-03-25',1.0803),('usd','2020-03-26',1.089),('usd','2020-03-27',1.1048),('usd','2020-03-28',1.1048),('usd','2020-03-29',1.1048),('usd','2020-03-30',1.1139),('usd','2020-03-31',1.103),('usd','2020-04-01',1.1027),('usd','2020-04-02',1.0954),('usd','2020-04-03',1.0847),('usd','2020-04-04',1.0847),('usd','2020-04-05',1.0847),('usd','2020-04-06',1.0807),('usd','2020-04-07',1.0804),('usd','2020-04-08',1.0895),('usd','2020-04-09',1.0864),('usd','2020-04-10',1.0927),('usd','2020-04-11',1.0927),('usd','2020-04-12',1.0927),('usd','2020-04-13',1.0933),('usd','2020-04-14',1.0923),('usd','2020-04-15',1.0985),('usd','2020-04-16',1.0905),('usd','2020-04-17',1.0858),('usd','2020-04-18',1.0858),('usd','2020-04-19',1.0858),('usd','2020-04-20',1.0867),('usd','2020-04-21',1.0865),('usd','2020-04-22',1.0856),('usd','2020-04-23',1.081),('usd','2020-04-24',1.0777),('usd','2020-04-25',1.0777),('usd','2020-04-26',1.0777),('usd','2020-04-27',1.0824),('usd','2020-04-28',1.0825),('usd','2020-04-29',1.0837),('usd','2020-04-30',1.0877),('usd','2020-05-01',1.0945),('usd','2020-05-02',1.10945),('usd','2020-05-03',1.10945),('usd','2020-05-04',1.09529),('usd','2020-05-05',1.090899),('usd','2020-05-06',1.08401),('usd','2020-05-07',1.07965),('usd','2020-05-08',1.08416),('usd','2020-05-09',1.09705),('usd','2020-05-10',1.09705),('usd','2020-05-11',1.0846),('usd','2020-05-12',1.081257),('usd','2020-05-13',1.084693),('usd','2020-05-14',1.080881),('usd','2020-05-15',1.08063),('usd','2020-05-16',1.08216),('usd','2020-05-17',1.08216),('usd','2020-05-18',1.081876),('usd','2020-05-19',1.09083),('usd','2020-05-20',1.09445),('usd','2020-05-21',1.09592);
/*!40000 ALTER TABLE `currency_history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-08 18:35:01
