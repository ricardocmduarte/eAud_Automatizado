-- Table: public.monitoramento

-- DROP TABLE IF EXISTS public.monitoramento;

CREATE TABLE IF NOT EXISTS public.monitoramento
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
    detalhesmonitoramento character varying(5000) COLLATE pg_catalog."default",
    providencia character varying(5000) COLLATE pg_catalog."default",
    unidadesauditoria character varying(5000) COLLATE pg_catalog."default",
    unidadesenvolvidas character varying(5000) COLLATE pg_catalog."default",
    categoriasmonitoramento character varying(5000) COLLATE pg_catalog."default",
    tarefasprecedentes character varying(5000) COLLATE pg_catalog."default",
    valorprejuizoestimado character varying(5000) COLLATE pg_catalog."default",
    observadores character varying(5000) COLLATE pg_catalog."default",
    unidadegestora character varying(5000) COLLATE pg_catalog."default",
    fundamentos character varying(5000) COLLATE pg_catalog."default",
    ultimoposicionamento character varying(5000) COLLATE pg_catalog."default",
    textoultimoposicionamento character varying(5000) COLLATE pg_catalog."default",
    textoultimamanifestacao character varying(5000) COLLATE pg_catalog."default",
    anexorelatorio character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamentoespecifico character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT monitoramento_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.monitoramento
    OWNER to m1478769;

REVOKE ALL ON TABLE public.monitoramento FROM x09972752;

GRANT SELECT ON TABLE public.monitoramento TO m13365929;

GRANT ALL ON TABLE public.monitoramento TO m1478769;

GRANT SELECT ON TABLE public.monitoramento TO m7532203;

GRANT SELECT ON TABLE public.monitoramento TO x09972752;
