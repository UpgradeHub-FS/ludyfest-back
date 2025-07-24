-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: localhost    Database: ludyfest
-- ------------------------------------------------------
-- Server version	8.0.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Conciertos'),(2,'Parties'),(3,'Experiencias'),(4,'Torneos'),(5,'Cultura'),(6,'Cine');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `events` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `date` datetime NOT NULL,
  `price` float NOT NULL,
  `capacity` int NOT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `image` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` tinyint NOT NULL DEFAULT '1',
  `categories_id` int NOT NULL,
  `users_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_events_categories_idx` (`categories_id`),
  KEY `fk_events_users1_idx` (`users_id`),
  CONSTRAINT `fk_events_categories` FOREIGN KEY (`categories_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `fk_events_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `events`
--

LOCK TABLES `events` WRITE;
/*!40000 ALTER TABLE `events` DISABLE KEYS */;
INSERT INTO `events` VALUES (1,'Festival de Jazz','Artistas de jazz internacionales en directo.','2025-08-10 19:00:00',25.5,300,'Parque Central, Madrid',40.4168,-3.7038,'jazzfest.jpg',1,1,1),(2,'Rock Alternativo','Bandas underground en vivo.','2025-09-14 21:00:00',18,250,'Sala Caracol, Madrid',40.402,-3.6962,'rock.jpg',1,1,2),(3,'Concierto Clásico','Orquesta sinfónica en vivo.','2025-10-01 20:00:00',30,400,'Teatro Real, Madrid',40.4181,-3.7123,'clasico.jpg',1,1,3),(4,'Concierto Indie','Nuevas bandas independientes.','2025-08-22 19:30:00',15,200,'Matadero Madrid',40.3902,-3.698,'indie.jpg',1,1,4),(5,'Festival de Food Trucks','Comida urbana y música en vivo.','2025-08-20 12:00:00',5,400,'Plaza Mayor',40.4153,-3.7074,'foodtrucks.jpg',1,2,5),(6,'Fiesta DJ Electrónica','Luces y música hasta el amanecer.','2025-08-30 23:00:00',20,350,'Sala Riviera',40.4156,-3.7195,'djparty.jpg',1,2,6),(7,'Fiesta en la Playa','Música, cocktails y arena.','2025-08-25 18:00:00',12,500,'Playa de la Barceloneta',41.3784,2.1925,'playa.jpg',1,2,7),(8,'Noche de Reggaetón','Hits urbanos y bailarines en vivo.','2025-09-09 22:00:00',17,300,'Teatro Kapital',40.4089,-3.6975,'reggaeton.jpg',1,2,8),(9,'Ruta en Kayak','Explora el embalse en kayak.','2025-08-27 10:00:00',20,20,'Embalse de San Juan',40.3641,-4.2453,'kayak.jpg',1,3,9),(10,'Clase de Cocina','Aprende recetas locales.','2025-09-03 16:00:00',25,15,'Cocina Lab Madrid',40.425,-3.6999,'cocina.jpg',1,3,10),(11,'Tour Fotográfico','Descubre rincones escondidos.','2025-08-29 18:00:00',10,30,'Centro de Madrid',40.4168,-3.7038,'foto.jpg',1,3,11),(12,'Senderismo Nocturno','Ruta guiada bajo las estrellas.','2025-09-05 20:00:00',8,25,'Sierra de Guadarrama',40.785,-3.9545,'senderismo.jpg',1,3,12),(13,'Torneo de Ajedrez','Competencia abierta.','2025-10-08 10:00:00',5,60,'Centro Deportivo Chamberí',40.4325,-3.7162,'ajedrez.jpg',1,4,13),(14,'Torneo de FIFA','Videojuego en pantalla gigante.','2025-09-10 17:00:00',10,40,'Zona Gaming Madrid',40.4371,-3.7035,'fifa.jpg',1,4,14),(15,'Torneo de Pádel','Equipos amateur.','2025-08-31 09:00:00',7,32,'Club Deportivo Vallecas',40.3825,-3.6239,'padel.jpg',1,4,15),(16,'Torneo de Basket 3x3','Partidos rápidos, alto nivel.','2025-09-20 16:00:00',0,24,'Parque Rodríguez Sahagún',40.481,-3.7094,'basket.jpg',1,4,1),(17,'Obra de Teatro Don Quijote','Adaptación contemporánea.','2025-10-01 20:00:00',12,120,'Teatro Español',40.4138,-3.7025,'teatro.jpg',1,5,2),(18,'Espectáculo Flamenco','Flamenco tradicional en tablao.','2025-09-05 21:00:00',15,200,'La Quimera',40.42,-3.7035,'flamenco.jpg',1,5,3),(19,'Taller de Pintura','Aprende técnicas de acuarela.','2025-07-28 17:00:00',15,25,'Centro Cultural Lavapiés',40.4047,-3.7003,'pintura.jpg',1,5,4),(20,'Exposición Arte Moderno','Obras de artistas contemporáneos.','2025-08-18 11:00:00',3,80,'Museo Arte Contemporáneo',40.4261,-3.7092,'arte.jpg',1,5,5),(21,'Cine al Aire Libre','Películas clásicas al exterior.','2025-08-05 22:00:00',0,150,'Parque del Oeste',40.4314,-3.7289,'cine.jpg',1,6,6),(22,'Cine de Terror','Maratón de películas de miedo.','2025-10-31 20:00:00',8,200,'Autocine Madrid',40.4699,-3.7033,'terror.jpg',1,6,7),(23,'Documentales Sociales','Proyecciones + debate.','2025-09-12 18:30:00',5,100,'Cineteca Madrid',40.3903,-3.6982,'docu.jpg',1,6,8),(24,'Cine Infantil','Películas para toda la familia.','2025-08-15 11:00:00',3,120,'Cinesa Méndez Álvaro',40.3972,-3.6895,'infantil.jpg',1,6,9);
/*!40000 ALTER TABLE `events` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `register_to_event`
--

DROP TABLE IF EXISTS `register_to_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register_to_event` (
  `id` int NOT NULL AUTO_INCREMENT,
  `users_id` int NOT NULL,
  `events_id` int NOT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_users_has_events_events1_idx` (`events_id`),
  KEY `fk_users_has_events_users1_idx` (`users_id`),
  CONSTRAINT `fk_users_has_events_events1` FOREIGN KEY (`events_id`) REFERENCES `events` (`id`),
  CONSTRAINT `fk_users_has_events_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register_to_event`
