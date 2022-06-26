-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-06-2022 a las 08:28:13
-- Versión del servidor: 10.4.19-MariaDB
-- Versión de PHP: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `escuela_db`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `auth_permission`
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
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add alumno', 6, 'add_alumno'),
(22, 'Can change alumno', 6, 'change_alumno'),
(23, 'Can delete alumno', 6, 'delete_alumno'),
(24, 'Can view alumno', 6, 'view_alumno'),
(25, 'Can add aula', 7, 'add_aula'),
(26, 'Can change aula', 7, 'change_aula'),
(27, 'Can delete aula', 7, 'delete_aula'),
(28, 'Can view aula', 7, 'view_aula'),
(29, 'Can add materia', 8, 'add_materia'),
(30, 'Can change materia', 8, 'change_materia'),
(31, 'Can delete materia', 8, 'delete_materia'),
(32, 'Can view materia', 8, 'view_materia'),
(33, 'Can add preceptor', 9, 'add_preceptor'),
(34, 'Can change preceptor', 9, 'change_preceptor'),
(35, 'Can delete preceptor', 9, 'delete_preceptor'),
(36, 'Can view preceptor', 9, 'view_preceptor'),
(37, 'Can add profesor', 10, 'add_profesor'),
(38, 'Can change profesor', 10, 'change_profesor'),
(39, 'Can delete profesor', 10, 'delete_profesor'),
(40, 'Can view profesor', 10, 'view_profesor'),
(41, 'Can add turno', 11, 'add_turno'),
(42, 'Can change turno', 11, 'change_turno'),
(43, 'Can delete turno', 11, 'delete_turno'),
(44, 'Can view turno', 11, 'view_turno'),
(45, 'Can add tiene', 12, 'add_tiene'),
(46, 'Can change tiene', 12, 'change_tiene'),
(47, 'Can delete tiene', 12, 'delete_tiene'),
(48, 'Can view tiene', 12, 'view_tiene'),
(49, 'Can add rinde', 13, 'add_rinde'),
(50, 'Can change rinde', 13, 'change_rinde'),
(51, 'Can delete rinde', 13, 'delete_rinde'),
(52, 'Can view rinde', 13, 'view_rinde'),
(53, 'Can add dicta', 14, 'add_dicta'),
(54, 'Can change dicta', 14, 'change_dicta'),
(55, 'Can delete dicta', 14, 'delete_dicta'),
(56, 'Can view dicta', 14, 'view_dicta'),
(57, 'Can add curso', 15, 'add_curso'),
(58, 'Can change curso', 15, 'change_curso'),
(59, 'Can delete curso', 15, 'delete_curso'),
(60, 'Can view curso', 15, 'view_curso'),
(61, 'Can add tipo usuario', 16, 'add_tipousuario'),
(62, 'Can change tipo usuario', 16, 'change_tipousuario'),
(63, 'Can delete tipo usuario', 16, 'delete_tipousuario'),
(64, 'Can view tipo usuario', 16, 'view_tipousuario'),
(65, 'Can add user', 17, 'add_user'),
(66, 'Can change user', 17, 'change_user'),
(67, 'Can delete user', 17, 'delete_user'),
(68, 'Can view user', 17, 'view_user');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_spanish_ci DEFAULT NULL,
  `object_repr` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext COLLATE utf8_spanish_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(6, 'escuela', 'alumno'),
