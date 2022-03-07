-- Admin user roles table
CREATE TABLE IF NOT EXISTS admin_user_roles (
    `id` INTEGER PRIMARY KEY,
    `name` TEXT NOT NULL,
    `login` TEXT NOT NULL,
    `password` TEXT NOT NULL,
    `created_by` INTEGER NOT NULL,
    `updated_by` INTEGER NULL,
    `created_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `active` INTEGER NOT NULL DEFAULT 1
);

-- Admin user table
CREATE TABLE IF NOT EXISTS admin_users (
    `id` INTEGER PRIMARY KEY,
    `name` TEXT NOT NULL,
    `login` TEXT NOT NULL,
    `password` TEXT NOT NULL,
    `created_by` INTEGER NOT NULL,
    `updated_by` INTEGER NULL,
    `created_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `active` INTEGER NOT NULL DEFAULT 1
);

-- Idioms
CREATE TABLE IF NOT EXISTS idioms (
    `id` TEXT PRIMARY KEY,
    `name` TEXT NOT NULL,
    `active` INTEGER NOT NULL DEFAULT 1,
    `created_by` INTEGER NOT NULL,
    `updated_by` INTEGER NULL,
    `created_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
);

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
    `template` TEXT NOT NULL,
    `html` TEXT NULL,
    `properties` TEXT NULL
);

-- History
CREATE TABLE IF NOT EXISTS history (
    `id` INTEGER PRIMARY KEY,
    `type_resource` TEXT,
    `id_resource` INTEGER,
    `title` TEXT NOT NULL,
    `description` TEXT NOT NULL,
    `created_by` INTEGER NOT NULL,
    `created_on` TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
