-- Admin user table
CREATE TABLE IF NOT EXISTS users (
    `id` INTEGER PRIMARY KEY,
    `name` TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `password` TEXT NOT NULL,
    `permission` TEXT NOT NULL,
    `created_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `last_login` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `active` INTEGER NOT NULL DEFAULT 1,
    `deleted` INTEGET NOT NULL DEFAULT 0
);

-- Insert default admin users
INSERT INTO users (name, email, password, permission) VALUES ('Admin', 'admin@admin.com', 'admin', 'administrator');

-- Pages
CREATE TABLE IF NOT EXISTS pages (
    `id` INTEGER PRIMARY KEY,
    `idiom` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `layout` TEXT NOT NULL,
    `template` TEXT NOT NULL,
    `active` INTEGER NOT NULL DEFAULT 1,
    `created_by` INTEGER NOT NULL,
    `updated_by` INTEGER NULL,
    `created_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `title` TEXT NOT NULL,
    `author` TEXT NULL,
    `description` TEXT NULL,
    `keywords` TEXT NULL,
    `canonical_urls` TEXT NULL,
    `sitemap_active` INTEGER NOT NULL DEFAULT 1,
    `sitemap_priority` TEXT NULL DEFAULT '0.5',
    `sitemap_change_frequently` TEXT NULL DEFAULT 'always',
    `html` TEXT NULL,
    `properties` TEXT NULL,
    `json` TEXT NULL,
    `deleted` INTEGET NOT NULL DEFAULT 0
);

-- History
CREATE TABLE IF NOT EXISTS history (
    `id` INTEGER PRIMARY KEY,
    `type_resource` TEXT,
    `id_resource` INTEGER,
    `title` TEXT NOT NULL,
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
