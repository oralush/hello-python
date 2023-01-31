DROP TABLE IF EXISTS `data`;
CREATE TABLE `data` (
  `id` int(11) DEFAULT NULL,
  `text` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO `data` VALUES (1,'Hello world!\n');