(7, 'escuela', 'aula'),
(15, 'escuela', 'curso'),
(14, 'escuela', 'dicta'),
(8, 'escuela', 'materia'),
(9, 'escuela', 'preceptor'),
(10, 'escuela', 'profesor'),
(13, 'escuela', 'rinde'),
(12, 'escuela', 'tiene'),
(11, 'escuela', 'turno'),
(5, 'sessions', 'session'),
(16, 'user', 'tipousuario'),
(17, 'user', 'user');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-06-26 06:27:34.407235'),
(2, 'contenttypes', '0002_remove_content_type_name', '2022-06-26 06:27:35.090816'),
(3, 'auth', '0001_initial', '2022-06-26 06:27:38.210315'),
(4, 'auth', '0002_alter_permission_name_max_length', '2022-06-26 06:27:39.285681'),
(5, 'auth', '0003_alter_user_email_max_length', '2022-06-26 06:27:39.346927'),
(6, 'auth', '0004_alter_user_username_opts', '2022-06-26 06:27:39.369963'),
(7, 'auth', '0005_alter_user_last_login_null', '2022-06-26 06:27:39.396002'),
(8, 'auth', '0006_require_contenttypes_0002', '2022-06-26 06:27:39.417330'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2022-06-26 06:27:39.446565'),
(10, 'auth', '0008_alter_user_username_max_length', '2022-06-26 06:27:39.469850'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2022-06-26 06:27:39.521175'),
(12, 'auth', '0010_alter_group_name_max_length', '2022-06-26 06:27:40.369016'),
(13, 'auth', '0011_update_proxy_permissions', '2022-06-26 06:27:40.413594'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2022-06-26 06:27:40.454553'),
(15, 'user', '0001_initial', '2022-06-26 06:27:45.669652'),
(16, 'admin', '0001_initial', '2022-06-26 06:27:47.244826'),
(17, 'admin', '0002_logentry_remove_auto_add', '2022-06-26 06:27:47.274153'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2022-06-26 06:27:47.324253'),
(19, 'escuela', '0001_initial', '2022-06-26 06:27:59.013229'),
(20, 'escuela', '0002_initial', '2022-06-26 06:27:59.950722'),
(21, 'escuela', '0003_alter_alumno_usuario', '2022-06-26 06:28:01.953427'),
(22, 'sessions', '0001_initial', '2022-06-26 06:28:02.790250');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_spanish_ci NOT NULL,
  `session_data` longtext COLLATE utf8_spanish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escuela_alumno`
--

CREATE TABLE `escuela_alumno` (
  `num_reg` int(11) NOT NULL,
  `num_doc` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(90) COLLATE utf8_spanish_ci NOT NULL,
  `apellido` varchar(90) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_nac` date NOT NULL,
  `edad` int(11) DEFAULT NULL,
  `direccion` varchar(120) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(14) COLLATE utf8_spanish_ci NOT NULL,
  `aula_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escuela_aula`
--

CREATE TABLE `escuela_aula` (
  `idAula` int(11) NOT NULL,
  `año` int(11) NOT NULL,
  `division` int(11) NOT NULL,
  `preceptor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escuela_curso`
--

CREATE TABLE `escuela_curso` (
  `id` int(11) NOT NULL,
  `dia_clase` int(11) NOT NULL,
  `aula_idAula_id` int(11) NOT NULL,
  `materia_codigo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escuela_dicta`
--

CREATE TABLE `escuela_dicta` (
  `id` int(11) NOT NULL,
  `cargo` varchar(85) COLLATE utf8_spanish_ci NOT NULL,
  `materia_codigo_id` int(11) NOT NULL,
  `profesor_id_profesor_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escuela_materia`
--

CREATE TABLE `escuela_materia` (
  `codigo` int(11) NOT NULL,
  `nombre` varchar(90) COLLATE utf8_spanish_ci NOT NULL,
  `cant_horas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escuela_preceptor`
--

CREATE TABLE `escuela_preceptor` (
  `idPreceptor` int(11) NOT NULL,
  `num_cuil` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `num_doc` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(90) COLLATE utf8_spanish_ci NOT NULL,
  `apellido` varchar(90) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_nac` date NOT NULL,
  `edad` int(11) DEFAULT NULL,
  `direccion` varchar(120) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(14) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escuela_profesor`
--

CREATE TABLE `escuela_profesor` (
  `idProfesor` int(11) NOT NULL,
  `num_cuil` varchar(15) COLLATE utf8_spanish_ci NOT NULL,
  `num_doc` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(90) COLLATE utf8_spanish_ci NOT NULL,
  `apellido` varchar(90) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_nac` date NOT NULL,
  `edad` int(11) DEFAULT NULL,
  `direccion` varchar(120) COLLATE utf8_spanish_ci NOT NULL,
  `telefono` varchar(14) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escuela_rinde`
--

CREATE TABLE `escuela_rinde` (
  `id` int(11) NOT NULL,
  `nota_1` int(11) NOT NULL,
  `nota_2` int(11) NOT NULL,
  `nota_3` int(11) NOT NULL,
  `alumno_nro_registro_id` int(11) NOT NULL,
  `materia_codigo_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escuela_tiene`
--

CREATE TABLE `escuela_tiene` (
  `id` int(11) NOT NULL,
  `hora_ingreso` varchar(45) COLLATE utf8_spanish_ci NOT NULL,
  `hora_egreso` varchar(45) COLLATE utf8_spanish_ci NOT NULL,
  `aula_idAula_id` int(11) NOT NULL,
  `turno_idturno_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `escuela_turno`
--

CREATE TABLE `escuela_turno` (
  `idTurno` int(11) NOT NULL,
  `nombre` varchar(45) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_tipousuario`
--

CREATE TABLE `user_tipousuario` (
  `nombre` varchar(100) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_user`
--

CREATE TABLE `user_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8_spanish_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_spanish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `tipo_id` varchar(100) COLLATE utf8_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_user_groups`
--

CREATE TABLE `user_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_user_user_permissions`
--

CREATE TABLE `user_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_user_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `escuela_alumno`
--
ALTER TABLE `escuela_alumno`
  ADD PRIMARY KEY (`num_reg`),
  ADD UNIQUE KEY `num_doc` (`num_doc`),
  ADD UNIQUE KEY `escuela_alumno_usuario_id_766701c3_uniq` (`usuario_id`),
  ADD KEY `escuela_alumno_aula_id_2c8081b7_fk_escuela_aula_idAula` (`aula_id`);

--
-- Indices de la tabla `escuela_aula`
--
ALTER TABLE `escuela_aula`
  ADD PRIMARY KEY (`idAula`),
  ADD KEY `escuela_aula_preceptor_id_acaef7a9_fk_escuela_p` (`preceptor_id`);

--
-- Indices de la tabla `escuela_curso`
--
ALTER TABLE `escuela_curso`
  ADD PRIMARY KEY (`id`),
  ADD KEY `escuela_curso_aula_idAula_id_8b271c21_fk_escuela_aula_idAula` (`aula_idAula_id`),
  ADD KEY `escuela_curso_materia_codigo_id_787ad940_fk_escuela_m` (`materia_codigo_id`);

--
-- Indices de la tabla `escuela_dicta`
--
ALTER TABLE `escuela_dicta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `escuela_dicta_materia_codigo_id_065709a0_fk_escuela_m` (`materia_codigo_id`),
  ADD KEY `escuela_dicta_profesor_id_profesor_76032437_fk_escuela_p` (`profesor_id_profesor_id`);

--
-- Indices de la tabla `escuela_materia`
--
ALTER TABLE `escuela_materia`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `escuela_preceptor`
--
ALTER TABLE `escuela_preceptor`
  ADD PRIMARY KEY (`idPreceptor`),
  ADD UNIQUE KEY `num_cuil` (`num_cuil`),
  ADD UNIQUE KEY `num_doc` (`num_doc`);

--
-- Indices de la tabla `escuela_profesor`
--
ALTER TABLE `escuela_profesor`
  ADD PRIMARY KEY (`idProfesor`),
  ADD UNIQUE KEY `num_cuil` (`num_cuil`),
  ADD UNIQUE KEY `num_doc` (`num_doc`);

--
-- Indices de la tabla `escuela_rinde`
--
ALTER TABLE `escuela_rinde`
  ADD PRIMARY KEY (`id`),
  ADD KEY `escuela_rinde_alumno_nro_registro__e741dc4c_fk_escuela_a` (`alumno_nro_registro_id`),
  ADD KEY `escuela_rinde_materia_codigo_id_ac704b7e_fk_escuela_m` (`materia_codigo_id`);

--
-- Indices de la tabla `escuela_tiene`
--
ALTER TABLE `escuela_tiene`
  ADD PRIMARY KEY (`id`),
  ADD KEY `escuela_tiene_aula_idAula_id_492db536_fk_escuela_aula_idAula` (`aula_idAula_id`),
  ADD KEY `escuela_tiene_turno_idturno_id_faa69e53_fk_escuela_turno_idTurno` (`turno_idturno_id`);

--
-- Indices de la tabla `escuela_turno`
--
ALTER TABLE `escuela_turno`
  ADD PRIMARY KEY (`idTurno`);

--
-- Indices de la tabla `user_tipousuario`
--
ALTER TABLE `user_tipousuario`
  ADD PRIMARY KEY (`nombre`);

--
-- Indices de la tabla `user_user`
--
ALTER TABLE `user_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `user_user_tipo_id_4962648f_fk_user_tipousuario_nombre` (`tipo_id`);

--
-- Indices de la tabla `user_user_groups`
--
ALTER TABLE `user_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_user_groups_user_id_group_id_bb60391f_uniq` (`user_id`,`group_id`),
  ADD KEY `user_user_groups_group_id_c57f13c0_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `user_user_user_permissions`
--
ALTER TABLE `user_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq` (`user_id`,`permission_id`),
  ADD KEY `user_user_user_permi_permission_id_ce49d4de_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `escuela_aula`
--
ALTER TABLE `escuela_aula`
  MODIFY `idAula` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `escuela_curso`
--
ALTER TABLE `escuela_curso`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `escuela_dicta`
--
ALTER TABLE `escuela_dicta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `escuela_preceptor`
--
ALTER TABLE `escuela_preceptor`
  MODIFY `idPreceptor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `escuela_profesor`
--
ALTER TABLE `escuela_profesor`
  MODIFY `idProfesor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `escuela_rinde`
--
ALTER TABLE `escuela_rinde`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `escuela_tiene`
--
ALTER TABLE `escuela_tiene`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `escuela_turno`
--
ALTER TABLE `escuela_turno`
  MODIFY `idTurno` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user_user`
--
ALTER TABLE `user_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user_user_groups`
--
ALTER TABLE `user_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user_user_user_permissions`
--
ALTER TABLE `user_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `escuela_alumno`
--
ALTER TABLE `escuela_alumno`
  ADD CONSTRAINT `escuela_alumno_aula_id_2c8081b7_fk_escuela_aula_idAula` FOREIGN KEY (`aula_id`) REFERENCES `escuela_aula` (`idAula`),
  ADD CONSTRAINT `escuela_alumno_usuario_id_766701c3_fk_user_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `escuela_aula`
--
ALTER TABLE `escuela_aula`
  ADD CONSTRAINT `escuela_aula_preceptor_id_acaef7a9_fk_escuela_p` FOREIGN KEY (`preceptor_id`) REFERENCES `escuela_preceptor` (`idPreceptor`);

--
-- Filtros para la tabla `escuela_curso`
--
ALTER TABLE `escuela_curso`
  ADD CONSTRAINT `escuela_curso_aula_idAula_id_8b271c21_fk_escuela_aula_idAula` FOREIGN KEY (`aula_idAula_id`) REFERENCES `escuela_aula` (`idAula`),
  ADD CONSTRAINT `escuela_curso_materia_codigo_id_787ad940_fk_escuela_m` FOREIGN KEY (`materia_codigo_id`) REFERENCES `escuela_materia` (`codigo`);

--
-- Filtros para la tabla `escuela_dicta`
--
ALTER TABLE `escuela_dicta`
  ADD CONSTRAINT `escuela_dicta_materia_codigo_id_065709a0_fk_escuela_m` FOREIGN KEY (`materia_codigo_id`) REFERENCES `escuela_materia` (`codigo`),
  ADD CONSTRAINT `escuela_dicta_profesor_id_profesor_76032437_fk_escuela_p` FOREIGN KEY (`profesor_id_profesor_id`) REFERENCES `escuela_profesor` (`idProfesor`);

--
-- Filtros para la tabla `escuela_rinde`
--
ALTER TABLE `escuela_rinde`
  ADD CONSTRAINT `escuela_rinde_alumno_nro_registro__e741dc4c_fk_escuela_a` FOREIGN KEY (`alumno_nro_registro_id`) REFERENCES `escuela_alumno` (`num_reg`),
  ADD CONSTRAINT `escuela_rinde_materia_codigo_id_ac704b7e_fk_escuela_m` FOREIGN KEY (`materia_codigo_id`) REFERENCES `escuela_materia` (`codigo`);

--
-- Filtros para la tabla `escuela_tiene`
--
ALTER TABLE `escuela_tiene`
  ADD CONSTRAINT `escuela_tiene_aula_idAula_id_492db536_fk_escuela_aula_idAula` FOREIGN KEY (`aula_idAula_id`) REFERENCES `escuela_aula` (`idAula`),
  ADD CONSTRAINT `escuela_tiene_turno_idturno_id_faa69e53_fk_escuela_turno_idTurno` FOREIGN KEY (`turno_idturno_id`) REFERENCES `escuela_turno` (`idTurno`);

--
-- Filtros para la tabla `user_user`
--
ALTER TABLE `user_user`
  ADD CONSTRAINT `user_user_tipo_id_4962648f_fk_user_tipousuario_nombre` FOREIGN KEY (`tipo_id`) REFERENCES `user_tipousuario` (`nombre`);

--
-- Filtros para la tabla `user_user_groups`
--
ALTER TABLE `user_user_groups`
  ADD CONSTRAINT `user_user_groups_group_id_c57f13c0_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_user_groups_user_id_13f9a20d_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);

--
-- Filtros para la tabla `user_user_user_permissions`
--
ALTER TABLE `user_user_user_permissions`
  ADD CONSTRAINT `user_user_user_permi_permission_id_ce49d4de_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_user_user_permissions_user_id_31782f58_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `user_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
