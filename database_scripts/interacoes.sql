-- Table: public.interacoes

-- DROP TABLE IF EXISTS public.interacoes;

CREATE TABLE IF NOT EXISTS public.interacoes
(
    id integer NOT NULL DEFAULT nextval('interacoes_id_seq'::regclass),
    tipointeracao character varying(1000) COLLATE pg_catalog."default",
    autor character varying(1000) COLLATE pg_catalog."default",
    idtarefa integer NOT NULL,
    unidadeautor character varying(1000) COLLATE pg_catalog."default",
    datamodificacao character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT interacoes_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.interacoes
    OWNER to m1478769;

REVOKE ALL ON TABLE public.interacoes FROM m13365929;
REVOKE ALL ON TABLE public.interacoes FROM m7532203;
REVOKE ALL ON TABLE public.interacoes FROM x09972752;

GRANT SELECT ON TABLE public.interacoes TO m13365929;

GRANT ALL ON TABLE public.interacoes TO m1478769;

GRANT SELECT ON TABLE public.interacoes TO m7532203;

GRANT SELECT ON TABLE public.interacoes TO x09972752;
