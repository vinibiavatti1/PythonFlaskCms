-------------------------------------------------------------------------------
-- Drops
-------------------------------------------------------------------------------

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS contents;
DROP TABLE IF EXISTS pages;
DROP TABLE IF EXISTS history;
DROP TABLE IF EXISTS properties;
DROP TABLE IF EXISTS menus;
DROP TABLE IF EXISTS footer;

-------------------------------------------------------------------------------
-- Creates
-------------------------------------------------------------------------------

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

-- Contents
CREATE TABLE IF NOT EXISTS contents (
    `id` INTEGER PRIMARY KEY,
    `context` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `resource_type` TEXT NOT NULL,
    `data` TEXT NOT NULL DEFAULT '{}',
    `created_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `deleted` INTEGER NOT NULL DEFAULT 0,
    `deleted_on` TIMESTAMP NULL DEFAULT NULL
);

-- Pages
CREATE TABLE IF NOT EXISTS pages (
    `id` INTEGER PRIMARY KEY,
    `context` TEXT NOT NULL,
    `resource_type` TEXT NOT NULL,
    `data` TEXT NOT NULL DEFAULT '{}'
);

-- History
CREATE TABLE IF NOT EXISTS history (
    `id` INTEGER PRIMARY KEY,
    `resource_id` INTEGER NOT NULL,
    `resource_type` TEXT NOT NULL,
    `description` TEXT NOT NULL,
    `created_by` INTEGER NULL,
    `created_on` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `deleted` INTEGER NOT NULL DEFAULT 0
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
