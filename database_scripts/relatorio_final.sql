-- Table: public.relatorio_final

-- DROP TABLE IF EXISTS public.relatorio_final;

CREATE TABLE IF NOT EXISTS public.relatorio_final
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
    relatoriopreliminar character varying(5000) COLLATE pg_catalog."default",
    hipoteselegal character varying(5000) COLLATE pg_catalog."default",
    relatoriofinal character varying(5000) COLLATE pg_catalog."default",
    coordenadorequipe character varying(5000) COLLATE pg_catalog."default",
    supervisor character varying(5000) COLLATE pg_catalog."default",
    parecer character varying(5000) COLLATE pg_catalog."default",
    anexorelatorio character varying(5000) COLLATE pg_catalog."default",
    relatorioword character varying(5000) COLLATE pg_catalog."default",
    unidadesenvolvidas character varying(5000) COLLATE pg_catalog."default",
    relatoriocom character varying(5000) COLLATE pg_catalog."default",
    observadores character varying(5000) COLLATE pg_catalog."default",
    certificados character varying(5000) COLLATE pg_catalog."default",
    equipegeral character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamento character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT relatorio_final_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.relatorio_final
    OWNER to m1478769;

REVOKE ALL ON TABLE public.relatorio_final FROM m7532203;

GRANT SELECT ON TABLE public.relatorio_final TO m13365929;

GRANT ALL ON TABLE public.relatorio_final TO m1478769;

GRANT SELECT ON TABLE public.relatorio_final TO m7532203;
