--- Create a force_name table if doesn't exists
CREATE TABLE IF NOT EXISTS `id_not_null`
(
    id INT DEFAULT 1 NOT NULL,
    name VARCHAR(256)
);
