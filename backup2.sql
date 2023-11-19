--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO django;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO django;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO django;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO django;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO django;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.auth_user_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.auth_user ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO django;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO django;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO django;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO django;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO django;

--
-- Name: studentform_career; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.studentform_career (
    "idCareer" integer NOT NULL,
    code_name character varying(5) NOT NULL,
    name character varying(100) NOT NULL,
    needed_credits smallint NOT NULL,
    semesters smallint NOT NULL,
    CONSTRAINT studentform_career_needed_credits_check CHECK ((needed_credits >= 0)),
    CONSTRAINT studentform_career_semesters_check CHECK ((semesters >= 0))
);


ALTER TABLE public.studentform_career OWNER TO django;

--
-- Name: studentform_career_idCareer_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.studentform_career ALTER COLUMN "idCareer" ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public."studentform_career_idCareer_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: studentform_contact; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.studentform_contact (
    "idContact" bigint NOT NULL,
    phone character varying(25) NOT NULL,
    email character varying(254) NOT NULL,
    udg_email character varying(254) NOT NULL,
    emergency_phone character varying(25) NOT NULL,
    url_socialnet character varying(200),
    "idStudent_id" bigint NOT NULL,
    company character varying(50),
    "position" character varying(50)
);


ALTER TABLE public.studentform_contact OWNER TO django;

--
-- Name: studentform_contact_contact_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.studentform_contact ALTER COLUMN "idContact" ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.studentform_contact_contact_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: studentform_school_cycle; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.studentform_school_cycle (
    "idCycle" integer NOT NULL,
    cycle_period character varying(1) NOT NULL,
    end_date date NOT NULL,
    start_date date NOT NULL,
    year character varying(5) NOT NULL
);


ALTER TABLE public.studentform_school_cycle OWNER TO django;

--
-- Name: studentform_school_cycle_cycle_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.studentform_school_cycle ALTER COLUMN "idCycle" ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.studentform_school_cycle_cycle_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: studentform_status; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.studentform_status (
    "idStatus" integer NOT NULL,
    code_name character varying(3) NOT NULL,
    status character varying(40) NOT NULL
);


ALTER TABLE public.studentform_status OWNER TO django;

--
-- Name: studentform_status_idStatus_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.studentform_status ALTER COLUMN "idStatus" ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public."studentform_status_idStatus_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: studentform_student; Type: TABLE; Schema: public; Owner: django
--

CREATE TABLE public.studentform_student (
    "idStudent" bigint NOT NULL,
    code character varying(9) NOT NULL,
    name character varying(50) NOT NULL,
    status_id integer NOT NULL,
    admission_cycle_id integer NOT NULL,
    first_last_name character varying(30) NOT NULL,
    last_cycle_id integer NOT NULL,
    second_last_name character varying(30) NOT NULL,
    "idCareer_id" integer NOT NULL
);


ALTER TABLE public.studentform_student OWNER TO django;

--
-- Name: studentform_student_student_id_seq; Type: SEQUENCE; Schema: public; Owner: django
--

