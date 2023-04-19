-- Table: public.item_trabalho_atividade

-- DROP TABLE IF EXISTS public.item_trabalho_atividade;

CREATE TABLE IF NOT EXISTS public.item_trabalho_atividade
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
    unidadesexecutoras character varying(5000) COLLATE pg_catalog."default",
    detalhamento character varying(5000) COLLATE pg_catalog."default",
    anexosgerais character varying(5000) COLLATE pg_catalog."default",
    processoassociado character varying(5000) COLLATE pg_catalog."default",
    processt character varying(5000) COLLATE pg_catalog."default",
    origemdemanda character varying(5000) COLLATE pg_catalog."default",
    links character varying(5000) COLLATE pg_catalog."default",
    homemhora integer,
    unidadesenvolvidas character varying(5000) COLLATE pg_catalog."default",
    destinatariousuariounidade character varying(5000) COLLATE pg_catalog."default",
    tarefasprecedentes character varying(5000) COLLATE pg_catalog."default",
    executor character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamento character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT item_trabalho_atividade_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.item_trabalho_atividade
    OWNER to m1478769;

REVOKE ALL ON TABLE public.item_trabalho_atividade FROM x09972752;

GRANT SELECT ON TABLE public.item_trabalho_atividade TO m13365929;

GRANT ALL ON TABLE public.item_trabalho_atividade TO m1478769;

GRANT SELECT ON TABLE public.item_trabalho_atividade TO m7532203;

GRANT SELECT ON TABLE public.item_trabalho_atividade TO x09972752;
