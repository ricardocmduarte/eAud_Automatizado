-- Table: public.tarefas

-- DROP TABLE IF EXISTS public.tarefas;

CREATE TABLE IF NOT EXISTS public.tarefas
(
    id integer NOT NULL,
    atividade character varying(500) COLLATE pg_catalog."default",
    CONSTRAINT tarefas_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tarefas
    OWNER to m1478769;

REVOKE ALL ON TABLE public.tarefas FROM x09972752;

GRANT SELECT ON TABLE public.tarefas TO m13365929;

GRANT ALL ON TABLE public.tarefas TO m1478769;

GRANT SELECT ON TABLE public.tarefas TO m7532203;

GRANT SELECT ON TABLE public.tarefas TO x09972752;
