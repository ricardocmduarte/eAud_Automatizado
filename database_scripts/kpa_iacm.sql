-- Table: public.kpa_iacm

-- DROP TABLE IF EXISTS public.kpa_iacm;

CREATE TABLE IF NOT EXISTS public.kpa_iacm
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
    conclusaokpa character varying(5000) COLLATE pg_catalog."default",
    anexosgerais character varying(5000) COLLATE pg_catalog."default",
    objetivokpa character varying(5000) COLLATE pg_catalog."default",
    equipevalidacaoexternaiacm character varying(5000) COLLATE pg_catalog."default",
    atividaeskpa character varying(10485760) COLLATE pg_catalog."default",
    equipeavaliacaoiacm character varying(5000) COLLATE pg_catalog."default",
    titulokpamodelo character varying(5000) COLLATE pg_catalog."default",
    datarealizadamodelokpa character varying(20) COLLATE pg_catalog."default",
    datafimmodelokpa character varying(20) COLLATE pg_catalog."default",
    assundomodelokpa character varying(5000) COLLATE pg_catalog."default",
    unidadesvalidadoras character varying(5000) COLLATE pg_catalog."default",
    produtokpa character varying(10485760) COLLATE pg_catalog."default",
    resultadoskpa character varying(10485760) COLLATE pg_catalog."default",
    praticakpa character varying(10485760) COLLATE pg_catalog."default",
    links character varying(5000) COLLATE pg_catalog."default",
    uaigs character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamentoespecifico character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT kpa_iacm_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.kpa_iacm
    OWNER to m1478769;

REVOKE ALL ON TABLE public.kpa_iacm FROM x09972752;

GRANT SELECT ON TABLE public.kpa_iacm TO m13365929;

GRANT ALL ON TABLE public.kpa_iacm TO m1478769;

GRANT SELECT ON TABLE public.kpa_iacm TO m7532203;

GRANT SELECT ON TABLE public.kpa_iacm TO x09972752;
