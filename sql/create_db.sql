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
    `access` INTEGER NOT NULL DEFAULT 1
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

-------------------------------------------------------------------------------
-- Inserts
-------------------------------------------------------------------------------

-- Insert native user
INSERT INTO users (name, email, password, permission) VALUES ('Admin', 'admin@admin.com', '0410424fb170091dabc47fae4c19173574061b575c35434971e4e3ad4534eabb', 'administrator');

-- Insert initial homepage

-- Insert initial menu

-- Insert default translations
INSERT INTO translations (idiom, name, value) VALUES ('en', 'cookie_policy_title', 'Cookie Policy');
INSERT INTO translations (idiom, name, value) VALUES ('en', 'cookie_policy_content', 'We use cookies to improve user experience, and analyze website traffic. For these reasons, we may share your site usage data with our analytics partners. By clicking "Agree" you consent to store on your device all the technologies used in the application');
INSERT INTO translations (idiom, name, value) VALUES ('en', 'cookie_policy_agree', 'Agree');
INSERT INTO translations (idiom, name, value) VALUES ('en', 'cookie_policy_disagree', 'Disagree');
INSERT INTO translations (idiom, name, value) VALUES ('en', 'cookie_policy_cancel', 'Cancel');
