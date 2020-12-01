-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 01, 2020 at 11:02 AM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `trivial`
--
CREATE DATABASE IF NOT EXISTS `trivial` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `trivial`;

-- --------------------------------------------------------

--
-- Table structure for table `joueurs`
--

CREATE TABLE `joueurs` (
  `id_joueur` int(2) NOT NULL,
  `nom_joueur` varchar(50) NOT NULL,
  `points_joueur` int(10) NOT NULL,
  `couleur_joueur` char(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id_question` int(7) NOT NULL,
  `libelle_question` text NOT NULL,
  `id_theme` int(1) NOT NULL,
  `difficulte_question` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id_question`, `libelle_question`, `id_theme`, `difficulte_question`) VALUES
(1, 'Quels sont les \"trois V\" du Big Data ?', 1, 1),
(2, 'Quel est le \"poids\" du big data ?', 1, 2),
(3, 'Quel définition donner au Big Data ?', 1, 1),
(4, 'Quelles étapes pour déployer une solution Big Data ?', 1, 2),
(5, 'De combien le volume de données numériques créés a-t-il augmenté En 2020 par rapport à 2010 ?', 1, 2),
(6, 'Par combien sera multiplier le volume du big data en 2035 par rapport a 2020', 1, 3),
(7, 'Combien d’heures de vidéo sont téléchargées sur YouTube chaque minute ?', 1, 1),
(8, 'Vrai ou faux ? 90 % des données dans le monde ont été créées dans les deux dernières années.', 1, 2),
(9, 'Quelle entreprise informatique est le plus grand fournisseur Big Data dans le monde ?', 1, 2),
(10, 'Le modèle de programmation MapReduce a été initialement développé par…', 1, 2),
(11, 'Qui a créé le framework logiciel Hadoop, très populaire dans le monde du Big Data ?', 1, 2),
(12, 'Combien de gigaoctets y a-t-il dans un exaoctet ?', 1, 1),
(13, 'Combien d’exaoctets de données le LHC «Large Hadron Collider» peut-il produire par jour ?', 1, 3),
(14, 'Une fois terminé, le flux de données généré par le radiotélescope SKA sera équivalent à…', 1, 3),
(15, 'Quel est le rôle de Hadoop dans l’analyse de données volumineuses ?', 1, 3),
(16, 'Lequel des éléments suivants est une base de données distribuée à plusieurs niveaux?', 1, 3),
(17, 'Quel définition donner à Hadoop ?', 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `reponses`
--

CREATE TABLE `reponses` (
  `id_reponse` int(7) NOT NULL,
  `id_question` int(7) NOT NULL,
  `libelle_reponse` text NOT NULL,
  `valeur_reponse` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `reponses`
--

INSERT INTO `reponses` (`id_reponse`, `id_question`, `libelle_reponse`, `valeur_reponse`) VALUES
(19, 1, 'Volume, Vitesse, Variété', 1),
(20, 2, 'en 2020 --> 610 zetaoctet de données', 1),
(21, 3, 'Ensembles de données volumineux, complexes et en constante augmentation qui ne peuvent pas être gérés et manipuler avec des logiciels et techniques classiques.', 1),
(22, 4, '1. Ingestion de données,\r\n2. Stockage de données,\r\n3. Traitement de l’information.', 1),
(23, 5, '23,5 ( (de 2 milliards de téraoctets à 47).', 1),
(24, 6, '45', 1),
(25, 7, '35', 0),
(26, 7, '60', 0),
(27, 7, '100', 1),
(28, 8, 'VRAI', 1),
(29, 8, 'FAUX', 0),
(30, 9, 'DELL', 0),
(31, 9, 'HP', 0),
(32, 9, 'IBM', 1),
(33, 10, 'Appache Software Foundation', 0),
(34, 10, 'Google', 1),
(35, 10, 'Microsoft Research', 0),
(36, 11, 'Doug CUTTING', 1),
(37, 11, 'Richard STALLMAN', 0),
(38, 11, 'Alan COX', 0),
(39, 12, 'Un millier', 0),
(40, 12, 'Un million', 0),
(41, 12, 'Un milliard', 1),
(42, 13, '5 exaoctets', 0),
(43, 13, '50 exaoctets', 0),
(44, 13, '500 exaoctets', 1),
(45, 14, 'Un dixième du trafic Internet global', 0),
(46, 14, 'Deux fois le  trafic Internet global', 0),
(47, 14, 'Dix fois le trafic Internet global', 1),
(48, 15, 'Hadoop facilite l’analyse des données volumineuses car il fournit un stockage et aide à la collecte et au traitement des données.', 1),
(49, 16, 'HDFS', 0),
(50, 16, 'HBase', 1),
(51, 16, 'Les deux ci-dessus', 0),
(52, 16, 'Aucune de ces réponses', 0),
(53, 17, 'Hadoop est un framework logiciel open source, basé sur Java, permettant de stocker des données, et de lancer des applications sur des grappes de machines standards. Cette solution offre un espace de stockage massif pour tous les types de données, une immense puissance de traitement et la possibilité de prendre en charge une quantité de tâches virtuellement illimitée.', 1);

-- --------------------------------------------------------

--
-- Table structure for table `theme`
--

CREATE TABLE `theme` (
  `id-theme` int(1) NOT NULL,
  `nom_theme` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `theme`
--

INSERT INTO `theme` (`id-theme`, `nom_theme`) VALUES
(1, 'Big Data'),
(2, 'IA'),
(3, 'Ethique'),
(4, 'Python'),
(5, 'Mathématique');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `joueurs`
--
ALTER TABLE `joueurs`
  ADD PRIMARY KEY (`id_joueur`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id_question`),
  ADD KEY `id_theme` (`id_theme`);

--
-- Indexes for table `reponses`
--
ALTER TABLE `reponses`
  ADD PRIMARY KEY (`id_reponse`),
  ADD KEY `reponses_ibfk_1` (`id_question`);

--
-- Indexes for table `theme`
--
ALTER TABLE `theme`
  ADD PRIMARY KEY (`id-theme`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id_question` int(7) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `theme`
--
ALTER TABLE `theme`
  MODIFY `id-theme` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
