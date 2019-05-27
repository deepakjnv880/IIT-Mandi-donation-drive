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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog`
--

LOCK TABLES `blog` WRITE;
/*!40000 ALTER TABLE `blog` DISABLE KEYS */;
INSERT INTO `blog` VALUES (1,'b17039','nss','daily_use_item','I have a torn shoes. I want to donate it.','2019-05-27 16:25:27.028225','old-torn-shoes-isolated-on-450w-288798116.jpg'),(2,'anyone','nss','social','Donation drive is going on. Keep donating','2019-05-27 16:26:17.261894','depositphotos_146108105-stock-photo-donation-box-with-clothes.jpg'),(3,'Alumuni','photography','club_requirement','Our club needed 10000 for camera','2019-05-27 16:27:18.496209','camera.jpg'),(4,'b17068','nss','daily_use_item','I have a torn wallet.It is in usable form. I want to donate it.','2019-05-27 16:39:47.535792','index.jpeg'),(5,'anyone','nss','social','Blood donation camp is going on keep donating..','2019-05-27 16:40:42.858379','blood.jpg');
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
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`cemail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `club`
--

LOCK TABLES `club` WRITE;
/*!40000 ALTER TABLE `club` DISABLE KEYS */;
INSERT INTO `club` VALUES ('nss','nss@iitmandi.ac.in','social','pbkdf2:sha256:50000$DcBO8xBp$4134ba1db9c4439f8d54e5c81c7cb398222f828e5ac5702739907292d07a48ed',0),('photography','photography@iitmandi.ac.in','technical','pbkdf2:sha256:50000$fkRlhAcY$379e1c2d2628cd564e5de95a4fac9ef705bbd0a11596b5936243cdd248c8d1f2',0);
/*!40000 ALTER TABLE `club` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `club_requirement`
--

DROP TABLE IF EXISTS `club_requirement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `club_requirement` (
  `blog_id` int(11) NOT NULL,
  `userid` varchar(100) NOT NULL,
  `upvote` varchar(10) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `amount_donated` int(11) DEFAULT '0',
  `transaction_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`blog_id`,`userid`),
  CONSTRAINT `club_requirement_ibfk_1` FOREIGN KEY (`blog_id`) REFERENCES `blog` (`did`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `club_requirement`
--

LOCK TABLES `club_requirement` WRITE;
/*!40000 ALTER TABLE `club_requirement` DISABLE KEYS */;
/*!40000 ALTER TABLE `club_requirement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_use_item`
--

DROP TABLE IF EXISTS `daily_use_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `daily_use_item` (
  `blog_id` int(11) NOT NULL,
  `userid` varchar(100) NOT NULL,
  `recommended` varchar(10) DEFAULT NULL,
  `not_recommended` varchar(10) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`blog_id`,`userid`),
  CONSTRAINT `daily_use_item_ibfk_1` FOREIGN KEY (`blog_id`) REFERENCES `blog` (`did`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_use_item`
--

LOCK TABLES `daily_use_item` WRITE;
/*!40000 ALTER TABLE `daily_use_item` DISABLE KEYS */;
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
  `rating` int(11) DEFAULT NULL,
  PRIMARY KEY (`pemail`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES ('Deepak kumar','student','b17039@student.iitmandi.ac.in','pbkdf2:sha256:50000$0eRzLrCG$79958553bad8195651d1ad3d86d1835aab9f5d47bc84cea6f0daddcf1377104e',0),('vinay kumar','student','b17068@students.iitmandi.ac.in','pbkdf2:sha256:50000$5JBWlYQa$fb3c4170b85ff232c45676b93c5c9c327b6e895422f36e5dcb68daae4a2185b3',0);
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_blog`
--

DROP TABLE IF EXISTS `social_blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `social_blog` (
  `blog_id` int(11) NOT NULL,
  `userid` varchar(100) NOT NULL,
  `interested` varchar(10) DEFAULT NULL,
  `not_interested` varchar(10) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`blog_id`,`userid`),
  CONSTRAINT `social_blog_ibfk_1` FOREIGN KEY (`blog_id`) REFERENCES `blog` (`did`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_blog`
--

LOCK TABLES `social_blog` WRITE;
/*!40000 ALTER TABLE `social_blog` DISABLE KEYS */;
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

-- Dump completed on 2019-05-27 16:43:15
