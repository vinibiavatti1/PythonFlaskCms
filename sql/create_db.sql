-------------------------------------------------------------------------------
-- Drops
-------------------------------------------------------------------------------

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS pages;
DROP TABLE IF EXISTS menus;
DROP TABLE IF EXISTS history;
DROP TABLE IF EXISTS properties;
DROP TABLE IF EXISTS translations;
DROP TABLE IF EXISTS redirects;
DROP TABLE IF EXISTS blocks;

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

-- Pages
CREATE TABLE IF NOT EXISTS pages (
    `id` INTEGER PRIMARY KEY,
    `idiom` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `template` TEXT NOT NULL,
    `active` INTEGER NOT NULL DEFAULT 1,
    `title` TEXT NOT NULL,
    `author` TEXT NULL,
    `description` TEXT NULL,
    `keywords` TEXT NULL,
    `canonical_urls` TEXT NULL,
    `sitemap_active` INTEGER NOT NULL DEFAULT 1,
    `sitemap_priority` TEXT NULL DEFAULT '0.5',
    `sitemap_change_frequently` TEXT NULL DEFAULT 'always',
    `properties` TEXT NULL,
    `html` TEXT NULL,
    `css` TEXT NULL,
    `script` TEXT NULL,
    `json` TEXT NULL,
    `deleted` INTEGER NOT NULL DEFAULT 0,
    `access` INTEGER NOT NULL DEFAULT 1,
    `inject_posts` INTEGER NOT NULL DEFAULT 0,
    `inject_faqs` INTEGER NOT NULL DEFAULT 0,
    `inject_events` INTEGER NOT NULL DEFAULT 0
);

-- Menus
CREATE TABLE IF NOT EXISTS menus (
    `id` INTEGER PRIMARY KEY,
    `idiom` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `active` INTEGER NOT NULL DEFAULT 1,
    `json` TEXT NOT NULL,
    `deleted` INTEGET NOT NULL DEFAULT 0
);

-- History
CREATE TABLE IF NOT EXISTS history (
    `id` INTEGER PRIMARY KEY,
    `type_resource` TEXT,
    `id_resource` INTEGER,
    `description` TEXT NOT NULL,
    `created_by` INTEGER NOT NULL,
    `created_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `deleted` INTEGET NOT NULL DEFAULT 0
);

-- Properties
CREATE TABLE IF NOT EXISTS properties (
    `name` TEXT PRIMARY KEY,
    `value` TEXT NULL
);

-- Translations
CREATE TABLE IF NOT EXISTS translations (
    `id` INTEGER PRIMARY KEY,
    `idiom` TEXT NOT NULL,
    `name` INTEGER,
    `value` TEXT NOT NULL,
    `deleted` INTEGET NOT NULL DEFAULT 0
);

-- Redirects
CREATE TABLE IF NOT EXISTS redirects (
    `id` INTEGER PRIMARY KEY,
    `from_url` TEXT NOT NULL,
    `from_url_regex` INTEGER NOT NULL DEFAULT 0,
    `to_url` TEXT NOT NULL,
    `deleted` INTEGET NOT NULL DEFAULT 0
);

-- Blocks
CREATE TABLE IF NOT EXISTS blocks (
    `id` INTEGER PRIMARY KEY,
    `id_page` INTEGER NOT NULL,
    `name` TEXT NOT NULL,
    `json` TEXT NOT NULL,
    `order` INTEGER NOT NULL,
    `deleted` INTEGET NOT NULL DEFAULT 0
);
