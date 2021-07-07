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
  `Day` text DEFAULT NULL,
  `Rate` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `currency_history`
--

LOCK TABLES `currency_history` WRITE;
/*!40000 ALTER TABLE `currency_history` DISABLE KEYS */;
INSERT INTO `currency_history` VALUES ('2020-04-22',1.0856),('2020-04-23',1.081),('2020-04-24',1.0777),('2020-04-25',1.0777),('2020-04-26',1.0777),('2020-04-27',1.0824),('2020-04-28',1.0825),('2020-04-29',1.0837),('2020-04-30',1.0877),('2020-05-01',1.0945),('2020-05-02',1.10945),('2020-05-03',1.10945),('2020-05-04',1.09529),('2020-05-05',1.090899),('2020-05-06',1.08401),('2020-05-07',1.07965),('2020-05-08',1.08416),('2020-05-09',1.09705),('2020-05-10',1.09705),('2020-05-11',1.0846),('2020-05-12',1.081257),('2020-05-13',1.084693),('2020-05-14',1.080881),('2020-05-15',1.08063),('2020-05-16',1.08216),('2020-05-17',1.08216),('2020-05-18',1.081876),('2020-05-19',1.09083),('2020-05-20',1.09445),('2020-05-21',1.09592),('2020-05-22',1.0924),('2020-05-23',1.09005),('2020-05-24',1.09005),('2020-05-25',1.08929),('2020-05-26',1.09195),('2020-05-27',1.09585),('2020-05-28',1.101263),('2020-05-29',1.109405),('2020-05-30',1.1105),('2020-05-31',1.1105),('2020-06-01',1.113217),('2020-06-02',1.117323),('2020-06-03',1.123249),('2020-06-04',1.133845),('2020-06-05',1.129095),('2020-06-06',1.12915),('2020-06-07',1.130172),('2020-06-08',1.129494),('2020-06-09',1.133906),('2020-06-10',1.13775),('2020-06-11',1.129883),('2020-06-12',1.125715),('2020-06-13',1.12554),('2020-06-14',1.12473),('2020-06-15',1.132982),('2020-06-16',1.125937),('2020-06-17',1.124474),('2020-06-18',1.120933),('2020-06-19',1.11795),('2020-06-20',1.117735),('2020-06-21',1.118089),('2020-06-22',1.127319),('2020-06-23',1.13082),('2020-06-24',1.125252),('2020-06-25',1.122271),('2020-06-26',1.121855),('2020-06-27',1.121855),('2020-06-28',1.122441),('2020-06-29',1.124895),('2020-06-30',1.123531),('2020-07-01',1.125235),('2020-07-02',1.124181),('2020-07-03',1.124733),('2020-07-04',1.1245),('2020-07-05',1.124533),('2020-07-06',1.131055),('2020-07-07',1.12738),('2020-07-08',1.13327),('2020-07-09',1.128733),('2020-07-10',1.13006),('2020-07-11',1.13),('2020-07-12',1.131602),('2020-07-13',1.134529),('2020-07-14',1.140914),('2020-07-15',1.141222),('2020-07-16',1.1385),('2020-07-17',1.14295),('2020-07-18',1.14295),('2020-07-19',1.143578),('2020-07-20',1.14464),('2020-07-21',1.15327),('2020-07-22',1.157),('2020-07-23',1.160257),('2020-07-24',1.165605),('2020-07-25',1.16565),('2020-07-26',1.165283),('2020-07-27',1.176363),('2020-07-28',1.172058),('2020-07-29',1.179039),('2020-07-30',1.184819),('2020-07-31',1.177881),('2020-08-01',1.177881),('2020-08-02',1.17946),('2020-08-03',1.176066),('2020-08-04',1.179817),('2020-08-05',1.18726),('2020-08-06',1.188135),('2020-08-07',1.178885),('2020-08-08',1.178885),('2020-08-09',1.177621),('2020-08-10',1.174162),('2020-08-11',1.174362),('2020-08-12',1.17879),('2020-08-13',1.181748),('2020-08-14',1.184245),('2020-08-15',1.18424),('2020-08-16',1.184187),('2020-08-17',1.18735),('2020-08-18',1.19397),('2020-08-19',1.185161),('2020-08-20',1.186545),('2020-08-21',1.17955),('2020-08-22',1.1795);
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

-- Dump completed on 2021-07-07 15:47:58
