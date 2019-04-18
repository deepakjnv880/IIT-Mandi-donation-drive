-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: IDS
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blog`
--

DROP TABLE IF EXISTS `blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `pemail` varchar(100) DEFAULT NULL,
  `cemail` varchar(100) DEFAULT NULL,
  `dtype` varchar(100) DEFAULT NULL,
  `post` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `filename` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (1,'b17086','nss','daily_use_item','HI brother. How are you?','2019-04-12 10:51:22.785288',NULL),(2,'b17086','nss','daily_use_item','Hi i have one extra shirt. i want to donate it?','2019-04-12 10:52:21.417230','s-l300.jpg'),(3,'Alumuni','programmings','club_requirement','I need 20000.','2019-04-12 10:53:04.041015',NULL),(4,'Alumuni','programmings','club_requirement','needed 2 KG apple. 400 rupee needed','2019-04-12 10:57:48.514225','rag.jpeg'),(5,'Alumuni','nss','club_requirement','Blood donation camp is going on.','2019-04-12 11:10:23.764913',NULL),(6,'Alumuni','programmings','club_requirement','Blood donation camp is going on.','2019-04-12 11:13:00.673556',NULL),(7,'anyone','nss','social','Blood donation camp is going on.','2019-04-12 11:13:36.218034',NULL),(8,'anyone','nss','social','Donation drive is going on. Keep donating.','2019-04-12 11:14:09.594815','broken-glasses-330x220.jpg'),(9,'b17086','nss','daily_use_item','','2019-04-12 18:37:12.820499',NULL);
/*!40000 ALTER TABLE `blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `club`
--

DROP TABLE IF EXISTS `club`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `club` (
  `cname` varchar(100) DEFAULT NULL,
  `cemail` varchar(100) NOT NULL,
  `ctype` varchar(100) DEFAULT NULL,
  `cpassword` varchar(100) DEFAULT NULL,
  `online` int(11) DEFAULT NULL,
  PRIMARY KEY (`cemail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `club`
--

LOCK TABLES `club` WRITE;
/*!40000 ALTER TABLE `club` DISABLE KEYS */;
INSERT INTO `club` VALUES ('nss','nss@iitmandi.ac.in','social','nss',1),('programmings','programmings@iitmandi.ac.in','technical','hi234',1);
/*!40000 ALTER TABLE `club` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `person` (
  `pname` varchar(100) DEFAULT NULL,
  `ptype` varchar(100) DEFAULT NULL,
  `pemail` varchar(100) NOT NULL,
  `ppassword` varchar(100) DEFAULT NULL,
  `online` int(11) DEFAULT NULL,
  PRIMARY KEY (`pemail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES ('Deepak kumar','student','b17039@student.iitmandi.ac.in','hi123',1),('2','student','b17086@student.iitmandi.ac.in','hi123',1);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-19  0:12:49
