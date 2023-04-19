-- Table: public.planejamento_consultoria

-- DROP TABLE IF EXISTS public.planejamento_consultoria;

CREATE TABLE IF NOT EXISTS public.planejamento_consultoria
(
    id integer NOT NULL,
    situacao character varying(255) COLLATE pg_catalog."default",
    estado character varying(255) COLLATE pg_catalog."default",
    atividade character varying(255) COLLATE pg_catalog."default",
    titulo character varying(1000) COLLATE pg_catalog."default",
    idtarefaassociada integer,
    titulotarefaassociada character varying(500) COLLATE pg_catalog."default",
    dtprevisaoinicio character varying(50) COLLATE pg_catalog."default",
    dtprevisaofim character varying(50) COLLATE pg_catalog."default",
    dtrealizadainicio character varying(50) COLLATE pg_catalog."default",
    dtrealizadafim character varying(50) COLLATE pg_catalog."default",
    prioridade character varying(255) COLLATE pg_catalog."default",
    assunto character varying(5000) COLLATE pg_catalog."default",
    idatividade integer,
    descricaoatividade character varying(5000) COLLATE pg_catalog."default",
    idsituacao integer,
    dataultimamodificacao character varying(50) COLLATE pg_catalog."default",
    autorultimamodificacao character varying(500) COLLATE pg_catalog."default",
    analisepreliminar character varying(5000) COLLATE pg_catalog."default",
    unidadesenvolvidas character varying(5000) COLLATE pg_catalog."default",
    anexosgerais character varying(5000) COLLATE pg_catalog."default",
    observadores character varying(5000) COLLATE pg_catalog."default",
    hipoteselegal character varying(5000) COLLATE pg_catalog."default",
    docplanejamento character varying(5000) COLLATE pg_catalog."default",
    coordenadorequipe character varying(5000) COLLATE pg_catalog."default",
    equipegeral character varying(5000) COLLATE pg_catalog."default",
    supervisores character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamento character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT planejamento_consultoria_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.planejamento_consultoria
    OWNER to m1478769;

REVOKE ALL ON TABLE public.planejamento_consultoria FROM x09972752;

GRANT SELECT ON TABLE public.planejamento_consultoria TO m13365929;

GRANT ALL ON TABLE public.planejamento_consultoria TO m1478769;

GRANT SELECT ON TABLE public.planejamento_consultoria TO m7532203;

GRANT SELECT ON TABLE public.planejamento_consultoria TO x09972752;
