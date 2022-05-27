-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 27, 2022 at 01:58 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hggc`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add contact', 7, 'add_contact'),
(26, 'Can change contact', 7, 'change_contact'),
(27, 'Can delete contact', 7, 'delete_contact'),
(28, 'Can view contact', 7, 'view_contact'),
(29, 'Can add project', 8, 'add_project'),
(30, 'Can change project', 8, 'change_project'),
(31, 'Can delete project', 8, 'delete_project'),
(32, 'Can view project', 8, 'view_project'),
(33, 'Can add financial', 9, 'add_financial'),
(34, 'Can change financial', 9, 'change_financial'),
(35, 'Can delete financial', 9, 'delete_financial'),
(36, 'Can view financial', 9, 'view_financial'),
(37, 'Can add category', 10, 'add_category'),
(38, 'Can change category', 10, 'change_category'),
(39, 'Can delete category', 10, 'delete_category'),
(40, 'Can view category', 10, 'view_category'),
(41, 'Can add finance category', 11, 'add_financecategory'),
(42, 'Can change finance category', 11, 'change_financecategory'),
(43, 'Can delete finance category', 11, 'delete_financecategory'),
(44, 'Can view finance category', 11, 'view_financecategory'),
(45, 'Can add contact category', 12, 'add_contactcategory'),
(46, 'Can change contact category', 12, 'change_contactcategory'),
(47, 'Can delete contact category', 12, 'delete_contactcategory'),
(48, 'Can view contact category', 12, 'view_contactcategory'),
(49, 'Can add user activities', 13, 'add_useractivities'),
(50, 'Can change user activities', 13, 'change_useractivities'),
(51, 'Can delete user activities', 13, 'delete_useractivities'),
(52, 'Can view user activities', 13, 'view_useractivities'),
(53, 'Can add schedule meeting', 14, 'add_schedulemeeting'),
(54, 'Can change schedule meeting', 14, 'change_schedulemeeting'),
(55, 'Can delete schedule meeting', 14, 'delete_schedulemeeting'),
(56, 'Can view schedule meeting', 14, 'view_schedulemeeting'),
(57, 'Can add minutes', 15, 'add_minutes'),
(58, 'Can change minutes', 15, 'change_minutes'),
(59, 'Can delete minutes', 15, 'delete_minutes'),
(60, 'Can view minutes', 15, 'view_minutes'),
(61, 'Can add newsletter', 16, 'add_newsletter'),
(62, 'Can change newsletter', 16, 'change_newsletter'),
(63, 'Can delete newsletter', 16, 'delete_newsletter'),
(64, 'Can view newsletter', 16, 'view_newsletter'),
(65, 'Can add document category', 17, 'add_documentcategory'),
(66, 'Can change document category', 17, 'change_documentcategory'),
(67, 'Can delete document category', 17, 'delete_documentcategory'),
(68, 'Can view document category', 17, 'view_documentcategory'),
(69, 'Can add dropbox', 18, 'add_dropbox'),
(70, 'Can change dropbox', 18, 'change_dropbox'),
(71, 'Can delete dropbox', 18, 'delete_dropbox'),
(72, 'Can view dropbox', 18, 'view_dropbox'),
(73, 'Can add share file field', 19, 'add_sharefilefield'),
(74, 'Can change share file field', 19, 'change_sharefilefield'),
(75, 'Can delete share file field', 19, 'delete_sharefilefield'),
(76, 'Can view share file field', 19, 'view_sharefilefield'),
(77, 'Can add attachment', 20, 'add_attachment'),
(78, 'Can change attachment', 20, 'change_attachment'),
(79, 'Can delete attachment', 20, 'delete_attachment'),
(80, 'Can view attachment', 20, 'view_attachment');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$320000$e077Lr0jrULjVEf7k1wh0I$AiC8nPzVj6pgASoXsVqFtPNidaQSubIZUTGIft+W7q0=', '2022-05-27 13:58:19.709537', 1, 'admin', '', '', 'dev@qrair.co.za', 1, 1, '2022-05-27 13:57:05.147643');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_category`
--