ALTER TABLE public.studentform_student ALTER COLUMN "idStudent" ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.studentform_student_student_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add school_ cycle	7	add_school_cycle
26	Can change school_ cycle	7	change_school_cycle
27	Can delete school_ cycle	7	delete_school_cycle
28	Can view school_ cycle	7	view_school_cycle
29	Can add student	8	add_student
30	Can change student	8	change_student
31	Can delete student	8	delete_student
32	Can view student	8	view_student
33	Can add contact	9	add_contact
34	Can change contact	9	change_contact
35	Can delete contact	9	delete_contact
36	Can view contact	9	view_contact
37	Can add career	10	add_career
38	Can change career	10	change_career
39	Can delete career	10	delete_career
40	Can view career	10	view_career
41	Can add status	11	add_status
42	Can change status	11	change_status
43	Can delete status	11	delete_status
44	Can view status	11	view_status
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$600000$jEO903YbYYy2DSrCR2fdXx$sOWEPqglPJeC6u1wTerd8OW5Wttwgjp/jTzPtJijdow=	2023-10-31 16:47:38.7373+01	t	admin			admin@test.com	t	t	2023-10-31 16:47:29.434989+01
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2023-10-31 16:48:13.952385+01	1	2023A	1	[{"added": {}}]	7	1
2	2023-10-31 16:48:14.107571+01	2	2023A	1	[{"added": {}}]	7	1
3	2023-10-31 16:48:39.002774+01	1	2023B	2	[{"changed": {"fields": ["Cycle period", "Start date", "End date"]}}]	7	1
4	2023-11-01 14:31:19.941205+01	1	INCO	1	[{"added": {}}]	10	1
5	2023-11-01 14:44:00.568614+01	1	AC	1	[{"added": {}}]	11	1
6	2023-11-01 14:44:09.368064+01	2	IN	1	[{"added": {}}]	11	1
7	2023-11-01 14:44:38.59351+01	3	GD	1	[{"added": {}}]	11	1
8	2023-11-01 14:45:05.604032+01	4	TT	1	[{"added": {}}]	11	1
9	2023-11-01 14:45:51.028929+01	5	BC	1	[{"added": {}}]	11	1
10	2023-11-01 14:46:32.576239+01	6	B4	1	[{"added": {}}]	11	1
11	2023-11-01 14:46:42.270229+01	7	B5	1	[{"added": {}}]	11	1
12	2023-11-01 14:51:32.205805+01	1	Manuel Gerardo	1	[{"added": {}}]	8	1
13	2023-11-01 15:23:50.099903+01	2	Hernandez	1	[{"added": {}}]	8	1
14	2023-11-06 16:30:03.8523+01	3	Israel Huerta	1	[{"added": {}}]	8	1
15	2023-11-07 13:54:45.577641+01	4	Gebara	1	[{"added": {}}]	8	1
16	2023-11-09 15:22:52.259208+01	1	INCO	2	[]	10	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	studentform	school_cycle
8	studentform	student
9	studentform	contact
10	studentform	career
11	studentform	status
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2023-10-31 16:24:16.871624+01
2	auth	0001_initial	2023-10-31 16:24:17.042674+01
3	admin	0001_initial	2023-10-31 16:24:17.088787+01
4	admin	0002_logentry_remove_auto_add	2023-10-31 16:24:17.101665+01
5	admin	0003_logentry_add_action_flag_choices	2023-10-31 16:24:17.113592+01
6	contenttypes	0002_remove_content_type_name	2023-10-31 16:24:17.137223+01
7	auth	0002_alter_permission_name_max_length	2023-10-31 16:24:17.150903+01
8	auth	0003_alter_user_email_max_length	2023-10-31 16:24:17.16404+01
9	auth	0004_alter_user_username_opts	2023-10-31 16:24:17.175398+01
10	auth	0005_alter_user_last_login_null	2023-10-31 16:24:17.202214+01
11	auth	0006_require_contenttypes_0002	2023-10-31 16:24:17.206677+01
12	auth	0007_alter_validators_add_error_messages	2023-10-31 16:24:17.215973+01
13	auth	0008_alter_user_username_max_length	2023-10-31 16:24:17.24811+01
14	auth	0009_alter_user_last_name_max_length	2023-10-31 16:24:17.263826+01
15	auth	0010_alter_group_name_max_length	2023-10-31 16:24:17.267392+01
16	auth	0011_update_proxy_permissions	2023-10-31 16:24:17.281534+01
17	auth	0012_alter_user_first_name_max_length	2023-10-31 16:24:17.304224+01
18	sessions	0001_initial	2023-10-31 16:24:17.33179+01
19	studentform	0001_initial	2023-10-31 16:24:17.396644+01
20	studentform	0002_rename_contact_id_contact_idcontact_and_more	2023-10-31 16:24:17.440769+01
21	studentform	0003_alter_contact_emergency_phone_alter_contact_phone	2023-10-31 16:24:17.45711+01
22	studentform	0004_contact_company_contact_position	2023-10-31 16:32:08.486757+01
23	studentform	0005_remove_school_cycle_period_school_cycle_cycle_period_and_more	2023-10-31 16:40:05.479529+01
24	studentform	0006_alter_school_cycle_cycle_period_and_more	2023-10-31 16:41:30.935035+01
25	studentform	0007_career_status_student_first_last_name_and_more	2023-11-01 14:25:55.465013+01
26	studentform	0008_alter_student_admission_cycle_and_more	2023-11-01 14:26:51.573505+01
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
eiomupiec6oxx858zyu8ej3iqjfqn63c	.eJxVjEEOwiAQRe_C2pBCGSgu3fcMZBimUjWQlHZlvLtt0oVu33v_v0XAbc1ha7yEOYmrUOLyyyLSk8sh0gPLvUqqZV3mKI9EnrbJsSZ-3c727yBjy_uaBkugfJcQrdKRQAN0ttcQBxc1GMPeTC5ZC4g97ASQ_MSW0XnjkcTnC8xzN6g:1qxqxu:W-JY5jdAeSYWYlWaKctsBrLTeim07ZKd6FU2sxsDhHQ	2023-11-14 16:47:38.7424+01
\.


