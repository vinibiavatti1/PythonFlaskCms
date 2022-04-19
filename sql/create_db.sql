-------------------------------------------------------------------------------
-- Drops
-------------------------------------------------------------------------------

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS objects;
DROP TABLE IF EXISTS properties;
DROP TABLE IF EXISTS menus;
DROP TABLE IF EXISTS footer;
DROP TABLE IF EXISTS history;

-------------------------------------------------------------------------------
-- Tables
-------------------------------------------------------------------------------

-- Objects
CREATE TABLE IF NOT EXISTS objects (
    `id` INTEGER PRIMARY KEY,
    `context` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `object_type` TEXT NOT NULL,
    `object_order` INTEGER NOT NULL,
    `reference_name` TEXT NULL,
    `properties` TEXT NOT NULL DEFAULT '{}',
    `created_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `deleted_on` TIMESTAMP NULL DEFAULT NULL,
    `deleted` INTEGER NOT NULL DEFAULT 0,
    UNIQUE(`context`, `name`)
);

-- History
CREATE TABLE IF NOT EXISTS history (
    `id` INTEGER PRIMARY KEY,
    `context` TEXT NOT NULL,
    `table_name` TEXT NOT NULL,
    `target_id` INTEGER NOT NULL,
    `description` TEXT NOT NULL,
    `created_by` INTEGER NULL,
    `created_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Properties
CREATE TABLE IF NOT EXISTS properties (
    `id` INTEGER PRIMARY KEY,
    `context` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `value` TEXT NULL,
    UNIQUE(`context`, `name`)
);

-- Admin user table
CREATE TABLE IF NOT EXISTS users (
    `id` INTEGER PRIMARY KEY,
    `name` TEXT NOT NULL,
    `email` TEXT NOT NULL UNIQUE,
    `password` TEXT NOT NULL,
    `permission` TEXT NOT NULL,
    `last_login` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `active` INTEGER NOT NULL DEFAULT 1,
    `deleted` INTEGET NOT NULL DEFAULT 0
);

-------------------------------------------------------------------------------
-- Indexes
-------------------------------------------------------------------------------

-- Objects
CREATE UNIQUE INDEX idx_objects_name
ON objects (name);
