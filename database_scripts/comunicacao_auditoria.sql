-- Table: public.comunicacao_auditoria

-- DROP TABLE IF EXISTS public.comunicacao_auditoria;

CREATE TABLE IF NOT EXISTS public.comunicacao_auditoria
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
    indminutadestinatario character varying(5000) COLLATE pg_catalog."default",
    detalhamento character varying(5000) COLLATE pg_catalog."default",
    anexogerais character varying(5000) COLLATE pg_catalog."default",
    destinatarios character varying(5000) COLLATE pg_catalog."default",
    copiacomunicacao character varying(5000) COLLATE pg_catalog."default",
    prazo character varying(5000) COLLATE pg_catalog."default",
    dataenviocomunicacao character varying(20) COLLATE pg_catalog."default",
    dataciencia character varying(20) COLLATE pg_catalog."default",
    indminutaremetente character varying(5000) COLLATE pg_catalog."default",
    tarefasprecedentes character varying(5000) COLLATE pg_catalog."default",
    unidadesenvolvidas character varying(5000) COLLATE pg_catalog."default",
    coordenadorequipe character varying(5000) COLLATE pg_catalog."default",
    equipegeral character varying(5000) COLLATE pg_catalog."default",
    supervisores character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamentoespecifico character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT comunicacao_auditoria_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.comunicacao_auditoria
    OWNER to m1478769;

REVOKE ALL ON TABLE public.comunicacao_auditoria FROM x09972752;

GRANT SELECT ON TABLE public.comunicacao_auditoria TO m13365929;

GRANT ALL ON TABLE public.comunicacao_auditoria TO m1478769;

GRANT SELECT ON TABLE public.comunicacao_auditoria TO m7532203;

GRANT SELECT ON TABLE public.comunicacao_auditoria TO x09972752;
