SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for hosts
-- ----------------------------
DROP TABLE IF EXISTS `hosts`;
CREATE TABLE `hosts` (
`host`  varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL ,
`url`  varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
`title`  text CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL ,
`firstseen`  datetime NULL DEFAULT NULL ,
`lastseen`  datetime NULL DEFAULT NULL ,
`found_links`  int(11) NULL DEFAULT NULL ,
`server`  varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL ,
PRIMARY KEY (`host`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=latin1 COLLATE=latin1_swedish_ci

;
