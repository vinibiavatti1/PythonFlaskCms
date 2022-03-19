-------------------------------------------------------------------------------
-- Drops
-------------------------------------------------------------------------------

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS contents;
DROP TABLE IF EXISTS pages;
DROP TABLE IF EXISTS history;
DROP TABLE IF EXISTS properties;

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
    `idiom` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `type` TEXT NOT NULL,
    `private` INTEGER NOT NULL DEFAULT 0,
    `published` INTEGER NOT NULL DEFAULT 1,
    `deleted` INTEGER NOT NULL DEFAULT 0,
    `created_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `data` TEXT NOT NULL DEFAULT '{}'
);

-- Pages
CREATE TABLE IF NOT EXISTS pages (
    `id` INTEGER PRIMARY KEY,
    `idiom` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `private` INTEGER NOT NULL DEFAULT 0,
    `published` INTEGER NOT NULL DEFAULT 1,
    `deleted` INTEGER NOT NULL DEFAULT 0,
    `data` TEXT NOT NULL DEFAULT '{}'
);

-- History
CREATE TABLE IF NOT EXISTS history (
    `id` INTEGER PRIMARY KEY,
    `type` TEXT NOT NULL,
    `resource_id` INTEGER NOT NULL,
    `description` TEXT NOT NULL,
    `created_by` INTEGER NOT NULL,
    `created_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `deleted` INTEGER NOT NULL DEFAULT 0
);

-- Properties
CREATE TABLE IF NOT EXISTS properties (
    `id` INTEGER PRIMARY KEY,
    `idiom` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `value` TEXT NULL
);
