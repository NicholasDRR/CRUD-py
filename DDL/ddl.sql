-- crud.sales definition

CREATE TABLE `sales` (
  `id_product` int NOT NULL AUTO_INCREMENT,
  `name_product` varchar(30) DEFAULT NULL,
  `price` float DEFAULT NULL,
  PRIMARY KEY (`id_product`)
) ENGINE=MyISAM AUTO_INCREMENT=127 DEFAULT CHARSET=utf8mb3;