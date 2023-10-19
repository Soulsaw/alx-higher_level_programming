--- Create a force_name table if doesn't exists
CREATE TABLE IF NOT EXISTS unique_id
(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
