-- Table: public.apuracao_preliminar

-- DROP TABLE IF EXISTS public.apuracao_preliminar;

CREATE TABLE IF NOT EXISTS public.apuracao_preliminar
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
    unidadesenvolvidas character varying(5000) COLLATE pg_catalog."default",
    universosauditaveis character varying(5000) COLLATE pg_catalog."default",
    anexosgerais character varying(5000) COLLATE pg_catalog."default",
    objetosauditoria character varying(5000) COLLATE pg_catalog."default",
    matrizcontrole character varying(5000) COLLATE pg_catalog."default",
    tarefasprecedentes character varying(5000) COLLATE pg_catalog."default",
    observadores character varying(5000) COLLATE pg_catalog."default",
    hipoteselegal character varying(5000) COLLATE pg_catalog."default",
    coordenadorequipe character varying(5000) COLLATE pg_catalog."default",
    equipegeral character varying(5000) COLLATE pg_catalog."default",
    classificacaoacesso character varying(5000) COLLATE pg_catalog."default",
    supervisores character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamentoespecifico character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT apuracao_preliminar_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.apuracao_preliminar
    OWNER to m1478769;

REVOKE ALL ON TABLE public.apuracao_preliminar FROM x09972752;

GRANT SELECT ON TABLE public.apuracao_preliminar TO m13365929;

GRANT ALL ON TABLE public.apuracao_preliminar TO m1478769;

GRANT SELECT ON TABLE public.apuracao_preliminar TO m7532203;

GRANT SELECT ON TABLE public.apuracao_preliminar TO x09972752;
