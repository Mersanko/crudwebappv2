-- MySQL dump 10.13  Distrib 5.7.31, for Win32 (AMD64)
--
-- Host: 127.0.0.1    Database: crud
-- ------------------------------------------------------
-- Server version	5.7.31-log

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
-- Table structure for table `college`
--

DROP TABLE IF EXISTS `college`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `college` (
  `collegeNo` int(11) NOT NULL AUTO_INCREMENT,
  `collegeCode` varchar(255) NOT NULL,
  `collegeName` varchar(255) NOT NULL,
  PRIMARY KEY (`collegeNo`,`collegeCode`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `college`
--

LOCK TABLES `college` WRITE;
/*!40000 ALTER TABLE `college` DISABLE KEYS */;
INSERT INTO `college` VALUES (1,'COET','College of Engineering and Technology'),(2,'CSM','College of Science and Mathematics'),(3,'CCS','College of Computer Studies'),(4,'CED','College of Education'),(5,'CASS','College of Arts and Social Sciences'),(6,'CBAA','College of Business Administration and Accountancy'),(7,'CON','College of Nursing');
/*!40000 ALTER TABLE `college` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course` (
  `courseNo` int(11) NOT NULL AUTO_INCREMENT,
  `courseCode` varchar(255) NOT NULL,
  `courseName` varchar(255) NOT NULL,
  `department` int(11) NOT NULL,
  `college` int(11) NOT NULL,
  PRIMARY KEY (`courseNo`,`courseCode`),
  KEY `department` (`department`),
  KEY `college` (`college`),
  CONSTRAINT `course_ibfk_1` FOREIGN KEY (`department`) REFERENCES `department` (`departmentNo`),
  CONSTRAINT `course_ibfk_2` FOREIGN KEY (`college`) REFERENCES `college` (`collegeNo`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1,'BSMETENG','Bachelor of Science in Metallurgical Engineering',1,1),(2,'BSCERENG','Bachelor of Science in Ceramics Engineering',1,1),(3,'BSCHEMENG','Bachelor of Science in Chemical Engineering',2,1),(4,'BSCE','Bachelor of Science in Civil Engineering',3,1),(5,'BSECE','Bachelor of Science in Electronics and Communication Engineering',4,1),(6,'BSCOMENG','Bachelor of Science in Computer Engineering',4,1),(7,'BSEE','Bachelor of Science in Electrical Engineering',4,1),(8,'BSMECHENG','Bachelor of Science in Mechanical Engineering',5,1),(9,'BSBIOGEN','Bachelor of Science in Biology (General)',6,2),(10,'BSBIOBOT','Bachelor of Science in Biology (Botany)',6,2),(11,'BSBIOMARINE','Bachelor of Science in Biology (Marine Biology)',6,2),(12,'BSBIOZOO','Bachelor of Science in Biology (Zoology)',6,2),(13,'BSCHEM','Bachelor of Science in Chemistry ',7,2),(14,'BSMATH','Bachelor of Science in Mathematics ',8,2),(15,'BSSTAT','Bachelor of Science in Statictics ',8,2),(16,'BSPHYSICS','Bachelor of Science in Physics',9,2),(17,'BSCS','Bachelor of Science in Computer Science',10,3),(18,'BSIT','Bachelor of Science in Information Technology',11,3),(19,'BSIS','Bachelor of Science in Information System',12,3),(20,'BSCA','Bachelor of Science in Computer Application',13,3),(21,'BEEDM','Bachelor of Elementary Education Science and Mathematics',14,4),(22,'BSEDBIO','Bachelor of Secondary Education Biology',14,4),(23,'BSEDCHEM','Bachelor of Secondary Education Chemistry',14,4),(24,'BSEDPHYSICS','Bachelor of Secondary Education Physics',14,4),(25,'BSEDMATH','Bachelor of Secondary Education Mathematics',14,4),(26,'BSEDMATH','Bachelor of Secondary Education Mathematicsc`',14,4),(27,'BEELE','Bachelor of Elementary Education – Language Education',15,4),(28,'BSEDFIL','Bachelor of Secondary Education Filipino',15,4),(29,'BEP','Bachelor of Physical Education',16,4),(30,'BTLEE','Bachelor of Technology and Livelihood Education major in Home Economics',17,4),(31,'BTVTEDT','Bachelor of Technical-Vocational Teacher Education major in Drafting Technology',17,4),(32,'BSPSYCH','Bachelor of Science in Psychology',18,5),(33,'BAENG','Bachelor of Arts in English',19,5),(34,'MELS','Master in English Language Studies (Non-Thesis Program)',19,5),(35,'MAELS','Master of Arts in English Language Studies',19,5),(36,'BAFOL','Bachelor of Arts in Filipino & Other Languages',20,5),(37,'MAFIL','Master of Arts in Filipino',20,5),(38,'MFIL','Master of Filipino',20,5),(39,'PhDPHILFIL','Doctor of Philosophy in Filipino',20,5),(40,'BAHISTORY','Bachelor of Arts in History',21,5),(41,'BAPOLSCI','Bachelor of Arts in Political Science',22,5),(42,'BASOCIO','Bachelor of Arts in Sociology',23,5),(43,'BSA','Bachelor of Science in Accountancy',24,6),(44,'BSECON','Bachelor of Science in Economics',25,6),(45,'BSBE','Bachelor of Science in Business Administration major in Business Economics',25,6),(46,'BSBAMM','Bachelor of Science in Business Administration major in Marketing Management',26,6),(47,'BSENTREP','Bachelor of Science major in Entrepreneurship',26,6),(48,'BSHM','Bachelor of Science in Hospitality Management',27,6),(49,'BSN','Bachelor of Science in Nursing',28,7);
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `departmentNo` int(11) NOT NULL AUTO_INCREMENT,
  `departmentName` varchar(255) DEFAULT NULL,
  `college` int(11) DEFAULT NULL,
  PRIMARY KEY (`departmentNo`),
  KEY `collegeNo` (`college`),
  CONSTRAINT `department_ibfk_1` FOREIGN KEY (`college`) REFERENCES `college` (`collegeNo`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Department of Materials and Resources Engineering and Technology',1),(2,'Department of Chemical Engineering and Technology',1),(3,'Department of Civil Engineering',1),(4,'Department of Electrical and Electronics Engineering and Technology',1),(5,'Department of Mechanical Engineering and Technology',1),(6,'Department of Biological Sciences',2),(7,'Department of Chemistry',2),(8,'Department of Mathematics & Statistics',2),(9,'Department of Physics',2),(10,'Department of Computer Science',3),(11,'Department of Information Technology',3),(12,'Department of Information System',3),(13,'Department of Computer Application',3),(14,'Department of Science and Mathematics Education',4),(15,'Department of Professional Education',4),(16,'Department of Physical Education',4),(17,'Department of Techonology Teacher Education',4),(18,'Department of Psychology',5),(19,'Department of English',5),(20,'Department of Filipino & Other Languages',5),(21,'Department of History',5),(22,'Department of Political Science',5),(23,'Department of Sociology',5),(24,'Department of Accountancy',6),(25,'Department of Economics',6),(26,'Department of Marketing',6),(27,'Department of Hospitality & Tourism Management',6),(28,'Department of Nursing',7);
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `record`
--

DROP TABLE IF EXISTS `record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `record` (
  `noOfinsertion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `record`
--

LOCK TABLES `record` WRITE;
/*!40000 ALTER TABLE `record` DISABLE KEYS */;
INSERT INTO `record` VALUES (1),(1),(1),(1),(1);
/*!40000 ALTER TABLE `record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `rawid` int(11) NOT NULL AUTO_INCREMENT,
  `idno` varchar(255) NOT NULL,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` enum('Male','Female') NOT NULL,
  `contactno` varchar(255) NOT NULL,
  `course` int(11) NOT NULL,
  `yearLevel` int(11) NOT NULL,
  `department` int(11) NOT NULL,
  `college` int(11) NOT NULL,
  PRIMARY KEY (`rawid`,`idno`),
  KEY `course` (`course`),
  KEY `department` (`department`),
  KEY `college` (`college`),
  CONSTRAINT `students_ibfk_1` FOREIGN KEY (`course`) REFERENCES `course` (`courseNo`),
  CONSTRAINT `students_ibfk_2` FOREIGN KEY (`department`) REFERENCES `department` (`departmentNo`),
  CONSTRAINT `students_ibfk_3` FOREIGN KEY (`college`) REFERENCES `college` (`collegeNo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'2020-0001','Anus','Voldigoald',20,'Male','09657287028',4,2,3,1),(2,'2020-0002','Hinata','Shoyo',19,'Male','09657287028',49,2,28,7),(3,'2020-0003','Chizuru','Ichinose',19,'Female','09464565153',48,3,27,6),(4,'2020-0004','Natsu','Dragnel',17,'Male','09752936524',12,4,6,2),(5,'2020-0005','Mersan','Canonigo',29,'Male','09061163459',17,4,10,3);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-08 14:51:09