CREATE TABLE `base_category` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `slug` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_contact`
--

CREATE TABLE `base_contact` (
  `id` int(11) NOT NULL,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `email` varchar(254) NOT NULL,
  `belong_to_id` int(11) DEFAULT NULL,
  `category_id` bigint(20) DEFAULT NULL,
  `code` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_contactcategory`
--

CREATE TABLE `base_contactcategory` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `slug` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_financecategory`
--

CREATE TABLE `base_financecategory` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_financial`
--

CREATE TABLE `base_financial` (
  `id` char(32) NOT NULL,
  `profile_id` bigint(20) DEFAULT NULL,
  `amount` decimal(10,2) NOT NULL,
  `upload_date` date DEFAULT NULL,
  `contact_id` int(11) DEFAULT NULL,
  `entity_id` int(11) DEFAULT NULL,
  `project_id` char(32) DEFAULT NULL,
  `created` datetime(6) DEFAULT NULL,
  `category_id` bigint(20) DEFAULT NULL,
  `reason` longtext DEFAULT NULL,
  `created_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `base_project`
--

CREATE TABLE `base_project` (
  `id` char(32) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `created_by_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(10, 'base', 'category'),
(7, 'base', 'contact'),
(12, 'base', 'contactcategory'),
(11, 'base', 'financecategory'),
(9, 'base', 'financial'),
(8, 'base', 'project'),
(5, 'contenttypes', 'contenttype'),
(20, 'django_summernote', 'attachment'),
(17, 'library', 'documentcategory'),
(18, 'library', 'dropbox'),
(19, 'library', 'sharefilefield'),
(15, 'meetings', 'minutes'),
(14, 'meetings', 'schedulemeeting'),
(16, 'news', 'newsletter'),
(6, 'sessions', 'session'),
(13, 'users', 'useractivities');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-05-27 13:54:36.917734'),
(2, 'auth', '0001_initial', '2022-05-27 13:54:44.310220'),
(3, 'admin', '0001_initial', '2022-05-27 13:54:46.719495'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-05-27 13:54:46.798794'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-05-27 13:54:46.890789'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-05-27 13:54:47.637002'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-05-27 13:54:48.307318'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-05-27 13:54:49.003123'),
(9, 'auth', '0004_alter_user_username_opts', '2022-05-27 13:54:49.219636'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-05-27 13:54:49.773360'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-05-27 13:54:49.841053'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-05-27 13:54:49.920584'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-05-27 13:54:50.120590'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-05-27 13:54:50.348585'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-05-27 13:54:50.549588'),
(16, 'auth', '0011_update_proxy_permissions', '2022-05-27 13:54:50.615587'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-05-27 13:54:50.841582'),
(18, 'base', '0001_initial', '2022-05-27 13:54:55.617683'),
(19, 'base', '0002_alter_entity_options_alter_financial_upload_date', '2022-05-27 13:54:55.806935'),
(20, 'base', '0003_financial_created_alter_financial_project_and_more', '2022-05-27 13:54:58.848734'),
(21, 'base', '0004_alter_financial_options_alter_financial_upload_date_and_more', '2022-05-27 13:55:01.197982'),
(22, 'base', '0005_expenses_created_alter_expenses_captured_date_and_more', '2022-05-27 13:55:04.150669'),
(23, 'base', '0006_category_alter_financial_entity_and_more', '2022-05-27 13:55:04.973774'),
(24, 'base', '0007_alter_financial_profile', '2022-05-27 13:55:07.003551'),
(25, 'base', '0008_financecategory_delete_expenses_financial_category', '2022-05-27 13:55:08.333230'),
(26, 'base', '0009_alter_financial_options_alter_financial_contact_and_more', '2022-05-27 13:55:13.292913'),
(27, 'base', '0010_financial_reason', '2022-05-27 13:55:13.577506'),
(28, 'base', '0011_remove_project_entity_contact_belong_to_and_more', '2022-05-27 13:55:18.550255'),
(29, 'base', '0012_financial_created_by_project_created_by', '2022-05-27 13:55:20.087517'),
(30, 'base', '0013_contactcategory_contact_category', '2022-05-27 13:55:21.597315'),
(31, 'base', '0014_alter_contactcategory_options_alter_contact_id', '2022-05-27 13:55:25.823716'),
(32, 'base', '0015_alter_contact_id', '2022-05-27 13:55:28.474697'),
(33, 'base', '0016_contact_code_alter_contact_id', '2022-05-27 13:55:31.833255'),
(34, 'base', '0017_alter_contact_code', '2022-05-27 13:55:32.931296'),
(35, 'django_summernote', '0001_initial', '2022-05-27 13:55:33.459819'),
(36, 'django_summernote', '0002_update-help_text', '2022-05-27 13:55:33.513437'),
(37, 'django_summernote', '0003_alter_attachment_id', '2022-05-27 13:55:34.037712'),
(38, 'library', '0001_initial', '2022-05-27 13:55:37.747922'),
(39, 'library', '0002_remove_dropbox_category_dropbox_group', '2022-05-27 13:55:39.353132'),
(40, 'library', '0003_alter_dropbox_group', '2022-05-27 13:55:41.722495'),
(41, 'library', '0004_dropbox_category_alter_dropbox_group', '2022-05-27 13:55:44.803040'),
(42, 'meetings', '0001_initial', '2022-05-27 13:55:47.023071'),
(43, 'meetings', '0002_schedulemeeting_group', '2022-05-27 13:55:47.650623'),
(44, 'news', '0001_initial', '2022-05-27 13:55:47.967039'),
(45, 'news', '0002_newsletter_attachement', '2022-05-27 13:55:48.395527'),
(46, 'news', '0003_newsletter_group', '2022-05-27 13:55:49.418139'),
(47, 'sessions', '0001_initial', '2022-05-27 13:55:49.769309'),
(48, 'users', '0001_initial', '2022-05-27 13:55:51.610450');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('yh7v7stydt4kk1cpfsc32so6x79o6fou', '.eJxVjEEOwiAQRe_C2hBKARmX7j0DGWaoVA0kpV0Z726bdNFu_3vvf0XAZc5haWkKI4ub6MTluEWkdyob4BeWZ5VUyzyNUW6K3GmTj8rpc9_d00HGltdaazA9MTgiTioy4eBAgfLR63gF8q6z1veA7MHwgHqViZQ1SVsyyonfH--FOA0:1nuYbj:1kme-V66GVw0Pul9P8LBb40-oYyjZmnYiW2vyZpuaas', '2022-06-10 13:58:19.990914');

-- --------------------------------------------------------

--
-- Table structure for table `django_summernote_attachment`
--

CREATE TABLE `django_summernote_attachment` (
  `id` bigint(20) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `file` varchar(100) NOT NULL,
  `uploaded` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `library_documentcategory`
--

CREATE TABLE `library_documentcategory` (
  `id` bigint(20) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `slug` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `library_dropbox`
--

CREATE TABLE `library_dropbox` (
  `id` bigint(20) NOT NULL,
  `title` varchar(200) NOT NULL,
  `desc` longtext DEFAULT NULL,
  `created` datetime(6) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `category_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `library_sharefilefield`
--

CREATE TABLE `library_sharefilefield` (
  `id` bigint(20) NOT NULL,
  `file_field` varchar(100) DEFAULT NULL,
  `meeting_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `meetings_minutes`
--

CREATE TABLE `meetings_minutes` (
  `id` bigint(20) NOT NULL,
  `duration` varchar(10) NOT NULL,
  `contents` longtext DEFAULT NULL,
  `recording` varchar(100) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `meeting_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `meetings_schedulemeeting`
--

CREATE TABLE `meetings_schedulemeeting` (
  `id` bigint(20) NOT NULL,
  `agenda` varchar(200) NOT NULL,
  `estimated_period` varchar(10) NOT NULL,
  `start_time` datetime(6) DEFAULT NULL,
  `end_time` datetime(6) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `description` longtext DEFAULT NULL,
  `updated` datetime(6) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `group_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `news_newsletter`
--

CREATE TABLE `news_newsletter` (
  `id` bigint(20) NOT NULL,
  `subject` varchar(150) NOT NULL,
  `contents` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `attachement` varchar(100) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users_useractivities`
--

CREATE TABLE `users_useractivities` (
  `id` bigint(20) NOT NULL,
  `message` longtext NOT NULL,
  `created` datetime(6) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_useractivities`
--

INSERT INTO `users_useractivities` (`id`, `message`, `created`, `user_id`) VALUES
(1, ' logged in', '2022-05-27 13:58:19.787575', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `base_category`
--
ALTER TABLE `base_category`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_category_slug_6efb48c2` (`slug`);

--
-- Indexes for table `base_contact`
--
ALTER TABLE `base_contact`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_contact_belong_to_id_9bf28817_fk_auth_group_id` (`belong_to_id`),
  ADD KEY `base_contact_category_id_fc3732ec_fk_base_contactcategory_id` (`category_id`);

--
-- Indexes for table `base_contactcategory`
--
ALTER TABLE `base_contactcategory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_contactcategory_slug_56f5d7a8` (`slug`);

--
-- Indexes for table `base_financecategory`
--
ALTER TABLE `base_financecategory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_financecategory_slug_9f7301d3` (`slug`);

--
-- Indexes for table `base_financial`
--
ALTER TABLE `base_financial`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_financial_project_id_cc6e111f_fk_base_project_id` (`project_id`),
  ADD KEY `base_financial_profile_id_a7795668` (`profile_id`),
  ADD KEY `base_financial_category_id_bff6f7b3_fk_base_financecategory_id` (`category_id`),
  ADD KEY `base_financial_entity_id_9b395307_fk_auth_group_id` (`entity_id`),
  ADD KEY `base_financial_created_by_id_befe2519_fk_auth_user_id` (`created_by_id`),
  ADD KEY `base_financial_contact_id_f08ed026_fk` (`contact_id`);

--
-- Indexes for table `base_project`
--
ALTER TABLE `base_project`
  ADD PRIMARY KEY (`id`),
  ADD KEY `base_project_group_id_ce82060f_fk_auth_group_id` (`group_id`),
  ADD KEY `base_project_created_by_id_4f7655f7_fk_auth_user_id` (`created_by_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `django_summernote_attachment`
--
ALTER TABLE `django_summernote_attachment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `library_documentcategory`
--
ALTER TABLE `library_documentcategory`
  ADD PRIMARY KEY (`id`),
  ADD KEY `library_documentcategory_slug_96851295` (`slug`);

--
-- Indexes for table `library_dropbox`
--
ALTER TABLE `library_dropbox`
  ADD PRIMARY KEY (`id`),
  ADD KEY `library_dropbox_user_id_fc8e24c4_fk_auth_user_id` (`user_id`),
  ADD KEY `library_dropbox_category_id_f1e53d04_fk_library_d` (`category_id`),
  ADD KEY `library_dropbox_group_id_e8844e9a_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `library_sharefilefield`
--
ALTER TABLE `library_sharefilefield`
  ADD PRIMARY KEY (`id`),
  ADD KEY `library_sharefilefield_meeting_id_ab739eb6_fk_library_dropbox_id` (`meeting_id`);

--
-- Indexes for table `meetings_minutes`
--
ALTER TABLE `meetings_minutes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `meetings_minutes_meeting_id_09b7a17e_fk_meetings_` (`meeting_id`);

--
-- Indexes for table `meetings_schedulemeeting`
--
ALTER TABLE `meetings_schedulemeeting`
  ADD PRIMARY KEY (`id`),
  ADD KEY `meetings_schedulemeeting_owner_id_8d7dcd36_fk_auth_user_id` (`owner_id`),
  ADD KEY `meetings_schedulemeeting_group_id_b033db2d_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `news_newsletter`
--
ALTER TABLE `news_newsletter`
  ADD PRIMARY KEY (`id`),
  ADD KEY `news_newsletter_group_id_b11c55c5_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `users_useractivities`
--
ALTER TABLE `users_useractivities`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_useractivities_user_id_4d660ac3_fk_auth_user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_category`
--
ALTER TABLE `base_category`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_contact`
--
ALTER TABLE `base_contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_contactcategory`
--
ALTER TABLE `base_contactcategory`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `base_financecategory`
--
ALTER TABLE `base_financecategory`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `django_summernote_attachment`
--
ALTER TABLE `django_summernote_attachment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `library_documentcategory`
--
ALTER TABLE `library_documentcategory`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `library_dropbox`
--
ALTER TABLE `library_dropbox`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `library_sharefilefield`
--
ALTER TABLE `library_sharefilefield`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `meetings_minutes`
--
ALTER TABLE `meetings_minutes`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `meetings_schedulemeeting`
--
ALTER TABLE `meetings_schedulemeeting`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `news_newsletter`
--
ALTER TABLE `news_newsletter`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_useractivities`
--
ALTER TABLE `users_useractivities`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `base_contact`
--
ALTER TABLE `base_contact`
  ADD CONSTRAINT `base_contact_belong_to_id_9bf28817_fk_auth_group_id` FOREIGN KEY (`belong_to_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `base_contact_category_id_fc3732ec_fk_base_contactcategory_id` FOREIGN KEY (`category_id`) REFERENCES `base_contactcategory` (`id`);

--
-- Constraints for table `base_financial`
--
ALTER TABLE `base_financial`
  ADD CONSTRAINT `base_financial_category_id_bff6f7b3_fk_base_financecategory_id` FOREIGN KEY (`category_id`) REFERENCES `base_financecategory` (`id`),
  ADD CONSTRAINT `base_financial_contact_id_f08ed026_fk` FOREIGN KEY (`contact_id`) REFERENCES `base_contact` (`id`),
  ADD CONSTRAINT `base_financial_created_by_id_befe2519_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `base_financial_entity_id_9b395307_fk_auth_group_id` FOREIGN KEY (`entity_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `base_financial_profile_id_a7795668_fk_base_category_id` FOREIGN KEY (`profile_id`) REFERENCES `base_category` (`id`),
  ADD CONSTRAINT `base_financial_project_id_cc6e111f_fk_base_project_id` FOREIGN KEY (`project_id`) REFERENCES `base_project` (`id`);

--
-- Constraints for table `base_project`
--
ALTER TABLE `base_project`
  ADD CONSTRAINT `base_project_created_by_id_4f7655f7_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `base_project_group_id_ce82060f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `library_dropbox`
--
ALTER TABLE `library_dropbox`
  ADD CONSTRAINT `library_dropbox_category_id_f1e53d04_fk_library_d` FOREIGN KEY (`category_id`) REFERENCES `library_documentcategory` (`id`),
  ADD CONSTRAINT `library_dropbox_group_id_e8844e9a_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `library_dropbox_user_id_fc8e24c4_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `library_sharefilefield`
--
ALTER TABLE `library_sharefilefield`
  ADD CONSTRAINT `library_sharefilefield_meeting_id_ab739eb6_fk_library_dropbox_id` FOREIGN KEY (`meeting_id`) REFERENCES `library_dropbox` (`id`);

--
-- Constraints for table `meetings_minutes`
--
ALTER TABLE `meetings_minutes`
  ADD CONSTRAINT `meetings_minutes_meeting_id_09b7a17e_fk_meetings_` FOREIGN KEY (`meeting_id`) REFERENCES `meetings_schedulemeeting` (`id`);

--
-- Constraints for table `meetings_schedulemeeting`
--
ALTER TABLE `meetings_schedulemeeting`
  ADD CONSTRAINT `meetings_schedulemeeting_group_id_b033db2d_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `meetings_schedulemeeting_owner_id_8d7dcd36_fk_auth_user_id` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `news_newsletter`
--
ALTER TABLE `news_newsletter`
  ADD CONSTRAINT `news_newsletter_group_id_b11c55c5_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `users_useractivities`
--
ALTER TABLE `users_useractivities`
  ADD CONSTRAINT `users_useractivities_user_id_4d660ac3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
