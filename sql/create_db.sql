-------------------------------------------------------------------------------
-- Drops
-------------------------------------------------------------------------------

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS objects;
DROP TABLE IF EXISTS properties;
DROP TABLE IF EXISTS menus;
DROP TABLE IF EXISTS footer;

-------------------------------------------------------------------------------
-- Creates
-------------------------------------------------------------------------------

-- Objects
CREATE TABLE IF NOT EXISTS objects (
    `id` INTEGER PRIMARY KEY,
    `context` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `object_type` TEXT NOT NULL,
    `object_subtype` TEXT NOT NULL,
    `properties` TEXT NOT NULL DEFAULT '{}',
    `created_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `deleted_on` TIMESTAMP NULL DEFAULT NULL,
    `deleted` INTEGER NOT NULL DEFAULT 0
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
    `value` TEXT NULL
);

-- Menus
CREATE TABLE IF NOT EXISTS menus (
    `id` INTEGER PRIMARY KEY,
    `context` TEXT NOT NULL,
    `data` TEXT NOT NULL DEFAULT '{}'
);

-- Footers
CREATE TABLE IF NOT EXISTS footers (
    `id` INTEGER PRIMARY KEY,
    `context` TEXT NOT NULL,
    `data` TEXT NOT NULL DEFAULT '{}'
);

-- Admin user table
CREATE TABLE IF NOT EXISTS users (
    `id` INTEGER PRIMARY KEY,
    `name` TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `password` TEXT NOT NULL,
    `permission` TEXT NOT NULL,
    `last_login` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `active` INTEGER NOT NULL DEFAULT 1,
    `deleted` INTEGET NOT NULL DEFAULT 0
);
