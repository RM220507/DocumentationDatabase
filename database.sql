BEGIN; 

DROP DATABASE IF EXISTS documentation;

CREATE DATABASE documentation
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_GB.UTF-8'
    LC_CTYPE = 'en_GB.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

ALTER DEFAULT PRIVILEGES FOR ROLE postgres
GRANT INSERT, SELECT, UPDATE, DELETE ON TABLES TO client;


CREATE SCHEMA IF NOT EXISTS public
    AUTHORIZATION postgres;

COMMENT ON SCHEMA public
    IS 'standard public schema';

GRANT ALL ON SCHEMA public TO PUBLIC;

GRANT ALL ON SCHEMA public TO postgres;


DROP TABLE IF EXISTS public.languages;

CREATE TABLE IF NOT EXISTS public.languages
(
    langid integer NOT NULL DEFAULT nextval('languages_langid_seq'::regclass),
    name character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT languages_pkey PRIMARY KEY (langid),
    CONSTRAINT langnameunique UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.languages
    OWNER to postgres;

GRANT DELETE, INSERT, SELECT, UPDATE ON TABLE public.languages TO client;

GRANT ALL ON TABLE public.languages TO postgres;


DROP TABLE IF EXISTS public.links;

CREATE TABLE IF NOT EXISTS public.links
(
    linkid integer NOT NULL DEFAULT nextval('links_linkid_seq'::regclass),
    name character(255) COLLATE pg_catalog."default" NOT NULL,
    link character varying(512) COLLATE pg_catalog."default" NOT NULL,
    type boolean DEFAULT false,
    langid integer NOT NULL DEFAULT nextval('links_langid_seq'::regclass),
    CONSTRAINT links_pkey PRIMARY KEY (linkid),
    CONSTRAINT language FOREIGN KEY (langid)
        REFERENCES public.languages (langid) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.links
    OWNER to postgres;

GRANT DELETE, INSERT, SELECT, UPDATE ON TABLE public.links TO client;

GRANT ALL ON TABLE public.links TO postgres;

END;