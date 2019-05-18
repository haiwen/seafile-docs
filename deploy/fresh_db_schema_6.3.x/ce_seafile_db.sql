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

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
--
-- Table structure for table `Branch`
--
DROP TABLE IF EXISTS `Branch`;
CREATE TABLE `Branch` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `repo_id` char(41) NOT NULL,
  `commit_id` char(41) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`,`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `GarbageRepos`
--
DROP TABLE IF EXISTS `GarbageRepos`;
CREATE TABLE `GarbageRepos` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(36) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `InnerPubRepo`
--
DROP TABLE IF EXISTS `InnerPubRepo`;
CREATE TABLE `InnerPubRepo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(37) NOT NULL,
  `permission` char(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `OrgQuota`
--
DROP TABLE IF EXISTS `OrgQuota`;
CREATE TABLE `OrgQuota` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `org_id` int(11) NOT NULL,
  `quota` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `org_id` (`org_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `OrgUserQuota`
--
DROP TABLE IF EXISTS `OrgUserQuota`;
CREATE TABLE `OrgUserQuota` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `org_id` int(11) NOT NULL,
  `user` varchar(255) NOT NULL,
  `quota` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `org_id` (`org_id`,`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `Repo`
--
DROP TABLE IF EXISTS `Repo`;
CREATE TABLE `Repo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(37) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `RepoFileCount`
--
DROP TABLE IF EXISTS `RepoFileCount`;
CREATE TABLE `RepoFileCount` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(36) NOT NULL,
  `file_count` bigint(20) unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `RepoGroup`
--
DROP TABLE IF EXISTS `RepoGroup`;
CREATE TABLE `RepoGroup` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(37) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `permission` char(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`repo_id`),
  KEY `repo_id` (`repo_id`),
  KEY `user_name` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `RepoHead`
--
DROP TABLE IF EXISTS `RepoHead`;
CREATE TABLE `RepoHead` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(37) NOT NULL,
  `branch_name` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `RepoHistoryLimit`
--
DROP TABLE IF EXISTS `RepoHistoryLimit`;
CREATE TABLE `RepoHistoryLimit` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(37) NOT NULL,
  `days` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `RepoInfo`
--
DROP TABLE IF EXISTS `RepoInfo`;
CREATE TABLE `RepoInfo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(36) NOT NULL,
  `name` varchar(255) NOT NULL,
  `update_time` bigint(20) DEFAULT NULL,
  `version` int(11) DEFAULT NULL,
  `is_encrypted` int(11) DEFAULT NULL,
  `last_modifier` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `RepoOwner`
--
DROP TABLE IF EXISTS `RepoOwner`;
CREATE TABLE `RepoOwner` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(37) NOT NULL,
  `owner_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`),
  KEY `owner_id` (`owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `RepoSize`
--
DROP TABLE IF EXISTS `RepoSize`;
CREATE TABLE `RepoSize` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(37) NOT NULL,
  `size` bigint(20) unsigned DEFAULT NULL,
  `head_id` char(41) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `RepoTokenPeerInfo`
--
DROP TABLE IF EXISTS `RepoTokenPeerInfo`;
CREATE TABLE `RepoTokenPeerInfo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` char(41) NOT NULL,
  `peer_id` char(41) DEFAULT NULL,
  `peer_ip` varchar(41) DEFAULT NULL,
  `peer_name` varchar(255) DEFAULT NULL,
  `sync_time` bigint(20) DEFAULT NULL,
  `client_ver` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `RepoTrash`
--
DROP TABLE IF EXISTS `RepoTrash`;
CREATE TABLE `RepoTrash` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(36) NOT NULL,
  `repo_name` varchar(255) DEFAULT NULL,
  `head_id` char(40) DEFAULT NULL,
  `owner_id` varchar(255) DEFAULT NULL,
  `size` bigint(20) DEFAULT NULL,
  `org_id` int(11) DEFAULT NULL,
  `del_time` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`),
  KEY `owner_id` (`owner_id`),
  KEY `org_id` (`org_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `RepoUserToken`
--
DROP TABLE IF EXISTS `RepoUserToken`;
CREATE TABLE `RepoUserToken` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(37) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `token` char(41) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`,`token`),
  KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `RepoValidSince`
--
DROP TABLE IF EXISTS `RepoValidSince`;
CREATE TABLE `RepoValidSince` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(37) NOT NULL,
  `timestamp` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `SeafileConf`
--
DROP TABLE IF EXISTS `SeafileConf`;
CREATE TABLE `SeafileConf` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `cfg_group` varchar(255) NOT NULL,
  `cfg_key` varchar(255) NOT NULL,
  `value` varchar(255) DEFAULT NULL,
  `property` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `SharedRepo`
--
DROP TABLE IF EXISTS `SharedRepo`;
CREATE TABLE `SharedRepo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `repo_id` char(37) DEFAULT NULL,
  `from_email` varchar(255) DEFAULT NULL,
  `to_email` varchar(255) DEFAULT NULL,
  `permission` char(15) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `repo_id` (`repo_id`),
  KEY `from_email` (`from_email`),
  KEY `to_email` (`to_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `SystemInfo`
--
DROP TABLE IF EXISTS `SystemInfo`;
CREATE TABLE `SystemInfo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `info_key` varchar(256) DEFAULT NULL,
  `info_value` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `UserQuota`
--
DROP TABLE IF EXISTS `UserQuota`;
CREATE TABLE `UserQuota` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user` varchar(255) NOT NULL,
  `quota` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `UserShareQuota`
--
DROP TABLE IF EXISTS `UserShareQuota`;
CREATE TABLE `UserShareQuota` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user` varchar(255) NOT NULL,
  `quota` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `VirtualRepo`
--
DROP TABLE IF EXISTS `VirtualRepo`;
CREATE TABLE `VirtualRepo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(36) NOT NULL,
  `origin_repo` char(36) DEFAULT NULL,
  `path` text,
  `base_commit` char(40) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`),
  KEY `origin_repo` (`origin_repo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `WebAP`
--
DROP TABLE IF EXISTS `WebAP`;
CREATE TABLE `WebAP` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `repo_id` char(37) NOT NULL,
  `access_property` char(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `repo_id` (`repo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET character_set_client = @saved_cs_client */;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;