--
-- Data for Name: studentform_career; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.studentform_career ("idCareer", code_name, name, needed_credits, semesters) FROM stdin;
1	INCO	Ingenier├¡a en Computaci├│n	318	8
\.


--
-- Data for Name: studentform_contact; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.studentform_contact ("idContact", phone, email, udg_email, emergency_phone, url_socialnet, "idStudent_id", company, "position") FROM stdin;
4	001-443-761-5558x832	ravenayers@example.org	oclark@example.org	001-695-491-7764x440	\N	4	\N	\N
3	001-522-572-4830	mjones@example.org	mckayelizabeth@example.net	938.972.8989x18998	https://google.com	3	\N	\N
2	(846)449-1500x2638	brodriguez@example.org	alexisleonard@example.net	920-965-4055x2754	https://facebook.com	2	Oracle	Software Developer
1	753-640-3489	joshuazuniga@example.net	kingdavid@example.org	588.550.3845	https://x.com	1	San Mina	Minero
\.


--
-- Data for Name: studentform_school_cycle; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.studentform_school_cycle ("idCycle", cycle_period, end_date, start_date, year) FROM stdin;
2	A	2023-07-15	2023-01-16	2023
1	B	2023-01-15	2023-07-16	2023
\.


--
-- Data for Name: studentform_status; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.studentform_status ("idStatus", code_name, status) FROM stdin;
1	AC	Activo
2	IN	Inactivo
3	GD	Graduado
4	TT	Titulado
5	BC	Baja por Art 33
6	B4	Alumno en Art 34
7	B5	Baja por Art 35
\.


--
-- Data for Name: studentform_student; Type: TABLE DATA; Schema: public; Owner: django
--

COPY public.studentform_student ("idStudent", code, name, status_id, admission_cycle_id, first_last_name, last_cycle_id, second_last_name, "idCareer_id") FROM stdin;
1	218292955	Manuel Gerardo	1	2	Perez	1	Perez	1
2	123456789	Hernandez	2	2	Castro	2	Mercado	1
3	210394857	Israel Huerta	1	1	Mu├▒oz	1	Vel├ízquez	1
4	217391025	Gebara	2	2	Zandivar	1	Ortega	1
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 44, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 16, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 11, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 26, true);


--
-- Name: studentform_career_idCareer_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public."studentform_career_idCareer_seq"', 1, true);


--
-- Name: studentform_contact_contact_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.studentform_contact_contact_id_seq', 4, true);


--
-- Name: studentform_school_cycle_cycle_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.studentform_school_cycle_cycle_id_seq', 2, true);


--
-- Name: studentform_status_idStatus_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public."studentform_status_idStatus_seq"', 7, true);


