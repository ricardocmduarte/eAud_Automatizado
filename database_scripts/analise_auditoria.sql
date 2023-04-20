-- Table: public.analise_auditoria

-- DROP TABLE IF EXISTS public.analise_auditoria;

CREATE TABLE IF NOT EXISTS public.analise_auditoria
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
    descteste character varying(10485760) COLLATE pg_catalog."default",
    desccriterio character varying(10485760) COLLATE pg_catalog."default",
    descinformacao character varying(10485760) COLLATE pg_catalog."default",
    descfonte character varying(10485760) COLLATE pg_catalog."default",
    desclimitacao character varying(10485760) COLLATE pg_catalog."default",
    descachado character varying(10485760) COLLATE pg_catalog."default",
    observacoes character varying(10485760) COLLATE pg_catalog."default",
    descricaoescopo character varying(10485760) COLLATE pg_catalog."default",
    responsavelitem character varying(10485760) COLLATE pg_catalog."default",
    anexoescopo character varying(10485760) COLLATE pg_catalog."default",
    anexoevidencia character varying(10485760) COLLATE pg_catalog."default",
    autoranexoevidencia character varying(10485760) COLLATE pg_catalog."default",
    matrizachados character varying(5000) COLLATE pg_catalog."default",
    tarefasprecedentes character varying(5000) COLLATE pg_catalog."default",
    observadores character varying(5000) COLLATE pg_catalog."default",
    hipoteselegal character varying(5000) COLLATE pg_catalog."default",
    coordenadorequipe character varying(5000) COLLATE pg_catalog."default",
    equipegeral character varying(5000) COLLATE pg_catalog."default",
    supervisores character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamentoespecifico character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT analise_auditoria_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.analise_auditoria
    OWNER to m1478769;

REVOKE ALL ON TABLE public.analise_auditoria FROM x09972752;

GRANT SELECT ON TABLE public.analise_auditoria TO m13365929;

GRANT ALL ON TABLE public.analise_auditoria TO m1478769;

GRANT SELECT ON TABLE public.analise_auditoria TO m7532203;

GRANT SELECT ON TABLE public.analise_auditoria TO x09972752;