--

LOCK TABLES `register_to_event` WRITE;
/*!40000 ALTER TABLE `register_to_event` DISABLE KEYS */;
/*!40000 ALTER TABLE `register_to_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(90) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `rol` enum('admin','user','guest') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'guest',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Ana Torres','ana.torres@example.com','hashed_password1','admin'),(2,'Carlos Pérez','carlos.perez@example.com','hashed_password2','user'),(3,'Lucía Gómez','lucia.gomez@example.com','hashed_password3','guest'),(4,'Diego Ramírez','diego.ramirez@example.com','hashed_password4','user'),(5,'María López','maria.lopez@example.com','hashed_password5','guest'),(6,'Jorge Sánchez','jorge.sanchez@example.com','hashed_password6','admin'),(7,'Valentina Ruiz','valentina.ruiz@example.com','hashed_password7','user'),(8,'Fernando Díaz','fernando.diaz@example.com','hashed_password8','user'),(9,'Laura Herrera','laura.herrera@example.com','hashed_password9','guest'),(10,'Andrés Rojas','andres.rojas@example.com','hashed_password10','user'),(11,'Isabel Morales','isabel.morales@example.com','hashed_password11','admin'),(12,'Pablo Méndez','pablo.mendez@example.com','hashed_password12','user'),(13,'Camila Soto','camila.soto@example.com','hashed_password13','guest'),(14,'Ricardo Navarro','ricardo.navarro@example.com','hashed_password14','user'),(15,'Natalia Castro','natalia.castro@example.com','hashed_password15','guest');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-07-24 12:37:06
