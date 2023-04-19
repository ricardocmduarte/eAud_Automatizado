-- Table: public.auto_avaliacao_iacm

-- DROP TABLE IF EXISTS public.auto_avaliacao_iacm;

CREATE TABLE IF NOT EXISTS public.auto_avaliacao_iacm
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
    anexosgerais character varying(5000) COLLATE pg_catalog."default",
    equipevalidacaoexterna character varying(5000) COLLATE pg_catalog."default",
    unidadevalidadoras character varying(5000) COLLATE pg_catalog."default",
    relatoriovalidacao character varying(5000) COLLATE pg_catalog."default",
    equipeiacm character varying(5000) COLLATE pg_catalog."default",
    unidadeauditoriasuptec character varying(5000) COLLATE pg_catalog."default",
    tarefaprecedentes character varying(5000) COLLATE pg_catalog."default",
    niveliacm integer,
    textohistorico character varying(5000) COLLATE pg_catalog."default",
    iacmplanoacao character varying(5000) COLLATE pg_catalog."default",
    unidadesuperior character varying(5000) COLLATE pg_catalog."default",
    mesconclusaoprevisto character varying(5000) COLLATE pg_catalog."default",
    textoajuda character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamentoespecifico character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT auto_avaliacao_iacm_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.auto_avaliacao_iacm
    OWNER to m1478769;

REVOKE ALL ON TABLE public.auto_avaliacao_iacm FROM m7532203;

GRANT SELECT ON TABLE public.auto_avaliacao_iacm TO m13365929;

GRANT ALL ON TABLE public.auto_avaliacao_iacm TO m1478769;

GRANT SELECT ON TABLE public.auto_avaliacao_iacm TO m7532203;
