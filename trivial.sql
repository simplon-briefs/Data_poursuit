-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 04, 2020 at 10:23 AM
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
(2, 'Quel est le support le plus adapté pour stocker un jeu de données important.', 1, 1),
(3, 'En 2020 de combien le volume de données numériques créés a-t-il augmenté En 2020 par rapport à 2010 ?', 1, 2),
(4, 'Par combien sera multiplier le volume du big data en 2035 par rapport a 2020', 1, 3),
(5, 'Combien d’heures de vidéo sont téléchargées sur YouTube chaque minute ?', 1, 1),
(6, 'Vrai ou faux ? 90 % des données dans le monde ont été créées dans les deux dernières années.', 1, 2),
(7, 'Quelle entreprise informatique est le plus grand fournisseur Big Data dans le monde ?', 1, 2),
(8, 'Le modèle de programmation MapReduce a été initialement développé par…', 1, 2),
(9, 'Qui a créé le framework logiciel Hadoop, très populaire dans le monde du Big Data ?', 1, 2),
(10, 'Combien de gigaoctets y a-t-il dans un exaoctet ?', 1, 1),
(11, 'Combien d’exaoctets de données le LHC «Large Hadron Collider» peut-il produire par jour ?', 1, 3),
(12, 'Une fois terminé, le flux de données généré par le radiotélescope SKA sera équivalent à…', 1, 3),
(13, 'Lequel des éléments suivants est une base de données distribuée à plusieurs niveaux?', 1, 3),
(14, 'Le volume de données des entreprise double tout les ... an(s)', 1, 2),
(15, 'Quel est le \"poids\" du Big Data en 2020?', 1, 1);

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
(1, 16, 'Un SSD avec un système de sécurité.', 1),
(2, 16, 'Un disque dur classique.', 0),
(3, 16, 'Une clé Usb avec un mot de passe.', 0),
(4, 1, 'Volume, Vitesse, Variété, Véracité, Variété.', 1),
(5, 2, '610 zetaoctet de données', 1),
(6, 5, '24', 1),
(7, 6, '45', 1),
(8, 7, '35', 0),
(9, 7, '60', 0),
(10, 7, '100', 1),
(11, 8, 'VRAI', 1),
(12, 8, 'FAUX', 0),
(13, 9, 'DELL', 0),
(14, 9, 'HP', 0),
(15, 9, 'IBM', 1),
(16, 10, 'Appache Software Foundation', 0),
(17, 10, 'Google', 1),
(18, 10, 'Microsoft Research', 0),
(19, 11, 'Doug CUTTING', 1),
(20, 11, 'Richard STALLMAN', 0),
(21, 11, 'Alan COX', 0),
(22, 12, 'Un millier', 0),
(23, 12, 'Un million', 0),
(24, 12, 'Un milliard', 1),
(25, 13, '5 exaoctets', 0),
(43, 13, '50 exaoctets', 0),
(44, 13, '500 exaoctets', 1),
(45, 14, 'Un dixième du trafic Internet global', 0),
(46, 14, 'Deux fois le  trafic Internet global', 0),
(47, 14, 'Dix fois le trafic Internet global', 1),
(49, 16, 'HDFS', 0),
(50, 16, 'HBase', 1),
(51, 16, 'Les deux', 0),
(52, 16, 'Aucune de ces réponses', 0),
(54, 2, '110 zetaoctet de données', 0),
(55, 2, '1010 zetaoctet de données', 0),
(56, 17, '1', 0),
(57, 17, '1,2', 1),
(58, 17, '2', 0);

-- --------------------------------------------------------

--
-- Table structure for table `theme`
--

CREATE TABLE `theme` (
  `id_theme` int(1) NOT NULL,
  `nom_theme` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `theme`
--

INSERT INTO `theme` (`id_theme`, `nom_theme`) VALUES
(1, 'big data'),
(2, 'ia'),
(3, 'ethique'),
(4, 'python'),
(5, 'mathématique');

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
  ADD PRIMARY KEY (`id_theme`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `joueurs`
--
ALTER TABLE `joueurs`
  MODIFY `id_joueur` int(2) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `theme`
--
ALTER TABLE `theme`
  MODIFY `id_theme` int(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`id_theme`) REFERENCES `theme` (`id_theme`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
