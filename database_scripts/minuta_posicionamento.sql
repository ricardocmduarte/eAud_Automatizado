-- Table: public.minuta_posicionamento

-- DROP TABLE IF EXISTS public.minuta_posicionamento;

CREATE TABLE IF NOT EXISTS public.minuta_posicionamento
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
    providenciaminuta character varying(5000) COLLATE pg_catalog."default",
    anexosgerais character varying(5000) COLLATE pg_catalog."default",
    destinatariousuariounidade character varying(5000) COLLATE pg_catalog."default",
    tarefasprecedentes character varying(5000) COLLATE pg_catalog."default",
    textohistorico character varying(5000) COLLATE pg_catalog."default",
    acaoposicionamento character varying(5000) COLLATE pg_catalog."default",
    referenciarecomendacao character varying(5000) COLLATE pg_catalog."default",
    unidadesauditorias character varying(5000) COLLATE pg_catalog."default",
    tipoposicionamento character varying(5000) COLLATE pg_catalog."default",
    unidademonitorada character varying(5000) COLLATE pg_catalog."default",
    recomendacaominuta character varying(5000) COLLATE pg_catalog."default",
    detalhamentomonitoramento character varying(5000) COLLATE pg_catalog."default",
    arquivocomportamento character varying(5000) COLLATE pg_catalog."default",
    estadosituacao character varying(5000) COLLATE pg_catalog."default",
    tags character varying(5000) COLLATE pg_catalog."default",
    pendencias character varying(5000) COLLATE pg_catalog."default",
    abasatividade character varying(5000) COLLATE pg_catalog."default",
    CONSTRAINT minuta_posicionamento_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.minuta_posicionamento
    OWNER to m1478769;

REVOKE ALL ON TABLE public.minuta_posicionamento FROM x09972752;

GRANT SELECT ON TABLE public.minuta_posicionamento TO m13365929;

GRANT ALL ON TABLE public.minuta_posicionamento TO m1478769;

GRANT SELECT ON TABLE public.minuta_posicionamento TO m7532203;

GRANT SELECT ON TABLE public.minuta_posicionamento TO x09972752;
