-- Table: public.achados_auditoria

-- DROP TABLE IF EXISTS public.achados_auditoria;

CREATE TABLE IF NOT EXISTS public.achados_auditoria
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
    itensachadosauditoria character varying(10485760) COLLATE pg_catalog."default",
    anexosgerais character varying(5000) COLLATE pg_catalog."default",
    relatoriocom character varying(5000) COLLATE pg_catalog."default",
    tarefaprecedentes character varying(5000) COLLATE pg_catalog."default",
    observadores character varying(5000) COLLATE pg_catalog."default",
    hipoteselegal character varying(5000) COLLATE pg_catalog."default",
    coordenadorequipe character varying(5000) COLLATE pg_catalog."default",
    equipegeral character varying(5000) COLLATE pg_catalog."default",
    supervisores character varying(5000) COLLATE pg_catalog."default",
    anexosrelatorio character varying(5000) COLLATE pg_catalog."default",
    mesconclusaorealizado character varying(250) COLLATE pg_catalog."default",
    mesanoultimamodificacao character varying(50) COLLATE pg_catalog."default",
    arquivocomportamentoespecifico character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT achados_auditoria_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.achados_auditoria
    OWNER to m1478769;

REVOKE ALL ON TABLE public.achados_auditoria FROM x09972752;

GRANT SELECT ON TABLE public.achados_auditoria TO m13365929;

GRANT ALL ON TABLE public.achados_auditoria TO m1478769;

GRANT SELECT ON TABLE public.achados_auditoria TO m7532203;

GRANT SELECT ON TABLE public.achados_auditoria TO x09972752;
