-- Table: public.tarefas_id

-- DROP TABLE IF EXISTS public.tarefas_id;

CREATE TABLE IF NOT EXISTS public.tarefas_id
(
    id integer NOT NULL,
    situacao character varying(500) COLLATE pg_catalog."default",
    atividade character varying(500) COLLATE pg_catalog."default",
    CONSTRAINT tarefas_id_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tarefas_id
    OWNER to m1478769;

REVOKE ALL ON TABLE public.tarefas_id FROM x09972752;

GRANT SELECT ON TABLE public.tarefas_id TO m13365929;

GRANT ALL ON TABLE public.tarefas_id TO m1478769;

GRANT SELECT ON TABLE public.tarefas_id TO m7532203;

GRANT SELECT ON TABLE public.tarefas_id TO x09972752;