--
-- Name: studentform_student_student_id_seq; Type: SEQUENCE SET; Schema: public; Owner: django
--

SELECT pg_catalog.setval('public.studentform_student_student_id_seq', 4, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: studentform_career studentform_career_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.studentform_career
    ADD CONSTRAINT studentform_career_pkey PRIMARY KEY ("idCareer");


--
-- Name: studentform_contact studentform_contact_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.studentform_contact
    ADD CONSTRAINT studentform_contact_pkey PRIMARY KEY ("idContact");


--
-- Name: studentform_contact studentform_contact_student_id_id_key; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.studentform_contact
    ADD CONSTRAINT studentform_contact_student_id_id_key UNIQUE ("idStudent_id");


--
-- Name: studentform_school_cycle studentform_school_cycle_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.studentform_school_cycle
    ADD CONSTRAINT studentform_school_cycle_pkey PRIMARY KEY ("idCycle");


--
-- Name: studentform_status studentform_status_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.studentform_status
    ADD CONSTRAINT studentform_status_pkey PRIMARY KEY ("idStatus");


--
-- Name: studentform_student studentform_student_code_key; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.studentform_student
    ADD CONSTRAINT studentform_student_code_key UNIQUE (code);


--
-- Name: studentform_student studentform_student_pkey; Type: CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.studentform_student
    ADD CONSTRAINT studentform_student_pkey PRIMARY KEY ("idStudent");


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: studentform_student_admission_cycle_id_bac68801; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX studentform_student_admission_cycle_id_bac68801 ON public.studentform_student USING btree (admission_cycle_id);


--
-- Name: studentform_student_code_211806d6_like; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX studentform_student_code_211806d6_like ON public.studentform_student USING btree (code varchar_pattern_ops);


--
-- Name: studentform_student_idCareer_id_a6161880; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX "studentform_student_idCareer_id_a6161880" ON public.studentform_student USING btree ("idCareer_id");


--
-- Name: studentform_student_last_cycle_id_105fce98; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX studentform_student_last_cycle_id_105fce98 ON public.studentform_student USING btree (last_cycle_id);


--
-- Name: studentform_student_status_id_3376e934; Type: INDEX; Schema: public; Owner: django
--

CREATE INDEX studentform_student_status_id_3376e934 ON public.studentform_student USING btree (status_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: studentform_contact studentform_contact_idStudent_id_18474103_fk_studentfo; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.studentform_contact
    ADD CONSTRAINT "studentform_contact_idStudent_id_18474103_fk_studentfo" FOREIGN KEY ("idStudent_id") REFERENCES public.studentform_student("idStudent") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: studentform_student studentform_student_admission_cycle_id_bac68801_fk_studentfo; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.studentform_student
    ADD CONSTRAINT studentform_student_admission_cycle_id_bac68801_fk_studentfo FOREIGN KEY (admission_cycle_id) REFERENCES public.studentform_school_cycle("idCycle") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: studentform_student studentform_student_idCareer_id_a6161880_fk_studentfo; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.studentform_student
    ADD CONSTRAINT "studentform_student_idCareer_id_a6161880_fk_studentfo" FOREIGN KEY ("idCareer_id") REFERENCES public.studentform_career("idCareer") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: studentform_student studentform_student_last_cycle_id_105fce98_fk_studentfo; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.studentform_student
    ADD CONSTRAINT studentform_student_last_cycle_id_105fce98_fk_studentfo FOREIGN KEY (last_cycle_id) REFERENCES public.studentform_school_cycle("idCycle") DEFERRABLE INITIALLY DEFERRED;


--
-- Name: studentform_student studentform_student_status_id_3376e934_fk_studentfo; Type: FK CONSTRAINT; Schema: public; Owner: django
--

ALTER TABLE ONLY public.studentform_student
    ADD CONSTRAINT studentform_student_status_id_3376e934_fk_studentfo FOREIGN KEY (status_id) REFERENCES public.studentform_status("idStatus") DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

