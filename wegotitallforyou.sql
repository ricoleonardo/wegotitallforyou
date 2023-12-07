CREATE TABLE `sales_reps` (
  `id` integer PRIMARY KEY,
  `name` varchar(255)
);

CREATE TABLE `customers` (
  `id` integer PRIMARY KEY,
  `name` varchar(255)
);

CREATE TABLE `invoices` (
  `id` integer PRIMARY KEY,
  `sales_reps` [id],
  `customers` [id],
  `producs` [id]
);

CREATE TABLE `producs` (
  `id` integer PRIMARY KEY,
  `name` varchar(255),
  `vendors` [id],
  `description` text
);

CREATE TABLE `vendors` (
  `id` integer PRIMARY KEY,
  `name` varchar(255)
);

ALTER TABLE `vendors` ADD FOREIGN KEY (`id`) REFERENCES `producs` (`vendors`);

ALTER TABLE `invoices` ADD FOREIGN KEY (`producs`) REFERENCES `producs` (`id`);

ALTER TABLE `invoices` ADD FOREIGN KEY (`customers`) REFERENCES `customers` (`id`);

ALTER TABLE `invoices` ADD FOREIGN KEY (`sales_reps`) REFERENCES `sales_reps` (`id`);
