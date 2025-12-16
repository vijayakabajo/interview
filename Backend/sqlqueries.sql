CREATE TABLE `users` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `full_name` VARCHAR(128),
  `email` VARCHAR(128) NOT NULL UNIQUE,
  `password` VARCHAR(128) NOT NULL,
  `is_active` BOOLEAN DEFAULT false,
  
   PRIMARY KEY (`id`)
  );
   
   CREATE TABLE `todos` (
  `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` BIGINT NOT NULL,
  `title` VARCHAR(64),
  `content` TEXT,
  `is_done` BOOLEAN DEFAULT false,
  
   PRIMARY KEY (`id`)
  );
   
   
   select * from users order by id desc;
   
   select * from todos order by id desc;