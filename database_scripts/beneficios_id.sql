-- Table: public.beneficios_id

-- DROP TABLE IF EXISTS public.beneficios_id;

CREATE TABLE IF NOT EXISTS public.beneficios_id
(
    id integer NOT NULL,
    atividade character varying(500) COLLATE pg_catalog."default",
    CONSTRAINT beneficios_id_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.beneficios_id
    OWNER to m1478769;
