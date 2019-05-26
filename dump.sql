-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: IDS
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.18.04.1

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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (1,'anyone','nss','social','Donative drive is going on... KEEP DONATING','2019-05-17 11:35:00.192786','depositphotos_146108105-stock-photo-donation-box-with-clothes.jpg'),(2,'Alumuni','photography','club_requirement','Our club needed  20000 for camera','2019-05-17 11:41:57.920903','camera.jpg'),(3,'b17039','nss','daily_use_item','I want to donate my torn wallet.It is in usable form','2019-05-17 11:43:03.917012','index.jpeg'),(4,'anyone','nss','social','Blood donation drive is going on...KEEP DONATING','2019-05-17 11:43:50.381584','blood.jpg');
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
INSERT INTO `club` VALUES ('Art geeks','artgeek@iitmandi.ac.in','cultural','pbkdf2:sha256:50000$Gr8Typm8$482f49c137f347faeff7931579c28cbde7d182966d951fe0e73d330be0d83e7d',1),('nss','nss@iitmandi.ac.in','social','nss',1),('photography','photography@iitmandi.ac.in','cultural','hi234',1),('programmings','programmings@iitmandi.ac.in','technical','hi234',1);
/*!40000 ALTER TABLE `club` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `club_requirement`
--

DROP TABLE IF EXISTS `club_requirement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `club_requirement` (
  `blog_id` varchar(100) NOT NULL,
  `userid` varchar(100) NOT NULL,
  `upvote` varchar(10) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `amount_donated` float(8,5) DEFAULT '0.00000',
  `transaction_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`blog_id`,`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `club_requirement`
--

LOCK TABLES `club_requirement` WRITE;
/*!40000 ALTER TABLE `club_requirement` DISABLE KEYS */;
INSERT INTO `club_requirement` VALUES ('2','b17039@student.iitmandi.ac.in','NULL','good one','2019-05-26 11:05:50.136754',47.00000,'20190523111212800110168607900520713');
/*!40000 ALTER TABLE `club_requirement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_use_item`
--

DROP TABLE IF EXISTS `daily_use_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `daily_use_item` (
  `blog_id` varchar(100) NOT NULL,
  `userid` varchar(100) NOT NULL,
  `recommended` varchar(10) DEFAULT NULL,
  `not_recommended` varchar(10) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`blog_id`,`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_use_item`
--

LOCK TABLES `daily_use_item` WRITE;
/*!40000 ALTER TABLE `daily_use_item` DISABLE KEYS */;
INSERT INTO `daily_use_item` VALUES ('3','b17039@student.iitmandi.ac.in','NULL','NULL',NULL,'2019-05-26 11:05:38.675519'),('5','b17039@student.iitmandi.ac.in','YES','NULL','ywa','2019-05-26 11:14:48.374821'),('5','b17086@student.iitmandi.ac.in',NULL,NULL,'good one','2019-05-19 16:05:49.045407'),('5','nss@iitmandi.ac.in','NULL','NULL',NULL,'2019-05-24 11:40:52.663288'),('5','programmings@iitmandi.ac.in','NULL','YES','nice one','2019-05-24 12:44:24.618888');
/*!40000 ALTER TABLE `daily_use_item` ENABLE KEYS */;
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
INSERT INTO `person` VALUES ('Deepak kumar','student','b17039@student.iitmandi.ac.in','hi123',1),('vinay kumar','student','b17068@student.iitmandi.ac.in','vinay',1),('2','student','b17086@student.iitmandi.ac.in','hi123',1);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_blog`
--

DROP TABLE IF EXISTS `social_blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_blog` (
  `blog_id` varchar(100) NOT NULL,
  `userid` varchar(100) NOT NULL,
  `interested` varchar(10) DEFAULT NULL,
  `not_interested` varchar(10) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`blog_id`,`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_blog`
--

LOCK TABLES `social_blog` WRITE;
/*!40000 ALTER TABLE `social_blog` DISABLE KEYS */;
INSERT INTO `social_blog` VALUES ('1','b17039@student.iitmandi.ac.in','YES','NULL',NULL,'2019-05-26 11:09:09.740154'),('4','b17039@student.iitmandi.ac.in','NULL','YES','why bro','2019-05-26 11:05:22.568220'),('4','b17086@student.iitmandi.ac.in','NULL','NULL','Timing is not comfortable.','2019-05-19 16:51:48.676554'),('4','programmings@iitmandi.ac.in','NULL','NULL',NULL,'2019-05-24 12:44:55.193500');
/*!40000 ALTER TABLE `social_blog` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-05-26 20:30:38
